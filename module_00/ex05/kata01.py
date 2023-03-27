#!/usr/bin/python3

kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

print(type(kata))

for t in kata: print(f"{t} was created by {kata[t]}")