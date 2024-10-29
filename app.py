from flask import Flask, render_template

app = Flask(__name__)

# Route pour la page d'accueil
@app.route('/')
def index():
    return render_template('index.html')

# Ajoute cette route si elle manque
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

if __name__ == '__main__':
    app.run(debug=True)
