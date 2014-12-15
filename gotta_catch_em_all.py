N = int(raw_input())

pokemons = [int(i) for i in raw_input().split()]

pokemons.sort(reverse=True)
result = []
j = 1
for i in pokemons:
    result.append(i + j)
    j += 1

print max(result) + 1