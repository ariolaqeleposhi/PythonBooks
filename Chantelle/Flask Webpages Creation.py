from flask import Flask

app = Flask(__name__)


@app.route('/cfgbooks/')
def content():
    return 'Home Page'


@app.route('/cfgbooks/search/')
def results():
    return 'Search Results'

@app.route('/cfgbooks/search/<book_page>/')
def book(book_page):
    return book_page

app.run(debug=True)