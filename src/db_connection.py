"""
Purpose:
    Create and test a connection between Python and MySQL.

Flow:
    Python
       ↓
    MySQL Connector
       ↓
    MySQL Server
       ↓
    customer_churn_ml database
"""


# SQLAlchemy is used to create a database engine.
from sqlalchemy import create_engine

def create_engine_connection():
    """
    Create a SQLAlchemy engine for MySQL.

    The engine provides Pandas with a supported
    database connection interface.
    """

    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    database = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")

    # Build the MySQL connection URL.
    connection_url = (
        f"mysql+mysqlconnector://{user}:{password}"
        f"@{host}:{port}/{database}"
    )

    # Create and return the SQLAlchemy engine.
    engine = create_engine(connection_url)

    return engine

# os is used to read environment variables.
import os

# mysql.connector provides the Python-to-MySQL connection.
import mysql.connector

# load_dotenv loads values from our .env file.
from dotenv import load_dotenv


# Load environment variables from the .env file.
load_dotenv()


def create_connection():
    """
    Create a connection to the MySQL database.

    The connection details are read from environment variables
    instead of being hardcoded in the Python source code.
    """

    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    return connection


def main():
    """
    Test the MySQL connection.
    """

    try:
        # Create the database connection.
        connection = create_connection()

        # Check whether the connection was successful.
        if connection.is_connected():

            print("MySQL connection successful!")

            # Get basic information about the database connection.
            database_name = connection.database

            print(f"Connected database: {database_name}")

    except mysql.connector.Error as error:

        # Display the database error if connection fails.
        print(f"MySQL connection failed: {error}")

    finally:

        # Close the connection if it was created.
        if "connection" in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")


# Execute main() only when this file is run directly.
if __name__ == "__main__":
    main()