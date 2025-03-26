from flask import Flask
from models import init_db
from routes import books_bp
from flask_cors import CORS

# Cria a aplicação Flask
app = Flask(__name__)
CORS(app)

# Inicializa o banco de dados pip freeze > requirements.txt
init_db()

# Registra o blueprint das rotas
app.register_blueprint(books_bp)

# Inicia o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
