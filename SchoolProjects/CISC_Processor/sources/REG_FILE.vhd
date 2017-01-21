
----------------------------------------------------------------------------------


library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;

entity REG_FILE is
  Port (CLK, WR         : in std_logic;  
        DIN             : in std_logic_vector(7 downto 0);
        ADRX            : in std_logic_vector (12 downto 8);
        ADRY            : in std_logic_vector (7 downto 3);
        DX_OUT, DY_OUT  : out std_logic_vector (7 downto 0));
end REG_FILE;

architecture Behavioral of REG_FILE is

    type reg_type is array (0 to 31) of std_logic_vector (7 downto 0);
    signal gen_reg : reg_type := (others=> (others => '0'));

begin
    reg_write: process (CLK, WR)
    begin
        if (rising_edge(CLK)) then
            if (WR = '1') then 
                gen_reg(conv_integer (ADRX)) <= DIN; 
            end if; 
        end if;
    end process reg_write;
    
    DX_OUT <= gen_reg(conv_integer (ADRX));
    DY_OUT <= gen_reg(conv_integer (ADRY));
end Behavioral;
