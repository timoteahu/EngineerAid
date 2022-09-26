from flask import Flask, render_template, session, redirect, url_for, request
import os

app = Flask('app')

@app.route('/')
def index():
    return render_template("/index.html")
