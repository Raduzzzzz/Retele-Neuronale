import pathlib
import math



#1
def load_system(path: pathlib.Path) -> tuple[list[list[float]], list[float]]:
    A = []
    B = []
    row =[]
    with open(path, "r") as f:
        for line in f:
            row = []
            curr_line = line.strip()
            l, r = curr_line.split("=")
            B.append(float(r))
            lista = l.split()
            sem = 1
            for i in lista:
                if i == "+":
                    sem =1
                elif i == "-":
                    sem = -1
                else:
                    if i[:-1] == "":
                        rez = float(sem)
                    else:
                        rez = float(i[:-1])*sem
                    row.append(rez)
            A.append(row)
    return A,B


A, B = load_system(pathlib.Path("system.txt"))
print(f"{A=} {B=}")




#2.1
def determinant(matrix: list[list[float]]) -> float:
    a = matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2]*matrix[2][1])
    b = matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2]*matrix[2][0])
    c = matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1]*matrix[2][0])

    return a - b + c


print(f"{determinant(A)=}")

#2.2
def trace(matrix: list[list[float]]) -> float:
    return matrix[0][0] + matrix[1][1] + matrix[2][2]


print(f"{trace(A)=}")

#2.3

def norm(vector: list[float]) -> float:

    return math.sqrt(vector[0] ** 2 + vector[1] ** 2 +vector[2] ** 2)

print(f"{norm(B)=}")

#2.4
def transpose(matrix: list[list[float]]) -> list[list[float]]:
    trans =[]
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[0])):
            row.append(matrix[j][i])
        trans.append(row)
    return trans
print(f"{transpose(A)=}")

#2.5

def multiply(matrix: list[list[float]], vector: list[float]) -> list[float]:
    rezultat = []
    for row in matrix:
        val = row[0] * vector[0] + row[1] * vector[1] + row[2] * vector[2]
        rezultat.append(val)
    return rezultat

print(f"{multiply(A, B)=}")

#3
def Aj_creater(matrix: list[list[float]], vector: list[float], a) -> list[list[float]]:
    Ax = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[0])):
            if a == j:
                row.append(vector[i])
            else:
                row.append(matrix[i][j])
        Ax.append(row)
    return Ax

def solve_cramer(matrix: list[list[float]], vector: list[float]) -> list[float]:
    x = determinant(Aj_creater(matrix,vector,0)) / determinant(matrix)
    y = determinant(Aj_creater(matrix,vector,1)) / determinant(matrix)
    z = determinant(Aj_creater(matrix,vector,2)) / determinant(matrix)
    return [x, y, z]

print(f"{solve_cramer(A, B)=}")


#4

def minor(matrix: list[list[float]], i: int, j: int) -> list[list[float]]:
    M = []
    for a in range(len(matrix)):
        if a == i:
            continue
        row = []
        for b in range(len(matrix[0])):
            if b != j:
                row.append(matrix[a][b])
        M.append(row)
    return M


def det2x2(m: list[list[float]]) -> float:
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]


def cofactor(matrix: list[list[float]]) -> list[list[float]]:
    C = []
    for a in range(len(matrix)):
        row = []
        for b in range(len(matrix[0])):
            val = ((-1) ** (a + b)) * det2x2(minor(matrix, a, b))
            row.append(val)
        C.append(row)
    return C


def adjoint(matrix: list[list[float]]) -> list[list[float]]:
    Aa = transpose(cofactor(matrix))
    return Aa


def solve(matrix: list[list[float]], vector: list[float]) -> list[float]:
    Aa = adjoint(matrix)
    det = determinant(matrix)

    A_inv = []
    for i in range(len(Aa)):
        row = []
        for j in range(len(Aa[0])):
            row.append(Aa[i][j] / det)
        A_inv.append(row)

    X = multiply(A_inv, vector)
    return X


print(f"{solve(A, B)=}")