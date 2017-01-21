library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity PC is
    Port ( CLK      : in STD_LOGIC;
           RST      : in STD_LOGIC;                                     -- active high
           LD, INC  : in STD_LOGIC;                                     -- active high
           DIN      : in STD_LOGIC_VECTOR(9 downto 0);
           PC_COUNT : out STD_LOGIC_VECTOR(9 downto 0) := "0000000001" );
end PC;

architecture PC_Behavioral of PC is

begin
    pc_prog: process (RST, LD, INC, DIN, CLK)
    variable tCount : STD_LOGIC_VECTOR(9 downto 0) := "0000000001";
    begin
        if (RST = '1') then
            tCount := "0000000001";
        elsif(rising_edge(CLK)) then
            if (LD = '1') then
                tCount := DIN;
            elsif (INC = '1') then
                tCount := tCount + 1;
            end if;
        end if;
        PC_COUNT <= tCount;
    end process pc_prog;
    
end PC_Behavioral;
