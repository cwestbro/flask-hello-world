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

@app.route("/db_create")
def db_create():
    conn = psycopg2.connect("postgresql://cwestbro_render_db_user:Ntm8A5ZPFbbsqbzNMTFyOaxRYBcoONFc@dpg-d9ijv6cm0tmc73cu4030-a/cwestbro_render_db")
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Basketball(
    First varchar(255),
    Last varchar(255),
    City varchar(255),
    Name varchar(255),
    Number int
    );
    """)
    conn.commit()
    conn.close()
    return "Basketball table created"

@app.route("/db_insert")
def db_insert():
    conn = psycopg2.connect("postgresql://cwestbro_render_db_user:Ntm8A5ZPFbbsqbzNMTFyOaxRYBcoONFc@dpg-d9ijv6cm0tmc73cu4030-a/cwestbro_render_db")
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO Basketball (First, Last, City, Name, Number) VALUES
    ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
    ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
    ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
    ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    """)
    conn.commit()
    conn.close()
    return "Basketball table successfully filled"

@app.route("/db_select")
def db_select():
    conn = psycopg2.connect("postgresql://cwestbro_render_db_user:Ntm8A5ZPFbbsqbzNMTFyOaxRYBcoONFc@dpg-d9ijv6cm0tmc73cu4030-a/cwestbro_render_db")
    cur = conn.cursor()
    cur.execute("""
    SELECT * FROM Basketball;
    """)
    records = cur.fetchall()
    conn.close()
    response_string = ""
    response_string += "<table>"
    for player in records:
        response_string += "<tr>"
        for info in player:
            response_string += "<td>{}</td>".format(info)
        response_string += "</tr>"
    response_string += "</table>"
    return response_string

@app.route("/db_drop")
def db_drop():
    conn = psycopg2.connect("postgresql://cwestbro_render_db_user:Ntm8A5ZPFbbsqbzNMTFyOaxRYBcoONFc@dpg-d9ijv6cm0tmc73cu4030-a/cwestbro_render_db")
    cur = conn.cursor()
    cur.execute("""
    DROP TABLE Basketball;
    """)
    conn.commit()
    conn.close()
    return "Basketball table successfully dropped"

