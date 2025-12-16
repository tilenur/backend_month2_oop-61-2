#2
allowed_commands = {
   "admin": ["start", "ban", "stop"],
   "user": ["start", "message"]
}


#1
class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

user1 = User("Alice", "admin")
user2 = User("Bob", "user")

# print(user1.username)
# print(user2.role)

#3
def check_access(command):
    def decorator(func):
        def wrapper(self, user):
            if command in allowed_commands[user.role]:
                print(f'✅ Команда "{command}" выполнена пользователем {user.username}')
                return func(self, user)

            else:
                print(f"❌ Пользователь {user.username}  не может выполнять команду '{command}' ")
        return wrapper
    return decorator

class CommandHandler:

    @check_access("start")
    def start(self, user):
        print(f"Пользователь {user.username} ({user.role}) выполняет команду start")

    @check_access("ban")
    def ban(self, user):
        print(f"Пользователь {user.username} ({user.role}) выполняет команду ban")

    @check_access("stop")
    def stop(self, user):
        print(f"Пользователь {user.username} ({user.role}) выполняет команду stop")

    @check_access("message")
    def message(self, user):
        print(f"Пользователь {user.username} ({user.role}) отправил сообщение")

handler = CommandHandler()

# Alice (admin)
handler.start(user1)
handler.ban(user1)
handler.stop(user1)
handler.message(user1)

print()  # blank line

# Bob (user)
handler.start(user2)
handler.ban(user2)
handler.stop(user2)
handler.message(user2)
