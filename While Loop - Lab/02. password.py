username = input()
username_password = input()
data = input()

while username_password != data:
    data = input()
print(f'Welcome {username}!')