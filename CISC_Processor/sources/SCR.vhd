library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity SCR is
    Port( CLK       : in STD_LOGIC;
          WE        : in STD_lOGIC;
          ADDR      : in STD_LOGIC_VECTOR(7 downto 0);
          DATA_IN   : in STD_LOGIC_VECTOR(9 downto 0);
          DATA_OUT  : out STD_LOGIC_VECTOR(9 downto 0) );
end SCR;

architecture SCR_Behavioral of SCR is
    type ram_type is array (0 to 255) of STD_LOGIC_VECTOR(9 downto 0);
    signal scratch_ram : ram_type := (others => (others => '0'));
begin
    ram_write: process (CLK, WE)
    begin
        if (rising_edge(CLK)) then
            if (WE = '1') then
                scratch_ram(conv_integer(ADDR)) <= DATA_IN;
            end if;
        end if;
    end process ram_write;
    
    DATA_OUT <= scratch_ram(conv_integer(ADDR));

end SCR_Behavioral;
