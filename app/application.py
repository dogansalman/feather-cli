import psycopg2
from psycopg2 import sql

def new(username, user_password, dbname, host, port):
    connection = None
    cursor = None
    psql_connection_string = f"host={host} port={port} dbname=postgres user={username}  password={user_password}"
    try:
        connection = psycopg2.connect(psql_connection_string)
        connection.autocommit = True

        print(f"Connected with connection string {psql_connection_string}")
        cursor = connection.cursor()
        cursor.execute(sql.SQL('CREATE DATABASE {};').format(sql.Identifier(dbname)))
        print("created database")


    except (Exception) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
