from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def home():
    try:

        response = requests.get('http://service-a:3000/users')
        users = response.json()
        
        html_output = "<h1>Relatório de Usuários (Service B)</h1>"
        html_output += "<p>Dados obtidos do <strong>Service A</strong>:</p><ul>"
        
        for user in users:
            html_output += f"<li><strong>{user['name']}</strong> ({user['role']}) - Ativo desde {user['since']}</li>"
        
        html_output += "</ul>"
        return html_output
        
    except Exception as e:
        return f"<h1>Erro</h1><p>Não foi possível conectar ao Service A.</p><p>Detalhe: {e}</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)