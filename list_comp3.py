# oh jeez! more list comprehension
vec = [-4, -2, 0, 2, 4]
srt = []
for x in vec:
    srt.append(x * 2)
print(srt)

srt1 = []
for x in vec:
    if x >= 0:
        srt1.append(x)
print(srt1)

srt2 = []
for x in vec:
    srt2.append(abs(x))
print(srt2)

print()
# or
vec1 = [-4, -2, 0, 2, 4]
print([x * 2 for x in vec1])
print([x for x in vec1 if x >= 0])
print([abs(x) for x in vec1])