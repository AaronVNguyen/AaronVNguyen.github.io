----------------------------------------------------------------------------------
-- Name: Aaron Nguyen
--       Patrick Soper
--
-- Date: April 28, 2016
-- 
-- Description: Top Level RAT CPU
----------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity RAT_CPU is
    Port ( IN_PORT : in  STD_LOGIC_VECTOR (7 downto 0);
           RESET : in  STD_LOGIC;
           CLK : in  STD_LOGIC;           
           OUT_PORT : out  STD_LOGIC_VECTOR (7 downto 0);
           PORT_ID : out  STD_LOGIC_VECTOR (7 downto 0);
           IO_STRB : out  STD_LOGIC);
end RAT_CPU;

architecture Behavioral of RAT_CPU is
  -- Component Declarations
    component prog_rom  
        port ( ADDRESS : in std_logic_vector(9 downto 0); 
               INSTRUCTION : out std_logic_vector(17 downto 0); 
               CLK : in std_logic);  
    end component;
    
    component PC is
        Port ( CLK      : in STD_LOGIC;
               RST      : in STD_LOGIC;                                     -- active high
               LD, INC  : in STD_LOGIC;                                     -- active high
               DIN      : in STD_LOGIC_VECTOR(9 downto 0);
               PC_COUNT : out STD_LOGIC_VECTOR(9 downto 0) := "0000000001" );
    end component;
   
    component FLAGS is
        Port ( CLK          : in STD_LOGIC;
               CLR, SET, LD : in STD_LOGIC;
               DATA_IN      : in STD_LOGIC;
               DATA_OUT     : out STD_LOGIC );
    end component;

    component REG_FILE is
        Port ( WR, CLK: in std_logic;
               DIN: in std_logic_vector(7 downto 0);
               ADRX: in std_logic_vector (12 downto 8);
               ADRY: in std_logic_vector (7 downto 3);
               DY_OUT, DX_OUT: out std_logic_vector (7 downto 0));
    end component;
    
    component ALU is
        Port ( CIN : in STD_LOGIC;
               SEL : in STD_LOGIC_VECTOR (3 downto 0);
               A : in STD_LOGIC_VECTOR (7 downto 0);
               B : in STD_LOGIC_VECTOR (7 downto 0);
               RESULT : out STD_LOGIC_VECTOR (7 downto 0);
               C : out STD_LOGIC;
               Z : out STD_LOGIC);
    end component;      
    
    component CONTROL_UNIT is
        Port ( CLK           : in   STD_LOGIC;
               C             : in   STD_LOGIC;
               Z             : in   STD_LOGIC;
               RESET         : in   STD_LOGIC;
               OPCODE_HI_5   : in   STD_LOGIC_VECTOR (4 downto 0);
               OPCODE_LO_2   : in   STD_LOGIC_VECTOR (1 downto 0);
               
               PC_LD         : out  STD_LOGIC;
               PC_INC        : out  STD_LOGIC;
               PC_MUX_SEL    : out  STD_LOGIC_VECTOR (1 downto 0);
               
               RF_WR         : out  STD_LOGIC;
               RF_WR_SEL     : out  STD_LOGIC_VECTOR (1 downto 0);
               
               
               
               ALU_OPY_SEL   : out  STD_LOGIC;
               ALU_SEL       : out  STD_LOGIC_VECTOR (3 downto 0);
                
               FLG_C_LD      : out  STD_LOGIC;
               FLG_C_SET     : out  STD_LOGIC;
               FLG_C_CLR     : out  STD_LOGIC;
               FLG_Z_LD      : out  STD_LOGIC;
               FLG_Z_CLR     : out  STD_LOGIC;
               
               IO_STRB       : out  STD_LOGIC;
               
               RST           : out  STD_LOGIC);          
    end component;
    
    component SCR is
        Port( CLK       : in STD_LOGIC;
              WE        : in STD_lOGIC;
              ADDR      : in STD_LOGIC_VECTOR(7 downto 0);
              DATA_IN   : in STD_LOGIC_VECTOR(9 downto 0);
              DATA_OUT  : out STD_LOGIC_VECTOR(9 downto 0) );
    end component;
    
    component SP is
      port (RST,CLK,LD,INCR,DECR : in std_logic;
            DATA_IN              : in std_logic_vector (7 downto 0);
            DATA_OUT             : out std_logic_vector (7 downto 0));
    end component;
    
  -- Control Signals
    signal I_SET, I_CLR : STD_LOGIC;
    signal PC_LD, PC_INC : STD_LOGIC;
    signal PC_MUX_SEL : STD_LOGIC_VECTOR(1 downto 0);
    signal ALU_OPY_SEL : STD_LOGIC;
    signal ALU_SEL : STD_LOGIC_VECTOR(3 downto 0);
    signal RF_WR : STD_LOGIC;
    signal RF_WR_SEL : STD_LOGIC_VECTOR(1 downto 0);
    signal SP_LD, SP_INCR, SP_DECR : STD_LOGIC;
    signal SCR_WE, SCR_DATA_SEL : STD_LOGIC := '0'; --unused currently
    signal SCR_ADDR_SEL : STD_LOGIC_VECTOR(1 downto 0);
    signal FLG_C_SET, FLG_C_CLR, FLG_LD_SEL, FLG_C_LD, FLG_Z_LD, FLG_Z_CLR, FLG_SHAD_LD : STD_LOGIC;
    signal C_FLAG, Z_FLAG : STD_LOGIC;
    signal RST : STD_LOGIC;
    
  --Data Signals
    signal INSTRUCTION : STD_LOGIC_VECTOR(17 downto 0);
    
    signal PC_MUX_OUT, PC_COUNT : STD_LOGIC_VECTOR(9 downto 0);

    signal RF_MUX_OUT, REGX_OUT, REGY_OUT : STD_LOGIC_VECTOR(7 downto 0);

    signal ALU_MUX_OUT, ALU_RESULT : STD_LOGIC_VECTOR(7 downto 0);
    signal ALU_C_OUT, ALU_Z_OUT : STD_LOGIC;
    
    signal SP_DOUT : STD_LOGIC_VECTOR(7 downto 0);
    
    
    signal SCR_DATA_MUX_OUT, SCR_DOUT : STD_LOGIC_VECTOR(9 downto 0);
    signal SCR_ADDR_MUX_OUT : STD_LOGIC_VECTOR(7 downto 0);
