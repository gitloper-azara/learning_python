# more on list comprehension

comp = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            comp.append((x, y))
print(comp)

# or a more efficient way
comp2 = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(comp2)