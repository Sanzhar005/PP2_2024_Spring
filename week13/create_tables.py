import psycopg2

def create_tables():
    """ Create tables in the PostgreSQL database"""
    commands = """
        CREATE TABLE phone_number (
            phone_number_id SERIAL PRIMARY KEY,
            name CHAR NOT NULL,
            surname CHAR NOT NULL,
            number_value VARCHAR(12) NOT NULL
        )
    """
    try:
        # Параметры подключения к базе данных
        db_params = {
            'database': 'postgres',
            'user': 'postgres',
            'password': 'Sancho501553',
        }
        # Подключение к базе данных
        with psycopg2.connect(**db_params) as conn:
            with conn.cursor() as cur:
                # Выполнение SQL-запроса CREATE TABLE
                cur.execute(commands)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_tables()