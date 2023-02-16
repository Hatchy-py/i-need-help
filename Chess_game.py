import chess
import os

board = chess.Board()

def center_board(board_str):
    screen_width = os.get_terminal_size().columns
    board_lines = board_str.splitlines()
    max_line_width = max(len(line) for line in board_lines)
    padding_width = (screen_width - max_line_width) // 2
    padding = ' ' * padding_width
    centered_lines = [padding + line + padding for line in board_lines]
    centered_board_str = '\n'.join(centered_lines)
    return centered_board_str

def print_board(board):
    clear_screen()
    board_str = str(board)
    centered_board_str = center_board(board_str)
    print("                                         A B C D E F G H")
    print("                                         _______________")
    print(centered_board_str)
    print("                                         _______________")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def is_move_legal(move, board):
    if move in board.legal_moves:
        return True
    else:
        return False

def chess_game():
    while True:
        print_board(board)
        print("type help to see moves ")
        move_str = input("choose your move: ")
        if move_str == "help":
            legal_moves = list(board.legal_moves)
            print(legal_moves)
        else:
            move = chess.Move.from_uci(move_str)
            if is_move_legal(move, board):
                board.push(move)
            else:
                print("illegal move !")

chess_game()
