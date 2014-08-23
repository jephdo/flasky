# import os

# from flask import Flask
# from flask.ext.script import Manager, Shell
# from flask.ext.bootstrap import Bootstrap
# from flask.ext.moment import Moment

# from flask.ext.sqlalchemy import SQLAlchemy
# from flask.ext.migrate import Migrate, MigrateCommand
# from flask.ext.mail import Mail, Message



# basedir = os.path.abspath(os.path.dirname(__file__))

# app = Flask(__name__)
# app.config['DEBUG'] = True
# app.config['SECRET_KEY'] = 'secret key'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
#     os.path.join(basedir, 'data.sqlite')
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
# app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
# app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN')
# app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
# app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <flasky@example.com>'


# manager = Manager(app)
# bootstrap = Bootstrap(app)
# moment = Moment(app)
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
# manager.add_command('db', MigrateCommand)
# mail = Mail(app)













