

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity PC_sim is
end PC_sim;

architecture PCsim_Behavioral of PC_sim is
    component PC is
        Port ( CLK      : in STD_LOGIC;
               RST      : in STD_LOGIC;                                     -- active high
               LD, INC  : in STD_LOGIC;                                     -- active high
               DIN      : in STD_LOGIC_VECTOR(9 downto 0);
               PC_COUNT : out STD_LOGIC_VECTOR(9 downto 0) := "0000000001");
    end component;
    
    signal CLK          : STD_LOGIC := '0';
    constant CLK_period : time := 10 ns;
    
    signal RST          : STD_LOGIC := '1';
    signal LD, INC      : STD_LOGIC;
    signal DIN          : STD_LOGIC_VECTOR(9 downto 0);
    signal PC_COUNT     : STD_LOGIC_VECTOR(9 downto 0) := "0000000001";

begin
	-- Map the UUT's ports to the signals
    uut: PC PORT MAP (
        RST => RST,
        INC => INC,
        LD => LD,
        DIN => DIN,
        CLK => CLK,
        PC_COUNT => PC_COUNT
    );

    CLK_process : process
    begin
        CLK <= '0';
        wait for CLK_period/2;
        CLK <= '1'; 
        wait for CLK_period/2;
    end process;

    pcsim_proc: process
    begin
        wait for 10 ns;
        
        RST <= '0';
        wait for 10 ns;
        
        DIN <= "0000000111"; --0x07
        wait for 10ns;
        
        LD <= '1';
        INC <= '0';
        wait for 10ns;
        
        INC <= '1';
        wait for 10ns;
        
        LD <= '0';
        DIN <= "0000001111"; --0x0F
        wait for 30ns;
        
        RST <= '1';
        wait for 10ns;
        
        INC <= '0';
        
        wait;
    end process;
end PCsim_Behavioral;
