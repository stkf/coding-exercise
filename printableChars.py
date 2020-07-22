import sys
import string

printable = set(ord(c) for c in string.printable)

def strings(filename, min=4):
    with open(filename, 'rb') as f:
        result = bytearray()
        for c in f.read():
            if ord(c) in printable:
                result.append(ord(c))
                continue
            if len(result) >= min:
                print result.decode('ASCII')
            result = bytearray()
        if len(result):
            print result.decode('ASCII')

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print "Usage printableChar <filename>"
        exit(1)

    strings(sys.argv[1])
