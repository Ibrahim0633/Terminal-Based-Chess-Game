def create_board():
    return [
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
    ]

def print_board(board):
    print("\n    a   b   c   d   e   f   g   h")
    print("  +---------------------------------+  BLACK (lowercase: p, r, n, b, q, k)")
    for i in range(8):
        row_str = f"{8 - i} |"
        for j in range(8):
            row_str += f" {board[i][j]} |"
        print(row_str + f" {8 - i}")
        print("  +---------------------------------+")
    print("    a   b   c   d   e   f   g   h    WHITE (uppercase: P, R, N, B, Q, K)\n")

def parse_coordinate(coord):
    try:
        if len(coord) != 2:
            return None
        col = ord(coord[0].lower()) - ord('a')
        row = 8 - int(coord[1])
        if 0 <= col < 8 and 0 <= row < 8:
            return row, col
    except:
        pass
    return None

def is_valid_move(board, start_row, start_col, end_row, end_col, turn):
    piece = board[start_row][start_col]
    target = board[end_row][end_col]

    if turn == 'White' and not piece.isupper():
        print("It is White's turn! Select your own piece.")
        return False
    if turn == 'Black' and not piece.islower():
        print("It is Black's turn! Select your own piece.")
        return False

    if target != '.':
        if turn == 'White' and target.isupper():
            print("Cannot capture your own piece!")
            return False
        if turn == 'Black' and target.islower():
            print("Cannot capture your own piece!")
            return False

    if piece.lower() == 'p':
        direction = -1 if turn == 'White' else 1
        if start_col == end_col:
            if end_row - start_row == direction and target == '.':
                return True
            if (turn == 'White' and start_row == 6 and end_row == 4 and board[5][start_col] == '.' and target == '.'):
                return True
            if (turn == 'Black' and start_row == 1 and end_row == 3 and board[2][start_col] == '.' and target == '.'):
                return True
        elif abs(start_col - end_col) == 1 and end_row - start_row == direction:
            if target != '.':
                return True
        return False

    return True

def main():
    board = create_board()
    turn = 'White'
    
    print("=== TERMINAL CHESS ===")
    print("White is at the bottom (Rows 1-2, Uppercase)")
    print("Black is at the top (Rows 7-8, Lowercase)")
    print("Enter moves using notation like 'e2 e4'. Type 'leave' to forfeit or 'exit' to quit.\n")
    
    while True:
        print_board(board)
        print(f"Turn: {turn}")
        move_input = input("Enter move (e.g. e2 e4): ").strip()
        
        if move_input.lower() == 'leave':
            winner = 'Black' if turn == 'White' else 'White'
            print(f"\n{turn} has left the match. {winner} wins by forfeit!")
            break

        if move_input.lower() == 'exit':
            print("Exiting game.")
            break
            
        parts = move_input.split()
        if len(parts) != 2:
            print("Invalid format! Use two coordinates separated by space, e.g., 'e2 e4'.")
            continue
            
        start = parse_coordinate(parts[0])
        end = parse_coordinate(parts[1])
        
        if not start or not end:
            print("Invalid coordinates! Must be within a1-h8.")
            continue
            
        start_row, start_col = start
        end_row, end_col = end
        
        piece = board[start_row][start_col]
        if piece == '.':
            print("No piece at the selected square!")
            continue
            
        if is_valid_move(board, start_row, start_col, end_row, end_col, turn):
            board[end_row][end_col] = piece
            board[start_row][start_col] = '.'
            turn = 'Black' if turn == 'White' else 'White'
        else:
            print("Invalid move, try again.")

if __name__ == "__main__":
    main()