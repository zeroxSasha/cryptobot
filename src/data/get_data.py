def get_all_users(connection) -> list:
    with connection.cursor() as cursor:
        cursor.execute(
            f'''SELECT * FROM users;'''
        )
        return cursor.fetchall()
