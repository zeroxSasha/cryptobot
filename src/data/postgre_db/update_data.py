def change_moneylimit(connection, user_id: int, money_limit: int) -> None:
    with connection.cursor() as cursor:
        cursor.execute(
            f'''UPDATE users SET money_limit = {money_limit} WHERE user_id = {user_id};'''
        )

def change_listofcoins(connection, user_id: int, list_of_coins: int) -> None:
    with connection.cursor() as cursor:
        cursor.execute(
            f'''UPDATE users SET list_of_coins = {list_of_coins} WHERE user_id = {user_id};'''
        )