begin
    program: prog_rom
        PORT MAP (
            ADDRESS => PC_COUNT,
            INSTRUCTION => INSTRUCTION,
            CLK => CLK
        );
  -- Begin Portmapping
    CU: CONTROL_UNIT
        PORT MAP ( 
            CLK => CLK,
            C => C_FLAG,
            Z => Z_FLAG,
            RESET => RESET,
            OPCODE_HI_5 => INSTRUCTION(17 downto 13),
            OPCODE_LO_2 => INSTRUCTION(1 downto 0),
            
            PC_LD => PC_LD,
            PC_INC => PC_INC,
            PC_MUX_SEL => PC_MUX_SEL,
            
            RF_WR => RF_WR,
            RF_WR_SEL => RF_WR_SEL,
            
            ALU_OPY_SEL => ALU_OPY_SEL,
            ALU_SEL => ALU_SEL,
            
            FLG_C_LD => FLG_C_LD,
            FLG_C_SET => FLG_C_SET,
            FLG_C_CLR => FLG_C_CLR,
            FLG_Z_LD => FLG_Z_LD,
            FLG_Z_CLR => FLG_Z_CLR,
            
            IO_STRB => IO_STRB,
            RST => RST
        );
        
    PCOUNTER: PC
        PORT MAP (
            CLK => CLK,
            RST => RST,
            LD => PC_LD,
            INC => PC_INC,
            DIN => PC_MUX_OUT,
            PC_COUNT => PC_COUNT
        );
        
    ZERO_REG: FLAGS
        PORT MAP (
            CLK => CLK,
            CLR => FLG_Z_CLR,
            SET => '0',
            LD => FLG_Z_LD,
            DATA_IN => ALU_Z_OUT,
            DATA_OUT => Z_FLAG
        );
    
    CARRY_REG: FLAGS
        PORT MAP (
            CLK => CLK,
            CLR => FLG_C_CLR,
            SET => FLG_C_SET,
            LD => FLG_C_LD,
            DATA_IN => ALU_C_OUT,
            DATA_OUT => C_FLAG
        );
        
    REGISTER_FILE: REG_FILE
        PORT MAP (
            CLK => CLK,
            WR => RF_WR,
            DIN => RF_MUX_OUT,
            ADRX => INSTRUCTION(12 downto 8),
            ADRY => INSTRUCTION(7 downto 3),
            DX_OUT => REGX_OUT,
            DY_OUT => REGY_OUT 
        );
        
    LOGIC_UNIT: ALU
        PORT MAP(
            CIN => C_FLAG,
            SEL => ALU_SEL,
            A => REGX_OUT,
            B => ALU_MUX_OUT,
            RESULT => ALU_RESULT,
            C => ALU_C_OUT,
            Z => ALU_Z_OUT
        );

    STACK: SP
        PORT MAP(
            CLK => CLK,
            RST => RST,
            LD => SP_LD,
            INCR => SP_INCR,
            DECR => SP_DECR,
            DATA_IN => REGX_OUT,
            DATA_OUT => SP_DOUT
        );
        
    SCRATCH_RAM: SCR
        PORT MAP(
            CLK => CLK,
            DATA_IN => SCR_DATA_MUX_OUT,
            WE => SCR_WE,
            ADDR => SCR_ADDR_MUX_OUT,
            DATA_OUT => SCR_DOUT
        );
  --remember to list all of the port names on the left and the signal they are being
  --ported to on the right.  Use the port map operator =>
  
  -- muxes
    with PC_MUX_SEL select
        PC_MUX_OUT <= INSTRUCTION(12 downto 3) when "00",
                      SCR_DOUT when "01",
                      "11" & x"FF" when "10",
                      "0000000000" when others;

    with RF_WR_SEL select
        RF_MUX_OUT <= ALU_RESULT when "00",
                      SCR_DOUT(7 downto 0) when "01",
                      SP_DOUT when "10",
                      IN_PORT when others;
                           
    with ALU_OPY_SEL select
        ALU_MUX_OUT <= REGY_OUT when '0',
                       INSTRUCTION(7 downto 0) when others;

    with SCR_DATA_SEL select
        SCR_DATA_MUX_OUT <= "00" & REGX_OUT when '0',
                            PC_COUNT when others;
                            
    with SCR_ADDR_SEL select
        SCR_ADDR_MUX_OUT <= REGY_OUT when "00",
                            INSTRUCTION(7 downto 0) when "01",
                            SP_DOUT - 1 when "11",
                            SP_DOUT when others;
                            
  -- Outputs
    PORT_ID <= INSTRUCTION(7 downto 0);
    OUT_PORT <= REGX_OUT;

end Behavioral;

