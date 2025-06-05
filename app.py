
#App.py = Arquivo principal que une tudo

#carregando dependencias necessarias
from flask import Flask, render_template
from livereload import Server


app = Flask(__name__)


#criando caminhos que app direciona
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/rich')
def rich_page():
    return render_template('rich.html') 

@app.route('/landing')
def landing_page():
    return render_template('landing.html') 

if __name__ == '__main__':
    app.run(debug=True)
