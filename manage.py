from app import create_app,db
from flask_script import Manager,Server
from app.models import User, Track, Notes, FinanceLiteracy #importing User class from models.py
from flask_migrate import Migrate, MigrateCommand

#creating app instance

app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)

#Initialize the Migrate class
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
#use shell decorator to create shell context and function for passing properties into shell

@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Track= Track, FinanceLiteracy = FinanceLiteracy, Notes = Notes)
    pass

if __name__ == '__main__':
    manager.run()
