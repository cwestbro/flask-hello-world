import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Cameron Westbrook in 3308!'

@app.route("/db_test")
def db_test():
    conn = None
    try:
        conn = psycopg2.connect("postgresql://cwestbro_render_db_user:Ntm8A5ZPFbbsqbzNMTFyOaxRYBcoONFc@dpg-d9ijv6cm0tmc73cu4030-a/cwestbro_render_db")
        return "Database connection successful"
    except Exception as e:
        return f"Database connection failed: {e}"
    finally:
        if conn is not None:
            conn.close()


