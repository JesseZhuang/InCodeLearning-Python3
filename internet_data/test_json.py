'''test json module, python standard library'''
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
