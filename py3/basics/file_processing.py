import gzip
import sys

# reference https://docs.python.org/3.1/library/io.html#module-interface
# Learning point 1 write text file to create a new file
# Learning point 2 read the entire text file
# Learning point 3 read one line at a time from the text file
# Learning point 4 steam object.close() and with

with open('test.log', mode='w', encoding='utf-8') as a_file:
    a_file.write('test succeeded')

with open('test.log', encoding='utf-8') as a_file:
    print(a_file.read())

# LP 5: write text file to append to file
with open('test.log', mode='a', encoding='utf-8') as a_file:
    a_file.write('\nand again 1\n')
    a_file.write('and again 2\n')
    a_file.write('and again 3\n')
    a_file.write('and again 4\n')
    a_file.write('and again 5\n')
    a_file.write('and again 6\n')

with open('test.log', encoding='utf-8') as a_file:
    print(a_file.read())

# LP 7: read text file one line at a time
line_number = 0
with open('test.log', encoding='utf-8') as a_file:
    for a_line in a_file:
        line_number += 1
        print('{:>4} {}'.format(line_number, a_line.rstrip()))

# LP 8: open return an stream object with many methods
a_file = open('test.log', encoding='utf-8')
print("stream object.name =" + a_file.name)
print("stream object.encoding = " + a_file.encoding)
print("stream object.mode = " + a_file.mode)

# LP9: write zipped files
with gzip.open('out.log.gz', mode='wb') as z_file:
    z_file.write(
        'A nine mile walk is no joke, especially in the rain.'.encode('utf-8'))

# read zipped files
with gzip.open('out.log.gz', mode='rb') as z_file:
    print(z_file.read())


# LP 10: redirect stdout to a file
class RedirectStdoutTo:
    def __init__(self, out_new):
        self.out_new = out_new

    def __enter__(self):
        self.out_old = sys.stdout
        sys.stdout = self.out_new

    def __exit__(self, *args):
        sys.stdout = self.out_old

with open('out.log', mode='w', encoding='utf-8') as a_file:
    with RedirectStdoutTo(a_file):
        print(u'Stdout is redirected to a file, 中文')

# with open('out.log', mode='r') as a_file:
with open('out.log', encoding='utf-8') as a_file:
    print(a_file.read())
