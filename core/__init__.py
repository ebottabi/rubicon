import sys as s

s.dont_write_bytecode = True
import urllib
import os
from flask import Flask
from tornado.options import define, options
from flask.ext.assets import Environment, Bundle
from flask.ext.bcrypt import Bcrypt
from flask.ext.mongoengine import MongoEngine, MongoEngineSessionInterface
from flask.ext.login import LoginManager
from flask_wtf.csrf import CsrfProtect
from flask.ext.cache import Cache
import memcache
from core.utils.libsmq import *
from mongoengine.queryset import Q
import datetime
from hashlib import md5
import pytz

gm_client = JSONGearmanClient(['localhost:4730'])

app = Flask(__name__)

cache = Cache(app, config={'CACHE_TYPE': 'memcached'})

csrf = CsrfProtect()


app.debug = True
app.config["MONGODB_SETTINGS"] = {'DB': "rubicon"}
app.config["SECRET_KEY"] = "t/eSb1zxF6fK2B/JNc0X2w=="
app.config['UPLOAD_FOLDER'] = '/opt/rubicon/csv_data'
app.config['UPLOAD_DATASETS'] = '/opt/rubicon/datasets'
app.config['ALLOWED_NUMBERS_EXTENSIONS'] = set(['csv'])
app.config['WTF_CSRF_CHECK_DEFAULT'] = False
app.config['MODELS_PATH'] = '/opt/rubicon/models'

db = MongoEngine(app)
app.session_interface = MongoEngineSessionInterface(db)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = urllib.quote("/account/login")  # to handle auth urls


# import models
from core.models.model import *

# import controllers
from core.controllers.home import *
