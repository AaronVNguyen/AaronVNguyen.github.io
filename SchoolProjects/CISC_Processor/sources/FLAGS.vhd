-- Priority: CLR -> SET -> LD
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity FLAGS is
    Port ( CLK          : in STD_LOGIC;
           CLR, SET, LD : in STD_LOGIC;
           DATA_IN      : in STD_LOGIC;
           DATA_OUT     : out STD_LOGIC );
end FLAGS;

architecture FLAGS_Behavioral of FLAGS is

begin
    flag_proc: process (CLK, LD, SET, CLR, DATA_IN)
    begin
        if (rising_edge(CLK)) then
            if (CLR = '1') then
                DATA_OUT <= '0';
            elsif (SET = '1') then
                DATA_OUT <= '1';
            elsif (LD = '1') then
                DATA_OUT <= DATA_IN;
            end if;
        end if;
    end process;
end FLAGS_Behavioral;
