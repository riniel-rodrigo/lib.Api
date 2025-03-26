from flask import Flask
from models import init_db
from routes import books_bp
from flask_cors import CORS

# cria a aplicação Flask
app = Flask(__name__)
CORS(app)

# inicializa o banco de dadospip freeze > requirements.txt
init_db()

# registra o blueprint das rotas
app.register_blueprint(books_bp)

# inicia o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
