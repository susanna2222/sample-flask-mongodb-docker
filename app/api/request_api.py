from flask import jsonify, abort, request, Blueprint
from app.api import mongoDB
import json

REQUEST_API = Blueprint('request_api', __name__)

def get_blueprint():
    """Return the blueprint for the main app module"""
    return REQUEST_API

items = {
    0 : {"name": "First item"}
}

@REQUEST_API.route('/items', methods=['GET'])
def search() -> list:
    return items

@REQUEST_API.route('/users/getall', methods=['GET'])
def user_getall():

    col = mongoDB["users"]
    myquery = {}
    users = col.find(myquery)

    entries = []

    for row in users:
        entries.append({'user': row['user']})

    return json.dumps(entries)

@REQUEST_API.route('/workitem/getall', methods=['GET'])
def workitem_getall():

    col = mongoDB["workitems"]
    myquery = {"user.email":"liling.chen@ccbji.co.jp"}
    workitems = col.find(myquery)

    entries = []

    for row in workitems:
        entries.append({'title': row['title']})

    return json.dumps(entries)