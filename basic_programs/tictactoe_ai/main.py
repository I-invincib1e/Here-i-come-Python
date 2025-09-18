from __future__ import annotations

from typing import List, Optional, Tuple

Board = List[str]


def print_board(board: Board) -> None:
    def cell(i: int) -> str:
        return board[i] if board[i] != " " else str(i + 1)

    print(f" {cell(0)} | {cell(1)} | {cell(2)}")
    print("---+---+---")
    print(f" {cell(3)} | {cell(4)} | {cell(5)}")
    print("---+---+---")
    print(f" {cell(6)} | {cell(7)} | {cell(8)}\n")


def winner(board: Board) -> Optional[str]:
    lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
        (0, 4, 8), (2, 4, 6),             # diagonals
    ]
    for a, b, c in lines:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_full(board: Board) -> bool:
    return all(c != " " for c in board)


def available_moves(board: Board) -> List[int]:
    return [i for i, c in enumerate(board) if c == " "]


def minimax(board: Board, is_maximizing: bool, alpha: int, beta: int) -> Tuple[int, Optional[int]]:
    win = winner(board)
    if win == "O":
        return 1, None
    if win == "X":
        return -1, None
    if is_full(board):
        return 0, None

    if is_maximizing:
        best_score = -10
        best_move: Optional[int] = None
        for move in available_moves(board):
            board[move] = "O"
            score, _ = minimax(board, False, alpha, beta)
            board[move] = " "
            if score > best_score:
                best_score, best_move = score, move
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score, best_move
    else:
        best_score = 10
        best_move = None
        for move in available_moves(board):
            board[move] = "X"
            score, _ = minimax(board, True, alpha, beta)
            board[move] = " "
            if score < best_score:
                best_score, best_move = score, move
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score, best_move


def human_turn(board: Board) -> None:
    while True:
        choice = input("Choose position (1-9): ").strip()
        if not choice.isdigit():
            print("Enter a number 1-9.")
            continue
        idx = int(choice) - 1
        if idx < 0 or idx > 8 or board[idx] != " ":
            print("Invalid move. Try again.")
            continue
        board[idx] = "X"
        break


def ai_turn(board: Board) -> None:
    _, move = minimax(board, True, -10, 10)
    assert move is not None
    board[move] = "O"


def game() -> None:
    board: Board = [" "] * 9
    print("Tic Tac Toe - You (X) vs AI (O)\n")
    print_board(board)
    while True:
        human_turn(board)
        print_board(board)
        if winner(board) == "X":
            print("You win! 🎉")
            return
        if is_full(board):
            print("It's a draw.")
            return

        print("AI thinking...")
        ai_turn(board)
        print_board(board)
        if winner(board) == "O":
            print("AI wins!")
            return
        if is_full(board):
            print("It's a draw.")
            return


if __name__ == "__main__":
    game()


