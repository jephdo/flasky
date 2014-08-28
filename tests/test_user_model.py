import unittest

from flasky import db
from flasky.models import User, Permission, Role, AnonymousUser

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

    def test_password_salts_are_random(self):
        user1 = User(password="cat")
        user2 = User(password="cat")

        self.assertFalse(user1.password_hash == user2.password_hash)

    def test_valid_reset_token(self):
        u = User(password='cat')
        db.session.add(u)
        db.session.commit()
        token = u.generate_reset_token()
        self.assertTrue(u.reset_password(token, 'dog'))
        self.assertTrue(u.verify_password('dog'))

    def test_invalid_reset_token(self):
        u1 = User(password='cat')
        u2 = User(password='dog')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        token = u1.generate_reset_token()
        self.assertFalse(u2.reset_password(token, 'horse'))
        self.assertTrue(u2.verify_password('dog'))

    def test_roles_and_permissions(self):
        Role.insert_roles()
        u = User(email='asdfxdfx@example12.com', password='cat')
        self.assertTrue(u.can(Permission.WRITE_ARTICLES))
        self.assertFalse(u.can(Permission.MODERATE_COMMENTS))

    def test_anonymous_user(self):
        u = AnonymousUser()
        self.assertFalse(u.can(Permission.FOLLOW))
