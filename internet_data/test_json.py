'''test json module, python standard library'''
import os
import unittest
import json


class TestJson(unittest.TestCase):
    """
    test json module
    """

    def test_json_dumps(self):
        '''json dumps object -> string'''
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

    def test_json_dumpload(self):
        '''dump and load json object from file'''
        d1 = {'key': 'value'}
        file_name = 'myfile.json'
        with open(file_name, 'w', encoding='utf8') as json_file:
            json.dump(d1, json_file)
        with open(file_name, 'r') as read_content:
            self.assertEqual("{'key': 'value'}", str(json.load(read_content)))
        os.remove(file_name)
