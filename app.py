from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>¡Hola Juan Camilo!</h1><p>Flask está funcionando sin validaciones.</p>"

if __name__ == '__main__':
    app.run(debug=True)
