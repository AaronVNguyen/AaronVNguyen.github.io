from sys import *
from puzzle_commandline import *
from puzzle_file_funcs import *

def main(argv):
        check_initial_conditions(argv)
        infile = in_file(argv)
        write_new_image(infile)

if __name__ == '__main__':
	main(argv)
