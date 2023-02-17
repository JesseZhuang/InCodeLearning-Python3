'''strings'''

import os
import platform
import unittest


class TestString(unittest.TestCase):
    '''python strings'''

    def test_raw_string(self):
        '''raw string, no escape'''
        print(r'C:\path\name')  # run this file or debug button in test explorer in vs code
        # raw string cannot end with back slash, e.g., r'C:\name\'
        self.assertEqual(r'C:\path\name', 'C:\\path\\name')
        path = os.path.join(r'C:\this\will\work', '')
        if platform.uname()[0] == 'Darwin':
            self.assertEqual('C:\\this\\will\\work/', path)

    def test_multi_line(self):
        '''multiline string'''
        print(  # back slash in doc string omits new line
            '''
        usage: thingy [options]
            -h\
            display help message
            -H hostname     hostname to connect to
        ''')
        ms1 = 'multi-lines\nstring\n1\n'
        self.assertEqual(  # ugly: identation will be considered as white spaces
            ms1,
            '''\
multi-lines
string
1
'''
        )
        ms2 = ('multi-lines\n'
               'string\n'
               '1\n')
        self.assertEqual(ms1, ms2)

    def test_immutable(self):
        '''
        python strings are immutable
        no char type in python, see bytes type
        '''
        with self.assertRaises(TypeError):
            'word'[0] = 'c'

    def test_fstring_format1(self):
        '''fsstring interpolation, digit format'''
        price = 1.0
        self.assertEqual(f'{0.7*price:.2f}', '0.70')


if __name__ == '__main__':
    unittest.main()
