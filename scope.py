
message = "Hello"


def greet():
    # global message  # will grant access to global 'message'
    message = "Salut"


greet()
print(message)  # Hello

# Python only has function scope, not block scopes like 'if' or 'for' in JS
