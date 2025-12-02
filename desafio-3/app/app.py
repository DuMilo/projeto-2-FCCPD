import os
import time
from flask import Flask
import redis
import psycopg2

app = Flask(__name__)


REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('POSTGRES_DB', 'meubanco')
DB_USER = os.getenv('POSTGRES_USER', 'user')
DB_PASS = os.getenv('POSTGRES_PASSWORD', 'password')


cache = redis.Redis(host=REDIS_HOST, port=6379)

def get_db_connection():

    retries = 5
    while retries > 0:
        try:
            conn = psycopg2.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASS
            )
            return conn
        except psycopg2.OperationalError:
            retries -= 1
            print("Banco ainda não está pronto... aguardando 2s")
            time.sleep(2)
    return None

@app.route('/')
def index():

    count = cache.incr('hits')
    

    conn = get_db_connection()
    db_status = "Falha ao conectar no Postgres"
    if conn:
        db_status = "Conectado ao Postgres com Sucesso!"
        conn.close()

    return f"""
    <h1>Desafio 3 - Docker Compose</h1>
    <p>Acessos (via Redis): <strong>{count}</strong></p>
    <p>Status do Banco (via Postgres): <strong>{db_status}</strong></p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)