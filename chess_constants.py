'''
所有的常量都写在这个文件里
'''
# 两个玩家
my_max = True
my_min = False
# 八个棋子
kong = 0 # ô trống 
jiang = 1 # vua 
che = 2 # xe
ma = 3 # ma
pao = 4 #phao
xiang = 5 #tuong
shi = 6 #sy
bing = 7 #tot
# 初始化的棋盘
init_borad = [
    [che, kong, kong, bing, kong, kong, bing, kong, kong, che],
    [ma, kong, pao, kong, kong, kong, kong, pao, kong, ma],
    [xiang, kong, kong, bing, kong, kong, bing, kong, kong, xiang],
    [shi, kong, kong, kong, kong, kong, kong, kong, kong, shi],
    [jiang, kong, kong, bing, kong, kong, bing, kong, kong, jiang],
    [shi, kong, kong, kong, kong, kong, kong, kong, kong, shi],
    [xiang, kong, kong, bing, kong, kong, bing, kong, kong, xiang],
    [ma, kong, pao, kong, kong, kong, kong, pao, kong, ma],
    [che, kong, kong, bing, kong, kong, bing, kong, kong, che]
]
# 最大步数

max_depth = 4
def change_depth(x):
    max_depth = x 
# 最大值，最小值
max_val = 1000000
min_val = -1000000
# 评估方法
base_val = [0, 0, 500, 300, 300, 250, 250, 80]
mobile_val = [0, 0, 6, 12, 6, 1, 1, 15]
pos_val = [
    [  # 空
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [  # 将
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        1, -8, -9, 0, 0, 0, 0, 0, 0, 0,
        5, -8, -9, 0, 0, 0, 0, 0, 0, 0,
        1, -8, -9, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ],
    [  # 车
        -6, 5, -2, 4, 8, 8, 6, 6, 6, 6,
        6, 8, 8, 9, 12, 11, 13, 8, 12, 8,
        4, 6, 4, 4, 12, 11, 13, 7, 9, 7,
        12, 12, 12, 12, 14, 14, 16, 14, 16, 13,
        0, 0, 12, 14, 15, 15, 16, 16, 33, 14,
        12, 12, 12, 12, 14, 14, 16, 14, 16, 13,
        4, 6, 4, 4, 12, 11, 13, 7, 9, 7,
        6, 8, 8, 9, 12, 11, 13, 8, 12, 8,
        -6, 5, -2, 4, 8, 8, 6, 6, 6, 6
    ],
    [  # 马
        0, -3, 5, 4, 2, 2, 5, 4, 2, 2,
        -3, 2, 4, 6, 10, 12, 20, 10, 8, 2,
        2, 4, 6, 10, 13, 11, 12, 11, 15, 2,
        0, 5, 7, 7, 14, 15, 19, 15, 9, 8,
        2, -10, 4, 10, 15, 16, 12, 11, 6, 2,
        0, 5, 7, 7, 14, 15, 19, 15, 9, 8,
        2, 4, 6, 10, 13, 11, 12, 11, 15, 2,
        -3, 2, 4, 6, 10, 12, 20, 10, 8, 2,
        0, -3, 5, 4, 2, 2, 5, 4, 2, 2
    ],
    [  # 炮
        0, 0, 1, 0, -1, 0, 0, 1, 2, 4,
        0, 1, 0, 0, 0, 0, 3, 1, 2, 4,
        1, 2, 4, 0, 3, 0, 3, 0, 0, 0,
        3, 2, 3, 0, 0, 0, 2, -5, -4, -5,
        3, 2, 5, 0, 4, 4, 4, -4, -7, -6,
        3, 2, 3, 0, 0, 0, 2, -5, -4, -5,
        1, 2, 4, 0, 3, 0, 3, 0, 0, 0,
        0, 1, 0, 0, 0, 0, 3, 1, 2, 4,
        0, 0, 1, 0, -1, 0, 0, 1, 2, 4
    ],
    [  # 相
        0, 0, -2, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 3, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, -2, 0, 0, 0, 0, 0, 0, 0
    ],
    [  # 士
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 3, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ],
    [  # 兵
        0, 0, 0, -2, 3, 10, 20, 20, 20, 0,
        0, 0, 0, 0, 0, 18, 27, 30, 30, 0,
        0, 0, 0, -2, 4, 22, 30, 45, 50, 0,
        0, 0, 0, 0, 0, 35, 40, 55, 65, 2,
        0, 0, 0, 6, 7, 40, 42, 55, 70, 4,
        0, 0, 0, 0, 0, 35, 40, 55, 65, 2,
        0, 0, 0, -2, 4, 22, 30, 45, 50, 0,
        0, 0, 0, 0, 0, 18, 27, 30, 30, 0,
        0, 0, 0, -2, 3, 10, 20, 20, 20, 0
    ]
]
