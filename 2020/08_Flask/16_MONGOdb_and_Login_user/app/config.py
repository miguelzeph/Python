from app import app, mongo#, login_manager
import os

#app.config['MONGO_URI'] = 'mongodb://mydb'

# Local
#app.config['SECRET_KEY'] = "mysecretkey"
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# Heroku
#app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY") 
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL") 



#login_manager.login_view='login'# nome VIEW FUNCTION
#login_manager.login_message_category='info' #Bootstrap, ex: alert, success...