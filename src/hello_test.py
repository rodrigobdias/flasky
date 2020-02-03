from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return '<h1>Test TDD</h1>'


def get_format_name(first, last):
    format_name = first + ' ' + last
    return format_name.title()