from db import get_connection

def create_table():
    conn = get_connection()
    if not conn:
        return
    
    try:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    age INT NOT NULL
                );
            """)
            conn.commit()
            print("Table created successfully.")
    except Exception as e:
        print("Error creating table:", e)
    finally:
        conn.close()

def insert_user(name, age):
    conn = get_connection()
    if not conn:
        return
    
    try:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO users (name, age) VALUES (%s, %s) RETURNING id;", (name, age))
            user_id = cur.fetchone()[0]
            conn.commit()
            print(f"User added with ID: {user_id}")
    except Exception as e:
        print("Error inserting user:", e)
    finally:
        conn.close()

def read_users():
    conn = get_connection()
    if not conn:
        return
    
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users;")
            users = cur.fetchall()
            for user in users:
                print(user)
    except Exception as e:
        print("Error reading users:", e)
    finally:
        conn.close()

def update_user(user_id, name, age):
    conn = get_connection()
    if not conn:
        return
    
    try:
        with conn.cursor() as cur:
            cur.execute("UPDATE users SET name=%s, age=%s WHERE id=%s;", (name, age, user_id))
            conn.commit()
            print(f"User {user_id} updated.")
    except Exception as e:
        print("Error updating user:", e)
    finally:
        conn.close()

def delete_user(user_id):
    conn = get_connection()
    if not conn:
        return
    
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM users WHERE id=%s;", (user_id,))
            conn.commit()
            print(f"User {user_id} deleted.")
    except Exception as e:
        print("Error deleting user:", e)
    finally:
        conn.close()