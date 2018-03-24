from flask import Flask

app = Flask(__name__)


@app.route('/cfgbooks/')
def content():
    return render_template('homePage.html')


@app.route('/cfgbooks/search/')
def results():
    return render_template('searchResults.html')

@app.route('/cfgbooks/search/<book_page>/')
def book(book_page):
    return render_template('bookDetails.html')

app.run(debug=True)