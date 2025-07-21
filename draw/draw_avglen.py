import matplotlib.pyplot as plt
import math
# 讀檔
with open("graph.txt", "r") as f:
    lines = f.read().strip().splitlines()

n = int(lines[0])
points = [tuple(float(x) for x in lines[i + 1].split()) for i in range(n)]
points = [(x * 300, y * 300) for x, y in points]

m = int(lines[n + 1])
edges = [tuple(map(int, lines[n + 2 + i].split())) for i in range(m)]

total_length = 0
for u, v in edges:
    x1, y1 = points[u]
    x2, y2 = points[v]
    total_length += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

avg_length = total_length / len(edges)
print(f"平均邊長：{avg_length:.2f} km")