import psycopg2

from .db_pool import get_connection


def get_user_data(email_or_username, hash_password):
    query = """
        SELECT
            u.*,
            l.*,
            p.*
        FROM users u
        LEFT JOIN login l ON u.userid = l.userid
        LEFT JOIN user_profiles p ON u.userid = p.userid
        WHERE u.email = %s OR u.username = %s
    """

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(query, (email_or_username, email_or_username))
        
        rows = cursor.fetchall()
        
        cursor.close()
        conn.close()

        db_password = rows[0][8] + rows[0][9]
        user_password = hash_password + rows[0][9]
       
        user_dict = {}
        if db_password == user_password and rows[0][10] == True and rows[0][11] == True and rows[0][12] == False:
            
            for row in rows:
                user_dict = {
                    'users': {
                        'userid': row[0],
                        'username': row[1],
                        'email': row[2],
                        'firstname': row[3],
                        'lastname': row[4],
                        'dob': row[5],
                        'gender': row[6]
                    },
                    'user_profiles': {
                        'bio': row[12],
                        'interest': row[13],
                        'picture_link': row[14]
                    }
                }

            return user_dict, True
        else:
            return None, False

    except Exception as e:
        print(f"An error occurred: {e}")

