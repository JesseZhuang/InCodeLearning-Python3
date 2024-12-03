from unittest import TestCase

from algorithm.jzstring.ascii_encoded_strings import encode_ascii_string, decode_ascii_string, decode_ascii_string_dp

cases = [
    ('hello world', '00180141111191123111801801101401'),
    ('HackerRank', '7010117928411101701997927'),
    ('Go VMWare', '101411797877682311117'),
    ('Truth Always Wins ', '23511011501782351112179911801562340161171141148')
]

cases2 = [
    ('0102101010231414141456102020111101', ['\n\x0bn\x14\x14\x106\x0e\x0e\x0e\r\x14\n\nx\n',
                                            '\n\x0bn\x14\x14\x106\x0e\x0e\x0e\r\x14\ne\x14\n',
                                            '\no\n\x14\x14\x106\x0e\x0e\x0e\r\x14\n\nx\n',
                                            '\no\n\x14\x14\x106\x0e\x0e\x0e\r\x14\ne\x14\n',
                                            'e\x0b\n\x14\x14\x106\x0e\x0e\x0e\r\x14\n\nx\n',
                                            'e\x0b\n\x14\x14\x106\x0e\x0e\x0e\r\x14\ne\x14\n']),
    ('10111', ['\x0be']),
    ('02101', ['\nx', 'e\x14']),  # \x followed by 2 digit hex value 0x14 == 20
    ('21111', ['\x0bp', 'o\x0c']),
    ('0102101', ['\nx\n', 'e\x14\n']),
]


class TestAsciiEncodedString(TestCase):

    def test_encoder(self):
        for s, exp in cases:
            with self.subTest(s=s):
                self.assertEqual(exp, encode_ascii_string(s))

    def test_decoder(self):
        for s, exp in cases:
            with self.subTest(s=s):
                self.assertEqual(s, decode_ascii_string(exp))

    def test_decoder_dp(self):
        for s, exp in cases2:
            with self.subTest(s=s):
                exp.sort()
                res = sorted(decode_ascii_string_dp(s))
                self.assertEqual(exp, res)
