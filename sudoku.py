
# matriz_sudoku =

# print(matriz_sudoku)



# import NumPy as np


# def is_valid(sudoku, x, y, value):
#     return value not in sudoku[x, :] and value not in sudoku[:, y] and value not in quadrant(sudoku, x, y)


# def quadrant(sudoku, x, y):
#     xx = x // 3
#     yy = y // 3
#     return sudoku[xx * 3:(xx + 1) * 3, yy * 3:(yy + 1) * 3]


# def possibilities(sudoku, x, y):
#     possibilities = list()
#     for value in range(1, 10):
#         if is_valid(sudoku, x, y, value):
#             possibilities.append(value)
#     return possibilities


# def solver(sudoku, solutions):
#     for (x, y), value in np.ndenumerate(sudoku):
#         if value == 0:
#             for possibility in possibilities(sudoku, x, y):
#                 sudoku[x, y] = possibility
#                 solver(sudoku, solutions)
#                 sudoku[x, y] = 0
#             return
#     solutions.append(sudoku.copy())


# if __name__ == '__main__':
#     sudoku = np.array([5, 3, 0, 0, 7, 0, 0, 0, 0,
#                        6, 0, 0, 1, 9, 5, 0, 0, 0,
#                        0, 9, 8, 0, 0, 0, 0, 6, 0,
#                        8, 0, 0, 0, 6, 0, 0, 0, 3,
#                        4, 0, 0, 8, 0, 3, 0, 0, 1,
#                        7, 0, 0, 0, 2, 0, 0, 0, 6,
#                        0, 6, 0, 0, 0, 0, 2, 8, 0,
#                        0, 0, 0, 4, 1, 9, 0, 0, 5,
#                        0, 0, 0, 0, 8, 0, 0, 7, 9]).reshape([9, 9])
#     solutions = list()
#     solver(sudoku, solutions)
#     for solution in solutions:
#         print(solution)


# def quadrante(num_alt,sudoku):
    
#     sudoku=[3, 3, 0, 0, 7, 0, 0, 0, 0,
#         6, 0, 0, 1, 9, 5, 0, 0, 0,
#         0, 9, 8, 0, 0, 0, 0, 6, 0,
#         8, 0, 0, 0, 6, 0, 0, 0, 3,
#         4, 0, 0, 8, 0, 3, 0, 0, 1,
#         7, 0, 0, 0, 2, 0, 0, 0, 6,
#         0, 6, 0, 0, 0, 0, 2, 8, 0,
#         0, 0, 0, 4, 1, 9, 0, 0, 5,
#         0, 0, 0, 0, 8, 0, 0, 7, 9]


# alteracao = input (" ")

# print(alteracao)

# minha_lista2 = [2,3,4],[3,4,5],[3,4,5],[3,4,5],[3,4,5],[3,4,5],[3,4,5],[3,4,5],[3,4,5]

# for item in minha_lista2:
#    print(item)

# produtos = [
#     {'id': '2810', 'tipo': 'forno', 'ano': 2020},
#     {'id': '9812', 'tipo': 'celular', 'ano': 2019},
#     {'id': '7756', 'tipo': 'geladeira', 'ano': 2022}
# ]

# print(produtos)
# ###

# sudoku = [
#   [9, 0, 0, 0, 8, 0, 3, 0, 0],
#   [0, 0, 0, 2, 5, 0, 7, 0, 0],
#   [0, 2, 0, 3, 0, 0, 0, 0, 4],
#   [0, 9, 4, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 7, 3, 0, 5, 6, 0],
#   [7, 0, 5, 0, 6, 0, 4, 0, 0],
#   [0, 0, 7, 8, 0, 3, 9, 0, 0],
#   [0, 0, 1, 0, 0, 0, 0, 0, 3],
#   [3, 0, 0, 0, 0, 0, 0, 0, 2]
# ]