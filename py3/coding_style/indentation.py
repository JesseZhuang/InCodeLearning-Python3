# google used to indent 2 spaces, mixed indentation is fine in same file
# PEP 8 recommends 4 spaces
# https://www.reddit.com/r/learnpython/comments/1xfoxz/pep_indentation_using_4_spaces_vs_googles_2_spaces/
if 1 + 1 == 2:
  print("hello with 2 spaces indentation")
#    print("hello with 4 spaces same block") not ok IndentationError

if 1 + 1 == 2:
    print("hello with 4 spaces indentation")
