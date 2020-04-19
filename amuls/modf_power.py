def concat_sequence(s1, s2):
    yield from s1
    yield from s2


seq1 = range(10)
seq2 = range(10, 20)
result = concat_sequence(seq1, seq2)

print("seq1")
for i in result:
    print(i)

result = concat_sequence(seq1, seq2)

print("seq2")
for i in result:
    print(i)
