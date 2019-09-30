from flask import Flask
app = Flask(__name__)

# Routing is how we will set up the pages, we basically fire off this app as 
#  things come in
@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()