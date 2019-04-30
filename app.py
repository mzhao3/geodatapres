# Maggie Zhao
# SoftDev1 pd7
# K
# 2018-##-##


from flask import Flask,render_template, request, session, url_for, redirect, flash

import os
app = Flask(__name__) #create instance of class flask

# app.secret_key = os.urandom(32)


@app.route("/")
def hello_world():
    return render_template("index.html")




if __name__ == "__main__":
    app.debug = True
    app.run()
