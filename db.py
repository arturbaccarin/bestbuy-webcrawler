import sqlite3

def config_db():
    return sqlite3.connect("best_buy_prods.db")


def create_table() -> None:
    con = config_db()
    cur = con.cursor()
    cur.execute('DROP TABLE IF EXISTS products;')

    sql = '''
        CREATE TABLE products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            sku TEXT NOT NULL,
            name TEXT,
            description TEXT,
            images TEXT
        );
    '''
    cur.execute(sql)
    con.commit()

def insert_values(product: dict[str, str]):
    con = config_db()
    cur = con.cursor()
    sql ='''
        INSERT INTO products (url, sku, name, description, images)
        VALUES (?, ?, ?, ?, ?)
    '''
    cur.execute(sql, (
        product['url'],
        product['sku'],
        product['name'],
        product['description'],
        product['images']
    ))
    con.commit()


def select_values() -> list[list[str]]:
    con = config_db()
    cur = con.cursor()
    res = cur.execute('SELECT * FROM products')
    return (res.fetchall())
