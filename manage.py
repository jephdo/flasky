#!/usr/bin/env python
import os

from flask.ext.script import Manager, Shell
from flask.ext.migrate import MigrateCommand

from flasky import create_app, db
from flasky.models import User, Role, Post

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role, Post=Post)

# register the application and database instances and models so that they are
# automatically imported into the shell
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)

@manager.command
def test():
    """Discover and run all unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.command
def deploy():
    from flask.ext.migrate import upgrade

    # migrate database to latest revision
    upgrade()

    Role.insert_roles()
    User.add_self_follows()


if __name__ == '__main__':
    manager.run()
