
print("hellow world1")
def sum(a, b):
    return a + b
print("hellow world2")
print(sum(1, 2))


# Path: hello_world.py
def login(username, password):
    if username == "admin" and password == "admin":
        return "Login Success"
    else:
        return "Login Failed"

print(login("admin", "admin"))