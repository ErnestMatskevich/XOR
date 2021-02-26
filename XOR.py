a = ''
b = ''
c = ''
d = ''
for i in range(1, 421):
    if i % 3 == 0:
        a = a + "1"
    else:
        a = a + "0"
for k in range(1, 421):
    if k % 7 == 0:
        b = b + "1"
    else:
        b = b + "0"
for j in range(1, 421):
    if j % 4 == 0:
        c = c + "1"
    else:
        c = c + "0"
for n in range(1, 421):
    if n % 5 == 0:
        d = d + "1"
    else:
        d = d + "0"

count = 0
for q in range(420):
    if int(a[q]) ^ int(b[q]) ^ int(c[q]) ^ int(d[q]):
        count = count + 1
print(count)
