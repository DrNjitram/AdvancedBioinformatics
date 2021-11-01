from itertools import permutations

a = [_ for _ in range(1, 8)]

perms = set(permutations(a))

print(len(perms))
for perm in perms:
    print(" ".join([str(_) for _ in perm]))

