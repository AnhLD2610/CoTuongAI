my_max = True
my_min = False
# quân cờ
kong = 0 # ô trống 
vua = 1 # vua 
xe = 2 # xe
ma = 3 # ma
phao = 4 #phao
tuong = 5 #tuong
si = 6 #sy
tot = 7 #tot
# bàn cờ
init_borad = [
    [xe, kong, kong, tot, kong, kong, tot, kong, kong, xe],
    [ma, kong, phao, kong, kong, kong, kong, phao, kong, ma],
    [tuong, kong, kong, tot, kong, kong, tot, kong, kong, tuong],
    [si, kong, kong, kong, kong, kong, kong, kong, kong, si],
    [vua, kong, kong, tot, kong, kong, tot, kong, kong, vua],
    [si, kong, kong, kong, kong, kong, kong, kong, kong, si],
    [tuong, kong, kong, tot, kong, kong, tot, kong, kong, tuong],
    [ma, kong, phao, kong, kong, kong, kong, phao, kong, ma],
    [xe, kong, kong, tot, kong, kong, tot, kong, kong, xe]
]

max_depth = 3
max_val = 1000000
min_val = -1000000
base_val = [0, 10000000, 500, 250 , 300, 150, 150, 80]
pos_val = [
    [  # o trong
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [  # tuong
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
    [  # xe
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
    [  # ma
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
    [  # phao
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
    [  # tượng
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
    [  # sĩ
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
    [  # tốt
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
