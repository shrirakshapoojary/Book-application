from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Temporary book list (no database yet)
books = []

@app.route('/')
def home():
    return render_template('index.html', books=books)

@app.route('/add', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']

    books.append({
        'title': title,
        'author': author
    })

    return redirect('/')

@app.route('/delete/<int:index>')
def delete_book(index):
    if 0 <= index < len(books):
        books.pop(index)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)