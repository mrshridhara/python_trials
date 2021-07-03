from datetime import datetime

from flask import Flask

app = Flask(__name__)
current_year = datetime.now().year
