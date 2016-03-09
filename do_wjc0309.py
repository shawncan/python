print([x * x for x in range(1,11)])

print([x * x for x in range(1,11) if x % 2 == 0])

print(list(range(1,11)))

print([m + n for m in 'ABC' for n in 'XYZ'])
print([m + n for m in 'XYZ' for n in 'ABC'])

print([x * y for x in range(1,11) for y in '2'])