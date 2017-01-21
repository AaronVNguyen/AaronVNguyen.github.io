library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity FLAGS_sim is
--  Port ( );
end FLAGS_sim;

architecture FLAGS_Behavioral of FLAGS_sim is
    component FLAGS is
        Port ( CLK          : in STD_LOGIC;
               CLR, SET, LD : in STD_LOGIC;
               DATA_IN      : in STD_LOGIC;
               DATA_OUT     : out STD_LOGIC );
    end component;
    
    signal CLK          : STD_LOGIC := '0';
    constant CLK_period : time := 10 ns;
    
    signal CLR, SET, LD : STD_LOGIC;
    signal DATA_IN      : STD_LOGIC;
    signal DATA_OUT     : STD_lOGIC;
    
    
begin
	-- Map the UUT's ports to the signals
    uut: FLAGS PORT MAP (
        CLK => CLK,
        LD => LD,
        SET => SET,
        CLR => CLR,
        DATA_IN => DATA_IN,
        DATA_OUT => DATA_OUT
    );

    CLK_process : process
    begin
        CLK <= '0';
        wait for CLK_period/2;
        CLK <= '1'; 
        wait for CLK_period/2;
    end process;
    
    flagsim_proc: process
    begin
        DATA_IN <= '1';
        wait for 10 ns;
        
        LD <= '1';
        wait for 10 ns;
        
        DATA_IN <= '0';
        wait for 10 ns;
         
        SET <= '1';
        wait for 10 ns;
        
        DATA_IN <= '1';
        wait for 10 ns;
        
        CLR <= '1';
        wait for 20 ns;
        
        CLR <= '0';
        wait for 10 ns;
        
        SET <= '0';
        DATA_IN <= '0';
        wait for 10 ns;
        
        LD <= '0';
        wait for 10 ns;
        
        DATA_IN <= '1';
        wait;
    end process;
end FLAGS_Behavioral;
