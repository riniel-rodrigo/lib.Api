from flask import Blueprint, request, jsonify
import sqlite3

# blueprint para organizar as rotas
books_bp = Blueprint('books', __name__)


@books_bp.route('/')
def home_page():
    """Rota para página inicial"""
    return '<h2>Home Page Flask</h2>'


@books_bp.route('/donate', methods=['POST'])
def donate():
    """Rota para cadastrar livro"""
    data = request.get_json()

    title = data.get('title')
    category = data.get('category')
    author = data.get('author')
    img = data.get('img')

    if not all([title, category, author, img]):
        return jsonify({'erro': 'Todos os campos são obrigatórios'}), 400

    with sqlite3.connect('database.db') as conn:
        conn.execute(f""" INSERT INTO books (title, category, author, img)
                     VALUES (?,?,?,?) 
                     """, (title, category, author, img))

        conn.commit()

        return jsonify({"mensagem": "Livro cadastrado com sucesso"}), 201


@books_bp.route("/books", methods=["GET"])
def list_books():
    """Rota para listar livros cadastrados"""
    with sqlite3.connect("database.db") as conn:
        books = conn.execute("SELECT * FROM books").fetchall()

    formatted_books = []

    for book in books:
        dict_books = {
            "id": book[0],
            "title": book[1],
            "category": book[2],
            "author": book[3],
            "img": book[4]
        }
        formatted_books.append(dict_books)

    return jsonify(formatted_books)