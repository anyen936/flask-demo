from flask import Flask
from datetime import datetime

#print(_name_)'
app = Flask(__name__)
books={1:"Python book",2:"Java book",3:"Flask book"}
@app.route('/sum/x=<x>&y=<y>')
def my_sum(x,y):
    return f'{x},{y}'


@app.route('/book/<int:id>')
def show_book(id):
     #輸出有書 <h1>第一本書: xxx</h1>
     if id not in books:
        return f"<h2 style = 'color:red'> 無此編號:{id} </h2>"
    return f"<h1>地{id}本書:{books[id]}</h1>"
  #無此編號
    # return books[id]
@app.route ("/books")
def show_books():
    return books[id]

@app.route("/")
def index():
    today = datatime.now()
    print(today)
    return f"<h1> Hello Flask !<br>{today}</h1>"


app.run(debug=True)