from service.check_parameter import *
import unittest
from mockito import when, mock


class TestCheckParameterForSubmitList(unittest.TestCase):

    def test_check_hour(self):
        check = CheckParameter()
        self.assertTrue(check.valid_hour('12:00'))

    def test_check_hour_bad_minutes(self):
        check = CheckParameter()
        self.assertFalse(check.valid_hour('12:60'))

    def test_check_bad_hour(self):
        check = CheckParameter()
        self.assertFalse(check.valid_hour('24:00'))

class TestCheckNameListToAddList(unittest.TestCase):

    def test_check_hour(self):
        check = CheckParameter()
        self.assertTrue(check.valid_name_list('name1'))

    def test_check_hour_bad_minutes(self):
        check = CheckParameter()
        self.assertFalse(check.valid_name_list('$ezrezi=<'))

    def test_check_bad_hour(self):
        check = CheckParameter()
        self.assertFalse(check.valid_name_list('<script type="javascript">alert("ok")</script>'))