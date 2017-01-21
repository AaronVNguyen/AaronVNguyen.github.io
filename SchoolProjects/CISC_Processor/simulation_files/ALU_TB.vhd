------------------------------------------------------------------------------------------------------------------
-- Programer: Aaron Nguyen
--            Patrick Soper
-- 
-- Date:      04/21/16
-- 
-- Description: Test Bench for ALU. Expected results in the corresponding ALU document table.
------------------------------------------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity ALU_TB is
end ALU_TB;

architecture ALU_TB_Behavioral of ALU_TB is
    component ALU is
        Port ( CIN      : in STD_LOGIC;
               SEL      : in STD_LOGIC_VECTOR (3 downto 0);
               A        : in STD_LOGIC_VECTOR (7 downto 0);
               B        : in STD_LOGIC_VECTOR (7 downto 0);
               RESULT   : out STD_LOGIC_VECTOR (7 downto 0);
               C        : out STD_LOGIC;
               Z        : out STD_LOGIC);
    end component;
    
    signal CLK : STD_LOGIC;
    constant CLK_period : time := 10 ns;
    
    signal CIN      : STD_LOGIC;
    signal SEL      : STD_LOGIC_VECTOR(3 downto 0);
    signal A        : STD_LOGIC_VECTOR(7 downto 0);
    signal B        : STD_LOGIC_VECTOR (7 downto 0);
    signal RESULT   : STD_LOGIC_VECTOR (7 downto 0);
    signal C        : STD_LOGIC;
    signal Z        : STD_LOGIC;

begin
    -- ALU is the unit under test.
    uut: ALU port map (
        CIN => CIN,
        SEL => SEL,
        A => A,
        B => B,
        RESULT => RESULT,
        C => C,
        Z => Z
    );
    
    -- Creating a CLK with period of 10ns and 50% duty cycle.
    CLK_process: process
    begin
        CLK <= '0';
        wait for CLK_period/2;
        CLK <= '1';
        wait for CLK_period/2;
    end process;
    
    -- Beginning of the ALU simulation.
    ALU_sim: process
    begin
        --ADD
        SEL <= "0000";
        A   <= x"AA";
        B   <= x"AA";
        CIN <= '0';
        wait for CLK_period;
        
        CIN <= '1';
        wait for CLK_period;
        
        --ADDC
        SEL <= "0001";
        A   <= x"C8";
        B   <= x"37";
        CIN <= '1';
        wait for CLK_period;
        
        CIN <= '0';
        wait for CLK_period;
        
        --SUB
        SEL <= "0010";
        A   <= x"C8";
        B   <= x"C8";
        CIN <= '1';
        wait for CLK_period;
        CIN <= '0';
        wait for CLK_period;
        
        --SUBC
        SEL <= "0011";
        A   <= x"C8";
        B   <= x"C8"; 
        CIN <= '1';
        wait for CLK_period;
        CIN <= '0';
        wait for CLK_period; 
        
        --CMP
        SEL <= "0100";
        A   <= x"AA";
        B   <= x"FF";
        CIN <= '0';
        wait for CLK_period;
        B   <= x"AA";
        CIN <= '1';
        wait for CLK_period;
        
        --AND
        SEL <= "0101";
        A   <= x"AA";
        B   <= x"CC";
        CIN <= '0';
        wait for CLK_period;
        
        --OR
        SEL <= "0110";
        A   <= x"AA";
        B   <= x"AA";
        CIN <= '1';
        wait for CLK_period;
        
        --EXOR
        SEL <= "0111";
        A   <= x"AA";
        B   <= x"AA";
        CIN <= '0';
        wait for CLK_period;
        
        --TEST
        SEL <= "1000";
        A   <= x"AA";
        B   <= x"55";
        CIN <= '0';
        wait for CLK_period;
        
        --LSL
        SEL <= "1001";
        A   <= x"01";
        B   <= x"12";
        CIN <= '1';
        wait for CLK_period;
        CIN <= '0';
        wait for CLK_period;
        
        --LSR
        SEL <= "1010";
        A   <= x"81";
        B   <= x"33";
        CIN <= '0';
        wait for CLK_period;
        CIN <= '1';
        wait for CLK_period;
        
        --ROL
        SEL <= "1011";
        A   <= x"01";
        B   <= x"AB";
        CIN <= '1';
        wait for CLK_period;
        CIN <= '0';
        wait for CLK_period;
        
        --ROR
        SEL <= "1100";
        A   <= x"81";
        B   <= x"3C";
        CIN <= '0';
        wait for CLK_period;
        CIN <= '1';
        wait for CLK_period;
        
        --ASR
        SEL <= "1101";
        A   <= x"81";
        B   <= x"81";
        CIN <= '0';
        wait for CLK_period;
        CIN <= '1';
        wait for CLK_period;
        
        --MOV
        SEL <= "1110";
        A   <= x"50";
        B   <= x"30";
        CIN <= '0';
        wait for CLK_period;
        CIN <= '1';
        wait for CLK_period;
        
        wait;
    end process;
end ALU_TB_Behavioral;
-------------------------------------------------------------------------------------------------------------------
-- End of code.
-------------------------------------------------------------------------------------------------------------------