from typing import List, Tuple
import random


Matrix = List[List[int]]


def stringify_matrix(m: Matrix) -> List[str]:

    stringified = []
    max_length = 0

    # --- Get maximal length of text-repr of row
    # --- Create string version of rows
    for row in m:

        new_row = []
        for col in row:

            # Adding values to print --> col is numeral value

            if isinstance(col, float):

                if col >= 0:
                    new_row.append("+{:.2f}".format(col))
                else:
                    new_row.append("{:.2f}".format(col))
                continue


            if col == -0:
                new_row.append(str(col))
                continue

            if col >= 0:
                new_row.append("+" + str(col))
            else:
                new_row.append(str(col))


        string_line = " ".join(new_row)
        stringified.append(string_line)

        if len(string_line) > max_length:
            max_length = len(string_line)


    PAD = 4
    res = []
    if len(stringified) == 1:
        res.append(("|" + stringified[0].center(max_length + PAD) + "|"))
        return res

    for i in range(len(stringified)):

        if i == 0:
            res.append(("/" + stringified[i].center(max_length + PAD) + "\\"))
        elif i == len(stringified) - 1:
            res.append(("\\" + stringified[i].center(max_length + PAD) + "/"))
        else:
            res.append(("|" + stringified[i].center(max_length + PAD) + "|"))

    return res


def print_matrix(m: Matrix) -> None:

    print("\n".join(stringify_matrix(m)))



def multiply(m1: Matrix, m2: Matrix) -> Matrix:
    """
    first - m x n
    second - n x p
    """

    common = len(m2)

    m = len(m1)
    p = len(m2[0])

    res = [[0 for j in range(p)] for i in range(m)]

    for i in range(m):
        for j in range(p):

            for k in range(common):

                res[i][j] += m1[i][k] * m2[k][j]

    return res


def create_random_multiply_duo(common: int,
                               boundaries: Tuple[int, int]) -> Tuple[Matrix, Matrix]:
    """
    common - common dimension of matrices
    boundaries - min and max value which can appear in matrices
    """
    
    rows = random.randint(int(common), int(common * 2))
    columns = random.randint(int(common), int(common * 2))

    m1 = [
            [random.randint(boundaries[0], boundaries[1]) for c in range(common)] for r in range(rows)
         ]

    m2 = [
            [random.randint(boundaries[0], boundaries[1]) for c in range(columns)] for r in range(common)
         ]

    return m1, m2


def parse_input() -> Matrix:

    line = input()
    lines = [line]

    while line != "":

        line = input()
        lines.append(line)

    matrix = []

    for line in lines:

        if line == "":
            continue

        row = []
        for val in line.split(" "):

            if val == "":
                continue

            row.append(int(val))

        matrix.append(row)

    return matrix


def are_equal(m1: Matrix, m2: Matrix) -> bool:

    if len(m1) != len(m2) or len(m1[0]) != len(m1[0]):
        return False

    for i in range(len(m1)):

        if len(m1[i]) != len(m2[i]):
            return False

        for j in range(len(m1[0])):

            if m1[i][j] != m2[i][j]:
                return False

    return True

# --- Interactive
def mul_excercise():

    print("###" + "Matrix-multiplication excercice".center(50) + "###")
    print()

    COMMON = 2
    LOWER, UPPER = -6, 6
    while True:

        m1, m2 = create_random_multiply_duo(COMMON, (LOWER, UPPER))

        print_matrix(m1)
        print()
        print_matrix(m2)
        print()

        user = parse_input()
        result = multiply(m1, m2)

        print("---")
        print("Result is:")
        print("---")
        print_matrix(result)
        print()

        if are_equal(user, result):
            print("Success!")

        else:
            print("You are failure!!!")

        print()


def det_excercise() -> None:

    N = 3

    print("### Determinant value ###")

    while True:

        print()
        det = [[random.randint(-5, 5) for j in range(N)] for i in range(N)]
        print_matrix(det)
        print()


        user = int(input("Answer: "))

        if user == calculate_det(det):
            print("Success!")

        else:
            print("You are failure!!!")

        print("Correct answer: ", calculate_det(det))
        print()     


# --- Determinant

def get_dev(m: Matrix, dev_column: int) -> Matrix:
    
    res = []
    for row in range(1, len(m)):

        new = []
        for column in range(len(m[0])):

            if column != dev_column:
                new.append(m[row][column])

        res.append(new)

    return res


def calculate_det(m: Matrix) -> int:

    """
    |a  b|
    |c  d|  ==  ad - bc
    """

    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    res = 0
    for column in range(len(m[0])):

        res += m[0][column] * (-1) ** (column + 1 + 1) * calculate_det(get_dev(m, column))

    return res

# --- Gauss (not finished)
def divide_line(i: int, m: Matrix, const: int) -> None:

    for j in range(len(m[i])):
        m[i][j] /= const

def multiply_line(i: int, m: Matrix, const: int) -> None:

    for j in range(len(m[i])):
        m[i][j] *= const

def add_line(i1: int, i2: int, m: Matrix) -> None:
    
    for j in range(len(m[i1])):
        m[i2][j] -= m[i1][j]


def eliminate(m: Matrix):

    for common in range(min(len(m), len(m[0]))):

        if m[common][common] != 0:
            divide_line(common, m, m[common][common])

        for following in range(common + 1, len(m)):
            
            const = m[following][common]
            if const == 0:
                continue

            multiply_line(common, m, const)
            add_line(common, following, m)
            divide_line(common, m, const)


if __name__ == "__main__":

    # mul_excercise()
    det_excercise()