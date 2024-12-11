"""salesforce hackerrank"""

import re

LOG = ("""
unicomp6.unicomp.net - - [01/Jul/1995:00:00:06 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985
burger.letters.com - - [01/Jul/1995:00:00:11 -0400] "GET /shuttle/countdown/liftoff.html HTTP/1.0" 304 0
burger.letters.com - - [01/Jul/1995:00:00:12 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 304 0
burger.letters.com - - [01/Jul/1995:00:00:12 -0400] "GET /shuttle/countdown/video/livevideo.GIF HTTP/1.0" 200 0
d104.aa.net - - [01/Jul/1995:00:00:13 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985
unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /shuttle/countdown/count.gif HTTP/1.0" 200 40310
unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 200 786
unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /images/KSC-logosmall.gif HTTP/1.0" 200 1204
d104. aa.net - - [01/Jul/1995:00:00:15 -0400] "GET /shuttle/countdown/count.gif HTTP/1.0" 200 40310
d104. aa.net - - [01/Jul/1995:00:00:15 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 200
d104. aa.net - - [01/Jul/1995:00:00:15 -0400] "POST /images/NASA-logosmall.gif HTTP/1.0" 200
""")


# https://stackoverflow.com/questions/40894264/when-are-files-too-large-to-be-read-as-strings-in-python
def unique_gif(lines: str) -> set[str]:
    p = r"GET .*/(.*.gif).*200"
    res = re.findall(p, lines, flags=re.IGNORECASE)
    print(res)
    return set(res)


def get_gif_from_log_file(fn: str):
    lines = set()
    with open(fn, "r") as f:
        lines.update(unique_gif(f.read()))
    with open(f'gifs_fn', "w") as f:
        f.write(f'l\n')


if __name__ == "__main__":
    for l in unique_gif(LOG):
        print(l)

# for file processing, see file_processing.py
