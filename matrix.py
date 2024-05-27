import numpy as np

# 파일 경로
file_path = 'test.emb'


def extract_vec(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    num_vectors, dim = map(int, lines[0].strip().split())

    node_vectors = []

    for line in lines[1:]:
        parts = line.strip().split()
        node = parts[0]
        vector = list(map(float, parts[1:]))
        node_vectors.append((node, vector))

    # 노드를 오름차순으로 정렬
    node_vectors.sort()

# 정렬된 벡터를 추출하여 행렬 생성
    matrix = np.array([vector for _, vector in node_vectors])
    index = np.array([index for index, _ in node_vectors])

    return matrix, index 

matrix, _ = extract_vec(file_path)
print(matrix)