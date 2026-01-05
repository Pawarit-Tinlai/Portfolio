users = []

def register(username, password):
    users.append({
        "username": username,
        "password": password
    })

def login(username, password):
    for user in users:
        if user["username"] == username and user["password"] == password:
            return "Login success"
    return "Login failed"


# Example
register("admin", "1234")
print(login("admin", "1234"))
print(login("admin", "0000"))
