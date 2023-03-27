Moscow = [0, 641, 2965, 1790, 810, 53, 1138, 1884, 535, 1009]
SPB = [641, 0, 2636, 2230, 1510, 313, 1363, 2079, 837, 1186]
Novosibirsk = [2965, 2636, 0, 1610, 2530, 1376, 294, 470, 1061, 2028]
EKB = [1790, 2230, 1610, 0, 1010, 669, 212, 1171, 474, 1457]
Kazan = [810, 1510, 2530, 1010, 0, 323, 779, 1531, 296, 1152]
NyzNov = [53, 313, 1376, 669, 323, 0, 939, 1687, 388, 1086]
Chelyabinsk = [1138, 1363, 294, 212, 779, 939, 0, 1305, 356, 1324]
Omsk = [1884, 2079, 470, 1171, 1531, 1687, 1305, 0, 637, 1628]
Samara = [535, 837, 1061, 474, 296, 388, 356, 637, 0, 1280]
Rostov = [1009, 1186, 2028, 1457, 1152, 1086, 1324, 1628, 1280, 0]
towns = [Moscow, SPB, Novosibirsk, EKB, Kazan, NyzNov, Chelyabinsk, Omsk, Samara, Rostov]

for i in range(len(towns)):
    for j in range(len(towns[i])):
        towns[i][j] = [towns[i][j], j]

n = 10
s, f = map(int, input("Введите начальный и конечный город (число от 1 до 10)").split())
s -= 1
f -= 1
if s > 10 or f > 10:
    print("Некорректный ввод")
else:
    now = []
    now.append(s)
    dist = [10 ** 6 for i in range(n)]
    dist[s] = 0
    used = [False for i in range(n)]
    used[s] = True
    while len(now) != 0:
        cur = towns[now[0]]
        cur.sort()
        for i in cur:
            if used[i[1]]:
                if dist[i[1]] > dist[now[0]] + i[0]:
                    now.append(i[1])
                dist[i[1]] = min(dist[i[1]], dist[now[0]] + i[0])
            else:
                used[i[1]] = True
                dist[i[1]] = dist[now[0]] + i[0]
                now.append(i[1])
        now.pop(0)
    print(dist[f])
