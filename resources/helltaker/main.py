import cv2
import numpy as np
import sys
import os

# 每个格子的长宽（map图片不同则需要调整）
cell_rows = 100
cell_cols = 100

# 初始值调整（map图片不同则需要调整）
init_rows = 20
init_cols = 110


def addA2B(A, B, position_rows, position_cols):
    b, g, r, a = cv2.split(A)
    rows, cols, channels = A.shape

    for i in range(rows):
        for j in range(cols):
            if a[i][j] > 200:
                B[i + position_rows][j + position_cols] = A[i][j]


def add(img, array):
    if type(array[0]) == int:
        addA2B(img, img_map1, init_rows + array[0] * cell_rows, init_cols + array[1] * cell_cols)
        return 0;
    else:
        for i in range(len(array)):
            addA2B(img, img_map1, init_rows + array[i][0] * cell_rows, init_cols + array[i][1] * cell_cols)


def update():
    me.clear()
    stone.clear()
    enemy.clear()
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 4:
                me.append(i)
                me.append(j)
            if map[i][j] == 3:
                stone.append([i, j])
            if map[i][j] == 2:
                enemy.append([i, j])


# 左是 0 -1
# 右是 0 1
# 上是 -1 0
# 下是 1 0
#   ------->y (cols)
#   |
#   |
#   √
#   x(rows)
def move(x, y):
    if map[me[0] + x][me[1] + y] == 0:
        over = cv2.imread('./plugins/PushBox-plugin/resources/helltaker/over.png', -1)
        # 显示地图
        # cv2.imshow('over', over)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        # 储存地图
        cv2.imwrite("./plugins/PushBox-plugin/resources/helltaker/now.png", over)
        os.remove("./plugins/PushBox-plugin/resources/helltaker/array")
        sys.exit(0)
    # 前面是地板就往前走一步
    if map[me[0] + x][me[1] + y] == 1:
        # 交换二者位置
        map[me[0] + x][me[1] + y] = 4
        map[me[0]][me[1]] = 1
    # 推怪
    if map[me[0] + x][me[1] + y] == 2 and map[me[0] + x * 2][me[1] + y * 2] == 1:
        map[me[0] + x * 2][me[1] + y * 2] = 2
        map[me[0] + x][me[1] + y] = 1
    # 推石头
    if map[me[0] + x][me[1] + y] == 3 and map[me[0] + x * 2][me[1] + y * 2] == 1:
        map[me[0] + x * 2][me[1] + y * 2] = 3
        map[me[0] + x][me[1] + y] = 1
    # 把怪踢爆
    if map[me[0] + x][me[1] + y] == 2 and map[me[0] + x * 2][me[1] + y * 2] >= 2:
        map[me[0] + x][me[1] + y] = 1


if __name__ == "__main__":
    # 外部墙体 5
    # 我 4
    # 石头 3
    # 怪 2
    # 地面 1
    # 白毛 0
    # a = [[5, 5, 5, 5, 5, 5, 5, 5, 5],
    #      [5, 5, 5, 5, 5, 1, 4, 5, 5],
    #      [5, 5, 1, 1, 2, 1, 1, 5, 5],
    #      [5, 5, 1, 2, 1, 2, 5, 5, 5],
    #      [5, 1, 1, 5, 5, 5, 5, 5, 5],
    #      [5, 1, 3, 1, 1, 3, 1, 5, 5],
    #      [5, 1, 3, 1, 3, 1, 1, 0, 5],
    #      [5, 5, 5, 5, 5, 5, 5, 5, 5]]
    # 读取地图
    print(os.path.exists("./plugins/PushBox-plugin/resources/helltaker/array"))
    if os.path.exists("./plugins/PushBox-plugin/resources/helltaker/array"):
        map = np.loadtxt("./plugins/PushBox-plugin/resources/helltaker/array")
    else:
        map = np.loadtxt("./plugins/PushBox-plugin/resources/helltaker/save")

    # 我 敌人 石头的位置
    me = []
    stone = []
    enemy = []
    update()

    # 读取照片
    img_me = cv2.imread('./plugins/PushBox-plugin/resources/helltaker/me.png', -1)
    img_map1 = cv2.imread('./plugins/PushBox-plugin/resources/helltaker/map1.png', -1)
    img_stone = cv2.imread('./plugins/PushBox-plugin/resources/helltaker/stone.png', -1)
    img_enemy = cv2.imread('./plugins/PushBox-plugin/resources/helltaker/enemy.png', -1)

    # 处理上下左右操作
    if len(sys.argv) == 2:
        if sys.argv[1] == '左':
            move(0, -1)
        if sys.argv[1] == '右':
            move(0, 1)
        if sys.argv[1] == '上':
            move(-1, 0)
        if sys.argv[1] == '下':
            move(1, 0)

    # 地图数组变更 重新读取各个东西的位置
    update()

    # 贴我 敌人 石头
    add(img_me, me)
    add(img_stone, stone)
    add(img_enemy, enemy)

    # 显示地图
    # cv2.imshow('map1', img_map1)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # 储存地图
    cv2.imwrite("./plugins/PushBox-plugin/resources/helltaker/now.png", img_map1)
    # 保存地图数组
    np.savetxt("./plugins/PushBox-plugin/resources/helltaker/array", map)
