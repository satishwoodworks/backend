from db_utils.db_pool import get_connection, put_connection, close_all_connections
import psycopg2
import random
from utils.user import send_email
from templates.email_templates import *


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

        code = random.randint(100000, 999999)

        verification_email_body1 = verification_email_body.replace("XXXXXX", str(code))

        send_email(verification_email_subject, verification_email_body1, sender_email, email, sender_key)

    except (Exception, psycopg2.DatabaseError) as error:
        conn.rollback()
        print(f"Error: {error}")


def insert_login_data(userid, hash_p, salt, conn, cursor):
    try:

        insert_query = """
            INSERT INTO 
            login(userid, hash, salt, verified)
            VALUES (%s, %s, %s, %s)
        """

        cursor.execute(insert_query, (userid, hash_p, salt, '0'))
        conn.commit()

        print("Login Data inserted successfully")

    except (Exception, psycopg2.DatabaseError) as error:
        conn.rollback()
        print(f"Error: {error}")


def update_verification_bit(user_id, cursor, conn):
    update_query = f"Update login set verified = 1 where userid = '{user_id}'"

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(update_query)
        conn.commit()
        return True
    
    except (Exception, psycopg2.DatabaseError) as error:
        conn.rollback() 
        return False