import os
from flask import Flask

app = Flask(__name__)

from app import routes, errors

PORT = os.getenv('PORT', '5000')

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
    app.run(host="0.0.0.0", port=int(PORT))