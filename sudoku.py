import sys
import numpy as np


def sudoku():
    while True:
        try:
            first_cell_digit = int(
                input("Enter the first cell digit (in between 1 and 6): "))
            break
        except:
            print("Please enter a valid number input")
    if first_cell_digit < 0 or first_cell_digit > 6:
        print("Enter a number between 1 and 6")
    else:
        empty_array = np.full((6, 6), 0)
        empty_array[0][0] = first_cell_digit

        sudoku_generator(empty_array)


def is_filled(array):
    for row_value in range(0, 6):
        for column_value in range(0, 6):
            if array[row_value][column_value] == 0:
                return False
    return True


def values(array, i, j):
    values_array = {}

    # set all the values in the values_array as 0
    for possible_value_index in range(1, 7):
        values_array[possible_value_index] = 0

    # possible entries in each row cells
    for column_value in range(0, 6):
        if array[i][column_value] != 0:
            values_array[array[i][column_value]] = 1

    # possible entries in each column cells
    for row_value in range(0, 6):
        if array[row_value][j] != 0:
            values_array[array[row_value][j]] = 1

    # possible entries in each 2x3 block cells
    row = column = 0

    if i >= 0 and i <= 1:
        row = 0
    elif i >= 2 and i <= 3:
        row = 2
    else:
        row = 4

    if j >= 0 and j <= 2:
        column = 0
    else:
        column = 3
    for row_value in range(row, row + 2):
        for column_value in range(column, column + 3):
            if array[row_value][column_value] != 0:
                values_array[array[row_value][column_value]] = 1

    for possible_value_index in range(1, 7):
        if values_array[possible_value_index] == 0:
            values_array[possible_value_index] = possible_value_index
        else:
            values_array[possible_value_index] = 0
    # print(values_array)
    return values_array


def sudoku_generator(array):
    i = j = 0
    possiblities = {}

    if is_filled(array):
        print("  ================")
        for row_value in range(0, 6):
            if row_value in (2, 4):
                print("||================||")
            for column_value in range(0, 6):
                if column_value == 0:
                    print("||", end=" ")
                print(array[row_value][column_value], end=" ")
                if column_value == 2:
                    print("||", end=" ")
                if column_value == 5:
                    print("||")
        print("  ================")
        sys.exit()
    else:
        for row_value in range(0, 6):
            for column_value in range(0, 6):
                if array[row_value][column_value] == 0:
                    i = row_value
                    j = column_value
                    break
            else:
                continue
            break

        # all possible entries for cell(i,j)
        possiblities = values(array, i, j)

        for possible_value_index in range(1, 7):
            if possiblities[possible_value_index] != 0:
                array[i][j] = possiblities[possible_value_index]
                sudoku_generator(array)
        array[i][j] = 0


if __name__ == "__main__":
    sudoku()
