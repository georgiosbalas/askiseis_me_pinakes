import random
def pinakas(size):
    matrix = []
    num = 1
    for i in range(size):
        row = []
        for j in range(size):
            row.append(num)
            num = num + 1
        matrix.append(row)
    return matrix
def ektypwsi_pinaka(matrix):
    for row in matrix:
        print(row)
def athroisma_grammwn(matrix):
    sums = []
    for row in matrix:
        row_sum = 0
        for element in row:
            row_sum = row_sum + element
        sums.append(row_sum)
    return sums  
def athroisma_stilwn(matrix):
    sums = []
    num_columns = len(matrix[0])
    for col in range(num_columns):
        col_sum = 0
        for row in matrix:
            col_sum = col_sum + row[col]
        sums.append(col_sum)
    return sums
def athroisma_diag_1(matrix):
    diagwnios = 0
    for i in range(len(matrix)):
        diagwnios = diagwnios + matrix[i][i]
    return diagwnios
def athroisma_diag_2(matrix):
    diagwnios = 0
    n = len(matrix)
    for i in range(n):
        diagwnios = diagwnios + matrix[i][n-1-i]
    return diagwnios
def tyxaios_pinakas(size, katw_arithmos=1, anw_arithmos=100):
    random_matrix = []
    for q in range(size):
        row = []
        for q in range(size):
            row.append(random.randint(katw_arithmos, anw_arithmos))
        random_matrix.append(row)
    return random_matrix
def ektypwsi_tyxaiou_pinaka(random_matrix):
    for row in random_matrix:
        print(row)
def athroisma_grammwn_tyxaiou(random_matrix):
    sums = []
    for row in random_matrix:
        row_sum = 0
        for element in row:
            row_sum = row_sum + element
        sums.append(row_sum)
    return sums  
def athroisma_stilwn_tyxaiou(random_matrix):
    sums = []
    num_columns = len(random_matrix[0])
    for col in range(num_columns):
        col_sum = 0
        for row in random_matrix:
            col_sum = col_sum + row[col]
        sums.append(col_sum)
    return sums
def athroisma_diag_1_tyxaiou(random_matrix):
    diagwnios = 0
    for i in range(len(random_matrix)):
        diagwnios = diagwnios + random_matrix[i][i]
    return diagwnios
def athroisma_diag_2_tyxaiou(random_matrix):
    diagwnios = 0
    n = len(random_matrix)
    for i in range(n):
        diagwnios = diagwnios + random_matrix[i][n-1-i]
    return diagwnios
    
size = 5

matrix = pinakas(size)
print("Διδιάστατος πίνακας 5Χ5 με στοιχεία 1-25:")
ektypwsi_pinaka(matrix)

athr_grammwn = athroisma_grammwn(matrix)
athr_stilwn = athroisma_stilwn(matrix)
athr_diag_ar_dexia = athroisma_diag_1(matrix)
athr_diag_dexia_ar = athroisma_diag_2(matrix)

print("Άθροισμα ανά γραμμή:", athr_grammwn)
print("Άθροiσμα ανά στήλη:", athr_stilwn)
print("Άθροισμα διαγωνίου από αριστερά προς τα δεξιά:", athr_diag_ar_dexia)
print("Άθροισμα διαγωνίου από δεξιά προς τα αριστερά:", athr_diag_dexia_ar)

random_matrix = tyxaios_pinakas(size)
print("Διδιάστατος τυχαίος 5Χ5 πίνακας:")
ektypwsi_tyxaiou_pinaka(random_matrix)

athr_grammwn_rand = athroisma_grammwn_tyxaiou(random_matrix)
athr_stilwn_rand = athroisma_stilwn_tyxaiou(random_matrix)
athr_diag_ar_dexia_rand = athroisma_diag_1_tyxaiou(random_matrix)
athr_diag_dexia_ar_rand = athroisma_diag_2_tyxaiou(random_matrix)


print("Άθροισμα ανά γραμμή για τον τυχαίο πίνακα:", athr_grammwn_rand)
print("Άθροισμα ανά στήλη για τον τυχαίο πίνακα:", athr_stilwn_rand)
print("Άθροισμα διαγωνίου από αριστερά προς τα δεξιά για τον τυχαίο πίνακα:", athr_diag_ar_dexia_rand)
print("Άθροισμα διαγωνίου από δεξιά προς τα αριστερά για τον τυχαίο πίνακα:", athr_diag_dexia_ar_rand)