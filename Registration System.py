users = []

def register(name, username):
    for user in users:
        if user["username"] == username:
            return "Username already exists"

    users.append({
        "name": name,
        "username": username
    })
    return "Register success"


def show_users():
    for user in users:
        print(f"{user['name']} ({user['username']})")


# Example
print(register("Red", "red01"))
print(register("Red", "red01"))
show_users()
