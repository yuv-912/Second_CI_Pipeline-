"""Program 39: Transpose a Matrix."""


def transpose_matrix(matrix):
    """Transpose a 2D matrix (swap rows and columns)."""
    if not matrix or not matrix[0]:
        return []
    rows = len(matrix)
    cols = len(matrix[0])
    return [[matrix[r][c] for r in range(rows)] for c in range(cols)]


if __name__ == "__main__":
    m = [[1, 2, 3], [4, 5, 6]]
    print("Original:", m)
    print("Transposed:", transpose_matrix(m))
