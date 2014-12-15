number_of_roses = int(raw_input())
roses = [int(x) for x in raw_input().split()]

even_sum = 0
odd_petals = []
for petal in roses:
    i_petal = petal
    if not i_petal % 2:
        even_sum += i_petal
    else:
        odd_petals.append(i_petal)

if odd_petals.__len__() % 2:
    even_sum += sum(odd_petals)
else:
    even_sum += sum(sorted(odd_petals)[1:])

if even_sum % 2:
    print(even_sum)
else:
    print ":("