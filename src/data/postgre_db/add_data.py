def add_new_user(connection, user_id: int, days_left: int, money_limit: int, list_of_coins: int) -> None:
    with connection.cursor() as cursor:
        
        # Check if user already exists
        cursor.execute(
            f'''SELECT user_id FROM users WHERE user_id = {user_id};'''
        )
        if cursor.fetchone():
            return
        
        # Add new user
        cursor.execute(
            f'''INSERT INTO users (user_id, days_left, money_limit, list_of_coins)
            VALUES ({user_id}, {days_left}, {money_limit}, {list_of_coins});'''
        )
