;-------------------------------------
;   Keyboard and Bufferless VGA Demo Assembly Program
;	Authors: Bridget Benson and Ryan Rumsey
;	Date:	5/4/16
;-------------------------------------

;------------------
;- Port Definitions
;------------------
.EQU	X_POS_EN_ID	= 0xA1	;VGA Controller port X_POS_EN
.EQU	Y_POS_ID	= 0xA2	;VGA Controller port Y_POS
.EQU	RGB_DATA_ID	= 0xA3  ;VGA Controller port RGB_DATA_IN
.EQU	OBJ_ADDR_ID	= 0xA4	;VGA Controller port OBJ_ADDR
.EQU	SSEG_ID		= 0x80  ;Seven Segment Display
.EQU	LEDS_ID		= 0x40  
.EQU	SWITCHES_ID = 0x20
.EQU	BUTTONS_ID  = 0x24
.EQU	PS2_KEY_CODE_ID = 0x30
.EQU	PS2_CONTROL_ID = 0x32

;------------------
;- Bit Masks
;------------------
.EQU	EN_MASK		= 0x80  ;Enable bit is in MSB position of X_POS_EN

;------------------------------------------------------------------
; Various Keyboard Definitions
;------------------------------------------------------------------
.EQU KEY_UP     = 0xF0        ; key release data
.EQU int_flag   = 0x01        ; interrupt hello from keyboard
.EQU P1_UP       = 0x1D       ; 'w' 
.EQU P1_DOWN     = 0x1B    	  ; 's'
.EQU P2_UP		= 0x44		  ; 'o'
.EQU P2_DOWN 	= 0x42		  ; 'k'
;------------------------------------------------------------

;------------------
;- Delay Constants
;------------------
.EQU	OUTER_CONST	 = 0x7F
.EQU	MIDDLE_CONST = 0x0F
.EQU	INNER_CONST  = 0x0F
;------------------
;- VGA Boundaries
;------------------
.EQU	MAX_X		= 0xCF  ;Maximum X position
.EQU	MAX_Y		= 0x3B	;Maximum Y position
;------------------
;- Object Memory
;------------------
.EQU	OBJ0_MEM		= 0x00	;Stack address for Object 0 info
.EQU	OBJ1_MEM		= 0x03	;Stack address for Object 1 info
.EQU	OBJ2_MEM		= 0x06	;Stack address for Object 2 info
.EQU 	P1_PADDLE_MEM 	= 0x09
.EQU 	P2_PADDLE_MEM 	= 0x0C
.EQU 	BALL_MEM		= 0x0F

;----------------------
;- Register Definitions
;----------------------
.DEF	R_X_POS_EN	= r0
.DEF	R_Y_POS		= r1
.DEF	R_RGB_DATA	= r2
.DEF	R_OBJ_ADDR	= r3
.DEF	R_ARGUMENT	= r31
.DEF	R_BALL_TRAV_X = r4	;1 left, 2 right
.DEF 	R_BALL_TRAV_Y = r5	;1 up, 2 down
.DEF	R_PADDLE_LOC_X = r6
.DEF	R_PADDLE_LOC_Y = r7

.CSEG 
.ORG 0x01


init:		;Enable Player 1 
			MOV		R_X_POS_EN, 0
			OR		R_X_POS_EN, EN_MASK
			MOV		R_Y_POS, 	30
			MOV		R_RGB_DATA, 0x00
			MOV		R_OBJ_ADDR, 0x04
			CALL	update_obj
			MOV		R_ARGUMENT, P1_PADDLE_MEM	;Set up r31 with mem address
			CALL	set_obj_data
			;Enable Player 2
			MOV		R_X_POS_EN, 255
			OR		R_X_POS_EN, EN_MASK
			MOV		R_Y_POS, 	30
			MOV		R_RGB_DATA, 0x00
			MOV		R_OBJ_ADDR, 0x05
			CALL	update_obj
			MOV		R_ARGUMENT, P2_PADDLE_MEM	;Set up r31 with mem address
			CALL	set_obj_data
			;Enable Ball (man)
			MOV		R_X_POS_EN, 40
			OR		R_X_POS_EN, EN_MASK
			MOV		R_Y_POS, 	30
			MOV		R_RGB_DATA, 0x00
			MOV		R_OBJ_ADDR, 0x06
			CALL	update_obj
			MOV		R_ARGUMENT, BALL_MEM	;Set up r31 with mem address
			CALL	set_obj_data
			;Initialize ball direction
			MOV 	R_BALL_TRAV_X 0x01
			MOV		R_BALL_TRAV_Y 0x00
			

main:       MOV		R_ARGUMENT, P1_PADDLE_MEM  ;select to move paddle 1
			MOV		R_OBJ_ADDR, 0x04
			CALL    get_obj_data
			MOV		R_ARGUMENT, P2_PADDLE_MEM  ;select to move paddle 2
			MOV		R_OBJ_ADDR, 0x05
			CALL    get_obj_data
			SEI

			
loop:		IN		r20, SWITCHES_ID 	;just to test switches 
			OUT		r20, LEDS_ID		;just to test LEDS
			;ball logic

			;check logic
			MOV		R_OBJ_ADDR, 0x06
			CALL	get_obj_data
			CMP		
			CMP		R_BALL_TRAV_X, 0x01
			BRNE 	check_right
			

check_left:	MOV 	R_OBJ_ADDR, 0x04
			CALL 	get_obj_data		;get left paddle data
			MOV		R_PADDLE_LOC_X, R_X_POS_EN
			MOV 	R_PADDLE_LOC_Y, R_Y_POS
			;BRN		get_ball
			MOV		R_OBJ_ADDR, 0x06
			CALL 	get_obj_data
			CMP 	R_X_POS_EN, R_PADDLE_LOC_X
			BREQ	change_dir
			BRCS	game_over
			BRN 	loop

