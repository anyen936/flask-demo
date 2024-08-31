from flask import Flask ,render_template
from datetime import datetime
from scrape import scrap_stocks
#print(_name_)'
app = Flask(__name__)
books={1:"Python book",2:"Java book",3:"Flask book"}
books={
1:{
"name":"Python book",
"price":299,
"image_url":"https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/CN1/136/11/CN11361197.jpg&v=58096f9ck&w=348&h=348"
},

2:{

"name":"Java book",
"price":399,
"image_url":"https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/087/31/0010873110.jpg&v=5f7c475bk&w=348&h=348"
},

3:{
"name":"C# book",
"price":499,
"image_url":"https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/036/04/0010360466.jpg&v=62d695bak&w=348&h=348"
},
}
@app.route('/stocks')
def get_stock():
    data = scrape_stocks()
    for data in datas:
        print(data[0],data[1])
    return render_template('stocks.html',datas=datas)

@app.route('/bmi/name=<name>&height=<h>&weight=<w>')
def x_bmiI(name,h,w):
    pass
   
    # try:
    #     bmi=eval((height)/eval(weight)/100)**2,2)
    #     return f"<h1><span style =' color :bule>{name}}</h1>"

@app.route('/sum/x=<x>&y=<y>')
def my_sum(x,y):
    # 參數不正鴂 請輸出參數錯誤 (try except)
    try:
        total = eval(x) + eval(y)
        return f'<h1>{x}+{y}={total}</h1>'
    except Exception as e:
        print(e)

    return '<h2>參數不正鴂 請輸出參數錯誤</h2>'
    

        # return f'{x},{y}'


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
    # return books[id]
    for key in books:
        print(books[key])
    return render_template("index.html",books = books)

@app.route("/")
def index():
    today = datetime.now()
    print(today)
    
    # return f"<h1> Hello Flask !<br>{today}</h1>"
    name = "jerry"
    return render_template("index.html",date=today, name=name)
app.run(debug=True)