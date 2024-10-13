"""test json module, python standard library"""
import json
import os
import unittest
from io import StringIO


class TestJson(unittest.TestCase):
    """
    test json module
    """

    def test_json_dumps(self):
        """json dumps object -> string"""
        json_array_object = ['foo', {'bar': ('baz', None, 1.0)}]
        self.assertEqual(json.dumps(json_array_object),
                         '["foo", {"bar": ["baz", null, 1.0]}]')
        self.assertEqual(json.dumps(json_array_object, indent=2),
                         ('[\n'
                          '  "foo",\n'
                          '  {\n'
                          '    "bar": [\n'
                          '      "baz",\n'
                          '      null,\n'
                          '      1.0\n'
                          '    ]\n'
                          '  }\n'
                          ']')
                         )

    def test_json_dump_load(self):
        """dump and load json object from file"""
        d1 = {'key': 'value'}
        file_name = 'myfile.json'
        with open(file_name, 'w', encoding='utf8') as json_file:
            json.dump(d1, json_file)
        with open(file_name, 'r') as read_content:
            d2 = json.load(read_content)
            self.assertEqual("{'key': 'value'}", str(d2))
            self.assertEqual(d1, d2)
        os.remove(file_name)  # delete file

    def test_json_stringio(self):
        """communicate via string io"""
        io = StringIO()
        string_o = '["dump", "to string io"]'
        obj = ['dump', 'to string io']
        json.dump(obj, io)
        self.assertEqual(string_o, io.getvalue())
        io = StringIO(string_o)
        self.assertEqual(obj, json.load(io))
