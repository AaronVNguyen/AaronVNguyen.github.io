library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity SCR_tb is
end SCR_tb;

architecture SCR_tb_Behavioral of SCR_tb is
    component SCR is
        Port( CLK       : in STD_LOGIC;
              WE        : in STD_lOGIC;
              ADDR      : in STD_LOGIC_VECTOR(7 downto 0);
              DATA_IN   : in STD_LOGIC_VECTOR(9 downto 0);
              DATA_OUT  : out STD_LOGIC_VECTOR(9 downto 0) );
    end component;
    
    -- Inputs
    signal CLK : STD_LOGIC := '0';
    signal WE : STD_LOGIC := '0';
    signal ADDR : STD_LOGIC_VECTOR(7 downto 0) := (others => '0');
    signal DATA_IN : STD_LOGIC_VECTOR(9 downto 0);
    
    -- Outputs
    signal DATA_OUT : STD_LOGIC_VECTOR(9 downto 0);
    
    -- Clock Period Definition
    constant CLK_period : time := 10 ns;
begin
    -- Instantiate the UUT.
    uut: SCR PORT MAP (
        CLK => CLK,
        WE => WE,
        ADDR => ADDR,
        DATA_IN => DATA_IN,
        DATA_OUT => DATA_OUT
    );
    
    -- Clock process
    CLK_process: process
    begin
        CLK <= '0';
        wait for CLK_period/2;
        CLK <= '1';
        wait for CLK_period/2;
    end process;
    
    -- Stimulus
    stim_proc: process
    variable I : integer range 0 to 255 := 0;
    begin
    
        -- write to every location in memory
        WE <= '1';
        ADDR <= x"00";
        while (I < 255) loop
            ADDR <= ADDR + 1;
            I := I + 1;
            DATA_IN <= "00" & (ADDR(7 downto 0) + 1);
            wait for 10ns;
        end loop;
        
        -- read from every location in memory
        WE <= '0';
        I := 0;
        while (I < 255) loop
            ADDR <= ADDR + 1;
            I := I + 1;
            wait for 10 ns;
        end loop;
        
    end process;
end SCR_tb_Behavioral;