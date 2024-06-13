import psycopg2
from templates.verification_email import *
from .db_pool import get_connection, put_connection, close_all_connections
from ..user import send_email


def insert_user_data(userid, username, email, firstname, lastname, dob, gender, hash_p, salt):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        insert_query = """
            INSERT INTO 
            users(userid, username, email, firstname, lastname, dob, gender)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(insert_query, (userid, username, email, firstname, lastname, dob, gender))
        conn.commit()

        print("User Data inserted successfully")

        insert_login_data(userid, hash_p, salt, conn, cursor)

    except (Exception, psycopg2.DatabaseError) as error:
        conn.rollback()
        print(f"Error: {error}")


def insert_login_data(userid, hash_p, salt, conn, cursor):
    try:

        insert_query = """
            INSERT INTO 
            login(userid, hash, salt, verified, isactive, isdeleted)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        cursor.execute(insert_query, (userid, hash_p, salt, '0', '0', '0'))
        conn.commit()

        print("Login Data inserted successfully")

    except (Exception, psycopg2.DatabaseError) as error:
        conn.rollback()
        print(f"Error: {error}")


def check_email_duplication(email):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        select_sql = "SELECT COUNT(*) FROM users WHERE email = %s"
        cursor.execute(select_sql, (email,))
        count = cursor.fetchone()[0]
        return count > 0
    
    except Exception as e:
        print(f"Error checking email duplication: {e}")
        return False


def check_username_duplication(username):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        select_sql = "SELECT COUNT(*) FROM users WHERE username = %s"
        cursor.execute(select_sql, (username,))
        count = cursor.fetchone()[0]
        return count > 0
    
    except Exception as e:
        print(f"Error checking username duplication: {e}")
        return False


def update_user_status(user_id):
    update_query = "UPDATE login SET verified = %s, isactive = %s WHERE userid = %s"

    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute(update_query, (True, True, user_id))
        conn.commit()
        return True
    
    except (Exception, psycopg2.DatabaseError) as error:
        conn.rollback()
        print(f"Error: {error}")
        return False