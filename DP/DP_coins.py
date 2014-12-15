# values = [1, 3, 4, 5, 6, 7, 8, 9, 10]
import datetime

coins = [1, 3, 5]

M = [0]

start_time = datetime.datetime.now()
for i in range(1, pow(10, 2)):
    M.append(99999999999)
    for coin in coins:
        if i >= coin and M[i - coin] + 1 < M[i]:
            M[i] = M[i - coin] + 1
end_time = datetime.datetime.now()

print (end_time - start_time)