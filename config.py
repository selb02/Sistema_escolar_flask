from flask import Flask

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['HOST'] = '127.0.0.1'
app.config['PORT'] = 5000
