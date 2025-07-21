import matplotlib.pyplot as plt
import matplotlib
# 讀檔
with open("graph.txt", "r") as f:
    lines = f.read().strip().splitlines()


n = int(lines[0])
points = [tuple(float(x) for x in lines[i + 1].split()) for i in range(n)]
points = [(x * 300, y * 300) for x, y in points]

m = int(lines[n + 1])
edges = [tuple(map(int, lines[n + 2 + i].split())) for i in range(m)]


# 顏色設定
node_color = "#800080"
edge_color = "#0000FF"

theme = {
"mathtext.fontset": "custom",
"font.family": "Times New Roman",
"mathtext.default": "default",
"mathtext.it": "Times New Roman:italic",
"mathtext.cal": "Times New Roman:italic",
"text.usetex": True,
}

matplotlib.rcParams.update(theme)

plt.figure(figsize=(10, 10))  # 正方形圖片
plt.grid(True, linestyle='--', alpha=0.3)


pad = 5
plt.xlim(-pad, 150 + pad)
plt.ylim(-2 * pad, 300 + 2 * pad)

plt.gca().set_aspect('auto')  # 不保持比例，讓圖框正方形但內容會失真
# plt.gca().set_aspect('equal', adjustable='box')


plt.xlabel("X (km)", fontsize=22)
plt.ylabel("Y (km)", fontsize=22)
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)

# 畫邊
for u, v in edges:
    x1, y1 = points[u]
    x2, y2 = points[v]
    plt.plot([x1, x2], [y1, y2], color=edge_color, linewidth=1.2)

# 光暈
shadow_layers = [
    (460, '#f2e6f2'),
    (380, '#e0b0e0'),
    (300, '#c080c0'),
]

for size, color in shadow_layers:
    plt.scatter(*zip(*points),
                s=size,
                color=color,
                edgecolors='none',
                zorder=1)

# 節點本體
plt.scatter(*zip(*points),
            s=90,
            color=node_color,
            edgecolors='white',
            linewidths=0.8,
            zorder=2)

plt.tight_layout()
plt.savefig("topo.eps", dpi=800, bbox_inches='tight')
plt.savefig("topo.png", dpi=800, bbox_inches='tight')
# plt.show()
