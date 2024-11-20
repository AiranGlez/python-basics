# TODO: Create a decorator that verifies if an user has permission to execute the decorated function.
# The decorator must receive an argument with the user level access.
# If the user doesn't have permissions the decorator must deny access to the function.

from functools import wraps

current_user = {
    "name": "user1",
    "role": "viewer",
}

# define the decorator with arguments
def access_control(role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user_role = current_user.get("role")
            if user_role == role or user_role == "admin":
                print("Access granted")
                return func(*args, **kwargs)
            else:
                raise PermissionError(f"Acces denied: Required role: {role}")
        return wrapper
    return decorator

@access_control('admin')
def delete_database():
    print("Database deleted!")

@access_control('viewer')
def view_database():
    print("Show data")

try:
    view_database()
    delete_database()
except PermissionError as e:
    print(e)