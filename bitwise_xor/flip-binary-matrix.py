def flip_and_invert_image(matrix):
    for row in matrix:
        row.reverse()
        for i in range(len(row)):
            row[i] = row[i] ^ 1

    return matrix


if __name__ == '__main__':
    print(flip_and_invert_image([
        [1, 0, 1],
        [1, 1, 1],
        [0, 1, 1]
    ]))
    # [
    #   [0,1,0],
    #   [0,0,0],
    #   [0,0,1]
    # ]
    print(flip_and_invert_image([
        [1, 1, 0, 0],
        [1, 0, 0, 1],
        [0, 1, 1, 1],
        [1, 0, 1, 0]
    ]))
    # [
    #   [1,1,0,0],
    #   [0,1,1,0],
    #   [0,0,0,1],
    #   [1,0,1,0]
    # ]
