import sys
sys.dont_write_bytecode = True
from core import app
import datetime
import json
from flask import flash, render_template, redirect, request, url_for, g, session, jsonify, Response
from flask.ext.login import current_user, login_user, login_required
import requests as res


@app.route('/')
def home():
    return render_template("home/index.html", title="Welcome")
