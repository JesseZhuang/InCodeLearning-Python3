import argparse

# source: https://hg.python.org/cpython/file/3.5/Lib/argparse.py
# https://code.google.com/archive/p/argparse/
# getopt equivalent for C getopt()
# deprecated optparse, argparse based on and similar to optparse

# camel case
parser = argparse.ArgumentParser(description="echo a string, "
                                 "and calculate x to the power of y")

# get -h --help for free

# optional argument to be echoed, pass in as -e ECHO or -e=ECHO
parser.add_argument("-e", "--echo", help="echo the string argument"
                    "passed in here")

# add math pow functionality, positional arguments
parser.add_argument("x", type=int, help="the base")  # default type string
parser.add_argument("y", type=int, help="the exponent")

# optional argument, conflicting options
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="count", default=0)
group.add_argument("-q", "--quiet", action="store_true")

args = parser.parse_args()                   # underscore


if args.echo:
    print("echoing string:", args.echo)

answer = args.x**args.y

# if args.quiet:
if args.verbose >= 2:
    print("running '{}'".format(__file__))
if args.verbose >= 1:
    print("{}^{} == ".format(args.x, args.y), end="")
    # does not start new line, todo add to print format
print(answer)
