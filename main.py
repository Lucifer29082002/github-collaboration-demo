def greet(name, reverse=False):
    message = f"Hello, {name}!"
    return message[::-1] if reverse else message

print(greet("World"))
print(greet("World", reverse=True))

