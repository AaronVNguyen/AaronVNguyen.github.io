def check_initial_conditions(argv):
        if len(argv) < 2:
                print "Usage: python puzzle.py <input file>"
                exit()

def in_file(argv):
        try:
                f = open(argv[1], 'r')
                return f
        except:
                print 'Could not open "' + argv[1] + '" for reading.'
                exit()
