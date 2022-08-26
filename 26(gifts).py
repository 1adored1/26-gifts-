f = open('26.txt')
n = int(f.readline())
a = sorted([int(x) for x in f], reverse=True)
count = 1
m = a[0]
for i in range(len(a) - 1):
    if m - a[i + 1] >= 3:
        m = a[i + 1]
        count += 1
print(count, m)