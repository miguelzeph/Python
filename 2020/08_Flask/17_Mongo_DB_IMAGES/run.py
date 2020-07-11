from flask import Flask, request, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb+srv://useradmin:admin@cluster0.7rvyr.gcp.mongodb.net/MEU_DB?retryWrites=true&w=majority"
mongo = PyMongo(app)

@app.route('/')
def index():
    return """
        <form method = "POST" action = "/create" enctype='multipart/form-data'>
        
            Username <input type = "text" name = "username">
            <br>
            <input type = "file" name = "userimage">
            <br>
            <input type = "submit" value = "Submeter">
        </form>
    """
    # Observação: Precisa do "enctype='multipart/form-data'" no Form

@app.route('/create', methods = ['POST','GET'])
def create():
    if 'userimage' in request.files:
        userimage = request.files['userimage']
        mongo.save_file(userimage.filename,userimage)
        
        profiles = mongo.db.profiles # Cria uma nova tabela chamada 'profiles'
        profiles.insert({
            'username': request.form['username'],
            'userimage': userimage.filename
        })# Salva os dados nela
    return "DONE!"

@app.route('/file/<filename>')
def file(filename):
    return mongo.send_file(filename)

@app.route('/profile/<username>')
def profile(username):
    user = mongo.db.profiles.find_one_or_404({'username':username})
    return f'''
        <h1>{username}</h1>
        <img src ="{url_for('file',filename=user['userimage'])}" >
    '''



if __name__ == '__main__':
    app.run(debug=True)