from flask import Flask
from flask import render_template
import socket #this will be a BIG part of this project
#PUT ALL SERVER CODE HERE:






app=Flask(__name__)
@app.route('/')
def mainpage():
    return render_template("main.html")#uses our html file 

if __name__=='__main__':
  app.run()#runs the website when the file is ran
