# ID 64131193
def solution(keys, matrix, players_count=2, symbols='123456789'):
    return sum(
        0 < matrix.count(symbol) <= keys * players_count
        for symbol in symbols
    )


if __name__ == "__main__":
    print(
        solution(
            keys=int(input()),
            matrix=f'{input()}{input()}{input()}{input()}'
        )
    )
