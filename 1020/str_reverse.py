str1 = "abcdef"

idx = -1
while idx >= -len(str1):
    print(str[idx])
    idx -= 1

# memo
i = len(str1)
rev = list(str1)
for c in str1:
    i -= 1
    rev[i] = c
print(join(rev))