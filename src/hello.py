from flask import Flask, redirect, request

meu_web_app = Flask(__name__)

@meu_web_app.route('/', methods=['GET'])
def index():
    return 'Test TDD'

