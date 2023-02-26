from flask import Flask
from .blueprints.link import link

app = Flask(__name__)
app.register_blueprint(link)

if __name__ == "__main__":
    app.run()
