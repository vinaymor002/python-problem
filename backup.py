import datetime

prime_numbers = [2, 3, 5, 7]


def is_prime(num):
    for _i in prime_numbers:
        if num % _i == 0:
            return False
    else:
        return True


i = 11
stat_time = datetime.datetime.now()
while i <= pow(10, 15):
    if is_prime(i):
        prime_numbers.append(i)
        rev_num = int(str(i)[::-1])
        if rev_num < i:
            if rev_num in prime_numbers:
                print i
    if (datetime.datetime.now() - stat_time).seconds >= 5:
        break
    i += 2

