# -*- coding:utf-8 -*-

def reverse(a_str):
    """Recursive function to reverse a string."""
    print "Got as an argument:", a_str
    # base case
    if len(a_str) == 1:
        print 'Base case!'
        return a_str
    # recursive step
    else:
        new_string = reverse(a_str[1:]) + a_str[0]
        print "Reaseembling %s and %s into %s" % \
              (a_str[1:], a_str[0], new_string)
        return new_string
    
if __name__ == '__main__':
    the_string = raw_input("What string: ")
    print
    result = reverse(the_string)
    print "\nThe reverse of %s is %s\n" % (the_string, result)
