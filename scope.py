
message = "Hello"


def greet():
    global message # will rewrite global 'message' BAD PRACTICE
    message = "Salut"


greet()
print(message)  # Hello

# Python only has function scope, not block scopes like 'if' or 'for' in JS
