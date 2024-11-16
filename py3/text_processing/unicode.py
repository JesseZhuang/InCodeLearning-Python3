print(ascii('¢'))  # \xa2 code point U+00A2
# utf-8 code point binary 1100 0010 1010 0010 hex c2 a2 2 bytes
# code point in binary 000 1010 0010 U+00A2, 11 bits
print(ascii('𐍈'))
print(ascii('€'))
# ascii converts to unicode points, not utf-8 representations
# does not start from 0 utf-8 2 bytes U+0080 to U+07FF
