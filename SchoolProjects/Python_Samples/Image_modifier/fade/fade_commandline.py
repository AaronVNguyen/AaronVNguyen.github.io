def check_initial_conditions(argv):
        if len(argv) < 5:
                print "Usage: python fade.py <input file> <row> <col> <radius>"
                exit()

def in_file(argv):
        try:
                f = open(argv[1], 'r')
                return f
        except:
                print 'Could not open "' + argv[1] + '" for reading.'
                exit()
