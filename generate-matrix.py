import json

def read_matrix_file(filename):
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            values = line.strip().split(',')
            matrix.append({values[i]: values[i + 1] for i in range(0, len(values), 2)})
    return matrix

matrix = read_matrix_file('matrix.txt')
print(json.dumps(matrix))