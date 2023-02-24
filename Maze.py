import random, copy, sys
from PIL import Image
sys.setrecursionlimit(1500000)


class Maze:
    def __init__(self, size):
        self.board_size = size
        self.board = []

    def generating_maze_file(self):
        def creating_maze(matrix, i, j):                            # Creating maze by DFS Algorithm
            possibles = []                                          # Check which moves are possible from point (i, j)
            if i + 1 < len(matrix): possibles.append((i + 1, j))
            if j + 1 < len(matrix): possibles.append((i, j + 1))
            if i - 1 >= 0: possibles.append((i - 1, j))
            if j - 1 >= 0: possibles.append((i, j - 1))
            random.shuffle(possibles)                               # Shuffle the order
            for pair in possibles:                                  # Do DFS for all unvisited blocks
                (new_i, new_j) = pair
                if matrix[new_i][new_j] != [0, 0, 0, 0]: continue
                if i - new_i == 1 and j == new_j:
                    matrix[i][j][0] = 1
                    matrix[new_i][new_j][2] = 1
                    creating_maze(matrix, new_i, new_j)
                elif i - new_i == -1 and j == new_j:
                    matrix[i][j][2] = 1
                    matrix[new_i][new_j][0] = 1
                    creating_maze(matrix, new_i, new_j)
                elif i == new_i and j - new_j == 1:
                    matrix[i][j][3] = 1
                    matrix[new_i][new_j][1] = 1
                    creating_maze(matrix, new_i, new_j)
                elif i == new_i and j - new_j == -1:
                    matrix[i][j][1] = 1
                    matrix[new_i][new_j][3] = 1
                    creating_maze(matrix, new_i, new_j)

        for i in range(self.board_size):                            # Creating empty Maze
            line = []
            for j in range(self.board_size):
                line.append([0, 0, 0, 0])
            self.board.append(line)
        creating_maze(self.board, 0, 0)                             # Do the algorithm

    def generating_file(self):
        self.generating_maze_file()

        def list_to_str(list_obj):
            result = ""
            for i in range(len(list_obj)):
                result += str(list_obj[i])
            return result

        maze_file = Image.new("RGB", (40*self.board_size, 40*self.board_size), (255,0,255))
        for i in range(self.board_size):
            for j in range(self.board_size):
                temp = list_to_str(self.board[i][j])
                block = Image.open(r'structures\{}.png'.format(temp))
                maze_file.paste(block, (j*40, i*40))
        block = Image.open(r'structures\start.png')
        maze_file.paste(block, (0, 8))
        maze_file.paste(block, (40*self.board_size-13, 40*self.board_size-32))
        maze_file.save('maze.png')

    def generating_maze_gif(self):
        images = []

        def creating_maze(matrix, i, j):
            images.append(copy.deepcopy(matrix))
            possibles = []
            if i + 1 < len(matrix): possibles.append((i + 1, j))
            if j + 1 < len(matrix): possibles.append((i, j + 1))
            if i - 1 >= 0: possibles.append((i - 1, j))
            if j - 1 >= 0: possibles.append((i, j - 1))
            random.shuffle(possibles)
            for pair in possibles:
                (new_i, new_j) = pair
                if matrix[new_i][new_j] != [0, 0, 0, 0]: continue
                if i - new_i == 1 and j == new_j:
                    matrix[i][j][0] = 1
                    matrix[new_i][new_j][2] = 1
                    creating_maze(matrix, new_i, new_j)
                elif i - new_i == -1 and j == new_j:
                    matrix[i][j][2] = 1
                    matrix[new_i][new_j][0] = 1
                    creating_maze(matrix, new_i, new_j)
                elif i == new_i and j - new_j == 1:
                    matrix[i][j][3] = 1
                    matrix[new_i][new_j][1] = 1
                    creating_maze(matrix, new_i, new_j)
                elif i == new_i and j - new_j == -1:
                    matrix[i][j][1] = 1
                    matrix[new_i][new_j][3] = 1
                    creating_maze(matrix, new_i, new_j)

        for i in range(self.board_size):
            line = []
            for j in range(self.board_size):
                line.append([0, 0, 0, 0])
            self.board.append(line)
        creating_maze(self.board, 0, 0)
        return images

    def generating_gif(self):

        def generating_image(matrix, size):
            def list_to_str(temp):
                result = ""
                for i in range(len(temp)):
                    result += str(temp[i])
                return result

            maze_file = Image.new("RGB", (40 * size, 40 * size), (255, 0, 255))
            for i in range(size):
                for j in range(size):
                    temp = list_to_str(matrix[i][j])
                    block = Image.open(r'structures\{}.png'.format(temp))
                    maze_file.paste(block, (j * 40, i * 40))

            block = Image.open(r'structures\start.png')
            maze_file.paste(block, (0, 8))
            if matrix[-1][-1] != [0, 0, 0, 0]:
                maze_file.paste(block, (40 * self.board_size - 13, 40 * self.board_size - 32))
            return maze_file

        images_matrix = self.generating_maze_gif()
        images_file = []
        for i in range(len(images_matrix)):
            img = generating_image(images_matrix[i], self.board_size)
            images_file.append(img)
        images_file[0].save(r'.\maze.gif', save_all=True, append_images=images_file[1:], optimize=False, duration=40, loop=0)

    def generating_gif_and_file(self):
        def generating_image(matrix, size):
            def list_to_str(temp):
                result = ""
                for i in range(len(temp)):
                    result += str(temp[i])
                return result

            maze_file = Image.new("RGB", (40*size, 40*size), (255, 0, 255))
            for i in range(size):
                for j in range(size):
                    temp = list_to_str(matrix[i][j])
                    block = Image.open(r'structures\{}.png'.format(temp))
                    maze_file.paste(block, (j * 40, i * 40))
            block = Image.open(r'structures\start.png')
            maze_file.paste(block, (0, 8))
            if matrix[-1][-1] != [0, 0, 0, 0]:
                maze_file.paste(block, (40 * self.board_size - 13, 40 * self.board_size - 32))
            return maze_file

        images_matrix = self.generating_maze_gif()
        images_file = []
        for i in range(len(images_matrix)):
            img = generating_image(images_matrix[i], self.board_size)
            images_file.append(img)
        images_file[0].save(r'.\maze.gif', save_all=True, append_images=images_file[1:], optimize=False, duration=40, loop=0)
        images_file[-1].save(r'.\maze.png')
