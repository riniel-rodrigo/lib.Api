from flask import Flask
from models import init_db
from routes import books_bp

# Cria a aplicação Flask
app = Flask(__name__)

# Inicializa o banco de dados
init_db()

# Registra o blueprint das rotas
app.register_blueprint(books_bp)

# Inicia o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
