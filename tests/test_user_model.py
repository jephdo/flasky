import unittest

from flasky.models import User

class UserModelTestCase(unittest.TestCase):

    def test_password_setter(self):
        user = User(password="cat")
        self.assertTrue(user.password_hash is not None)

    def test_no_password_getter(self):
        user = User(password="cat")

        with self.assertRaises(AttributeError):
            user.password

    def test_password_verification(self):
        user = User(password="cat")
        self.assertTrue(user.verify_password("cat"))
        self.assertFalse(user.verify_password("dog"))

    def  test_password_salts_are_random(self):
        user1 = User(password="cat")
        user2 = User(password="cat")

        self.assertFalse(user1.password_hash == user2.password_hash)
