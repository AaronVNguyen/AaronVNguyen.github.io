# also checks default value
def check_initial_conditions(argv):
        if len(argv) < 2:
                print "Usage: python blur.py <input file> [neighbor reach]"
                exit()
        elif len(argv) == 2:
                return 4
        else:
                return argv[2]
def in_file(argv):
        try:
                f = open(argv[1], 'r')
                return f
        except:
                print 'Could not open "' + argv[1] + '" for reading.'
                exit()

