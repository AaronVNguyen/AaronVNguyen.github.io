from sys import *
from blur_commandline import *
from blur_file_funcs import *
			
def main(argv):
	blur = check_initial_conditions(argv)
	infile = in_file(argv)
	write_new_image(infile, int(blur))

if __name__ == '__main__':
	main(argv)
