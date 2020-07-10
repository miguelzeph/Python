from app import app, mongo

from app.views import *

if __name__ == '__main__':
    app.run(debug=True)