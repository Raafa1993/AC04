## Rafael Araujo da Silva RA 1901722
## Matheus da Silva Santos RA 1901712

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/inicio')
@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/login')
def inicio_login():
    return render_template('login.html')

## Para rodar o projeto em desenvolvimento

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
