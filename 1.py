n = int(input("Введите сумму, которую необходимо выдать "))
s = [0, 0, 0, 0]
m = [0, 0, 0, 0]
ans = []
for i in range(4):
    m[i], s[i] = map(int, input("Введите количество и номинал монеты ").split())
for i in range(4):
    q = min(m[i], n // s[i])
    n -= q * s[i]
    ans.append(q)
for i in range(4):
    print("Необходимо выдать", ans[i], "монет(у) номиналом", s[i])
