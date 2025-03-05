from flask import Flask
import threading
import time
import requests

app = Flask(__name__)

urls = ['https://recipes-maker.onrender.com/', 'https://rpgplayer.onrender.com/','https://threedtudo.onrender.com/']

def manter_cu_grosso():
    while True:
        try:
            for url in urls:
                response = requests.get(url)  # Corrigida a indentação aqui
                if response.status_code == 200:
                    print("Requisição bem-sucedida!")
                    print("Por enquanto tudo certo aqui!, apenas um cara tranquilo")
                else:
                    print(f"Falha na requisição. Status code: {response.status_code}")
        except Exception as e:
            print(f"Erro na requisição: {e}")
        time.sleep(60)

# Iniciar o script em uma thread separada
threading.Thread(target=manter_cu_grosso, daemon=True).start()

@app.route('/')
def home():
    return "Xaublin!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
