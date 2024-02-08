print("Hola Mundo")








def solve_n_queens(n):
    def is_safe(board, row, col):
        # Verificar si hay una reina en la misma columna
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # Verificar si hay una reina en la misma diagonal hacia arriba a la izquierda
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        
        # Verificar si hay una reina en la misma diagonal hacia arriba a la derecha
        i = row - 1
        j = col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        
        return True

    def backtrack(board, row):
        if row == n:
            # Se encontró una solución, imprimir el tablero
            for i in range(n):
                print(' '.join(board[i]))
            print()
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                backtrack(board, row + 1)
                board[row][col] = '.'
    
    # Inicializar el tablero
    board = [['.' for _ in range(n)] for _ in range(n)]
    backtrack(board, 0)

# Ejemplo de uso
n = 4
solve_n_queens(n)

