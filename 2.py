def maze_build():
    maze = [[0 for j in range(10)] for i in range(10)]
    # 随机选择入口和出口
    while(1):
        entrance = random.choice([(0, i) for i in range(1, 9)] + [(i, 0) for i in range(1, 9)] + [(i, 9) for i in range(1, 9)])
        exit = random.choice([(0, i) for i in range(1, 9)] + [(i, 0) for i in range(1, 9)] + [(i, 9) for i in range(1, 9)])
        if(entrance[0]!=exit[0] and entrance[1]!=exit[1]):
            maze[entrance[0]][entrance[1]] = 2
            maze[exit[0]][exit[1]] = 8
            break
    for i in range(1, 9):
        for j in range(1, 9):
            maze[i][j] = random.randint(0, 1)
    return maze
import random
maze=maze_build()
for i in range(10):
    for j in range (10):
        print(maze[i][j],end='')
    print('\n',end='')

