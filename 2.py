n = int(input("Введите количество экспонатов "))
st = [[0, 0, i, True] for i in range(n)]
for i in range(n):
    st[i][1], st[i][0] = map(int, input("Введите вес и стоимость экспоната ").split())
m = int(input("Введите количество заходов "))
k = int(input("Введите максимальный вес в каждый заход "))
ans = []
sm = 0
for i in range(m):
    ck = k
    cans = []
    for j in range(len(st)):
        if st[j][1] <= ck and st[j][3]:
            ck -= st[j][1]
            cans.append(st[j][2] + 1)
            st[j][3] = False
            sm += st[j][0]
    ans.append(cans)

for i in range(m):
    print("В" + str(i + 1) + "-й заход нужно вынести экспонаты:", end=' ')
    print(*ans[i])
print("В итоге будет вынесено экспонатов стоимостью", sm)