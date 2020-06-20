import sqlite3


class SQLite:

    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def user_exists(self, user_id):
        """Проверяем, есть ли уже пользователь в базе"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `users` WHERE `user_id` = ?', (user_id,)).fetchall()
            return bool(len(result))

    def add_user(self, user_id, status=True):
        """Добавляем нового пользователя"""
        with self.connection:
            return self.cursor.execute("INSERT INTO users (user_id) values (?)", (user_id,))

    def update_city(self, user_id, city):
        """Обновляем географическую долготу"""
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `city` = ? WHERE `user_id` = ?", (city, user_id))

    # -=-=-=-= КАТЕГОРИИ -=-=-=-=-=-
    def category(self, user_id, category):
        with self.connection:
            result = self.cursor.execute(f'SELECT {category} FROM users WHERE user_id = ?', (user_id,)).fetchone()
            return str(result[0])

    def check(self, user_id, category):
        result = self.cursor.execute(f'SELECT {category} FROM `users` WHERE `user_id` = ?', (user_id,)).fetchone()
        return str(result[0])

    def check_city(self, user_id):
        result = self.cursor.execute(f'SELECT `*` FROM `users` WHERE `city` = ?', (user_id,)).fetchone()
        return str(result[0])

    def update(self, user_id, value, category):
        """Обновляем географическую долготу"""
        with self.connection:
            return self.cursor.execute(f"UPDATE `users` SET {category} = ? WHERE `user_id` = ?", (value, user_id))

    def ussr(self):
        with self.connection:
            ret = self.cursor.execute("SELECT `user_id` FROM `users`").fetchall()
            return ret
