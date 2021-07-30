from flask import Flask, request
from tools import *
app = Flask(__name__)

@app.route("/scrap")
def do_get():
    return build_scrap_document(request.args.get("url"))