check_right:MOV 	R_OBJ_ADDR, 0x04
			CALL 	get_obj_data		;get left paddle data
			MOV		R_PADDLE_LOC_X, R_X_POS_EN
			MOV 	R_PADDLE_LOC_Y, R_Y_POS
			;BRN		get_ball
			MOV		R_OBJ_ADDR, 0x06
			CALL 	get_obj_data
			CMP 	R_X_POS_EN, R_PADDLE_LOC_X
			BREQ	change_dir
			BRCS	game_over
			BRN 	loop

game_over:	;something here
			BRN		loop				;hang out here waiting for keyboard interrupts

		
;------------------------------------------------------------
;- These subroutines add and/or subtract '1' from the given 
;- X or Y value, depending on the direction the object was 
;- told to go. The trick here is to not go off the screen
;- so the object is moved only if there is room to move the 
;- object without going off the screen.  
;- 
;- Tweaked Registers: possibly r0, r1 (X and Y positions)
;------------------------------------------------------------
sub_y:   CMP   R_Y_POS,0x00    ; see if you can move
         BREQ  done2
         SUB   R_Y_POS,0x01    ; move if you can
done2:   RET

add_y:   CMP   R_Y_POS,MAX_Y    ; see if you can move
         BREQ  done4   
         ADD   R_Y_POS,0x01    ; move if you can
done4:   RET


;------------------------------------
; Subroutine get_obj_data
; Loads object data (X_POS, Y_POS, and color)
; from the stack based on address in r4
;
; R_ARGUMENT (r31) - Stack address
;------------------------------------
get_obj_data:
			LD		R_X_POS_EN, (r31)
			ADD		R_ARGUMENT, 0x01
			LD		R_Y_POS, 	(r31)
			ADD		R_ARGUMENT, 0x01
			LD		R_RGB_DATA, (r31)
			RET

;------------------------------------
; Subroutine set_obj_data
; Stores object data onto the stack based on address in r4
; Uses 3 memory words
;
; R_ARGUMENT (r31) - Stack address
;------------------------------------
set_obj_data:
			ST		R_X_POS_EN, (r31)
			ADD		R_ARGUMENT, 0x01
			ST		R_Y_POS, 	(r31)
			ADD		R_ARGUMENT, 0x01
			ST		R_RGB_DATA, (r31)
			RET

;------------------------------------
; Subroutine update_obj
;
; r0 - X_POS_EN
; r1 - Y_POS
; r2 - RGB_DATA
; r3 - OBJ_ADDR

;------------------------------------
update_obj:
			MOV		r4, R_OBJ_ADDR			;r4 is temp address
			OUT		r0, X_POS_EN_ID
			OUT		r1, Y_POS_ID
			OUT		r2, RGB_DATA_ID
			OUT		r4, OBJ_ADDR_ID
			MOV		r4, 0
			OUT		r4, OBJ_ADDR_ID
			RET

;------------------------------------
; Subroutine delay
; Delays the CPU by doing a long nested loop
;
;------------------------------------
delay:
					MOV		r29, OUTER_CONST
delay_outer:		MOV		r28, MIDDLE_CONST
					CMP		r29, 0x00
					BREQ	delay_done
delay_middle:		MOV		r27, INNER_CONST
					CMP		r28, 0x00
					BREQ	delay_mid_done
delay_inner:		CMP		r27, 0x00
					BREQ	delay_inner_done
					SUB		r27, 0x01	;sub inner count
					BRN		delay_inner
delay_inner_done:	SUB		r28, 0x01	;sub middle count
					BRN		delay_middle
delay_mid_done:		SUB		r29, 0x01	;sub outer count
					BRN		delay_outer
delay_done:			RET


;--------------------------------------------------------------
; Interrup Service Routine - Handles Interrupts from keyboard
;--------------------------------------------------------------
; Sample ISR that looks for various key presses. When a useful
; key press is found, the program does something useful. The 
; code also handles the key-up code and subsequent re-sending
; of the associated scan-code. 
;
; Tweaked Registers; r6, r15
;--------------------------------------------------------------
ISR:      CMP   r15, int_flag        ; check key-up flag 
          BRNE  continue
          MOV   r15, 0x00            ; clean key-up flag
          BRN   reset_ps2_register       

continue: IN    r6, PS2_KEY_CODE_ID     ; get keycode data
          OUT	r6, SSEG_ID
move_up:  CMP   r6, UP               ; decode keypress value
          BRNE  move_down 		  
          CALL  sub_y                ; verify move is possible
          CALL  update_obj             ; draw object
          BRN   reset_ps2_register

move_down:
          CMP   r6, DOWN
          BRNE  move_left 		  
          CALL  add_y                ; verify move
          CALL  update_obj             ; draw object
          BRN   reset_ps2_register
    
key_up_check:  
          CMP   r6,KEY_UP            ; look for key-up code 
		 
          BRNE  reset_ps2_register   ; branch if not found

set_skip_flag:
          ADD   r15, 0x01            ; indicate key-up found


reset_ps2_register:                  ; reset PS2 register 
          MOV    r6, 0x01
          OUT    r6, PS2_CONTROL_ID 
          MOV    r6, 0x00
          OUT    r6, PS2_CONTROL_ID
		  RETIE
;-------------------------------------------------------------------

;---------------------------------------------------------------------
; interrupt vector 
;---------------------------------------------------------------------
.CSEG
.ORG 0x3FF
           BRN   ISR
;---------------------------------------------------------------------
