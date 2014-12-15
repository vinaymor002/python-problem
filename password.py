first_line = [int(x) for x in raw_input().split()]

password_repo = []
for i in range(first_line[0]):
    new_password = raw_input().split()
    found = False
    for _password in password_repo:
        if _password[::-1] == new_password[0]:
            print _password.__len__(),
            print _password[_password.__len__() / 2]
            found = True

    if found:
        break
    password_repo.append(new_password[0])