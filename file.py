import psycopg2

def create_connection(dbname):
    conn = None
    try:
        conn = psycopg2.connect(
            dbname=dbname,
            user="postgres",
            password="0000",
            host="localhost",
            port="5432"
        )
        print("Connection established")
        return conn
    except Exception as error:
        print(error)
        return None


def close_connection(conn):
    if conn:
        conn.close()
        print("Connection closed")


def create_table(conn):
    table_1 = """
    CREATE TABLE IF NOT EXISTS airports (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        age INTEGER CHECK (age > 18 AND age < 55) 
    );
    """
    try:
        cursor = conn.cursor()
        cursor.execute(table_1)
        conn.commit()
        print("Table created successfully")
    except Exception as error:
        print(error)

conn = create_connection('airport')
if conn:
    create_table(conn)
    close_connection(conn)

