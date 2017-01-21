
----------------------------------------------------------------------------------


library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;


entity SP is
  port (RST,CLK,LD,INCR,DECR : in std_logic;
        DATA_IN              : in std_logic_vector (7 downto 0);
        DATA_OUT             : out std_logic_vector (7 downto 0));
end SP;

architecture my_SP of SP is
   signal d_signal : std_logic_vector(7 downto 0);
begin
   process (CLK, RST)
   begin
        if (RST = '1') then
            d_signal <= (others => '0'); -- clear
        elsif (rising_edge(CLK)) then
            if (LD = '1') then d_signal <= DATA_IN; -- load
            else
              if (INCR = '1') then d_signal <= d_signal + 1; -- incr
              elsif (DECR = '1') then d_signal <= d_signal - 1; -- decr
              end if;
            end if;
        end if;
    end process;
    DATA_OUT <= d_signal;
end my_SP;