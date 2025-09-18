import pytest

from basic_programs.tictactoe_ai.main import winner, is_full, available_moves, minimax


class TestWinner:
    def test_no_winner_empty_board(self):
        board = [" "] * 9
        assert winner(board) is None

    def test_no_winner_partial_board(self):
        board = ["X", "O", "X", " ", "O", " ", " ", " ", " "]
        assert winner(board) is None

    def test_x_wins_row(self):
        board = ["X", "X", "X", " ", " ", " ", " ", " ", " "]
        assert winner(board) == "X"

    def test_o_wins_column(self):
        board = ["O", " ", " ", "O", " ", " ", "O", " ", " "]
        assert winner(board) == "O"

    def test_x_wins_diagonal(self):
        board = ["X", " ", " ", " ", "X", " ", " ", " ", "X"]
        assert winner(board) == "X"

    def test_o_wins_anti_diagonal(self):
        board = [" ", " ", "O", " ", "O", " ", "O", " ", " "]
        assert winner(board) == "O"


class TestIsFull:
    def test_empty_board_not_full(self):
        board = [" "] * 9
        assert not is_full(board)

    def test_partial_board_not_full(self):
        board = ["X", "O", "X", " ", "O", " ", " ", " ", " "]
        assert not is_full(board)

    def test_full_board(self):
        board = ["X", "O", "X", "O", "X", "O", "O", "X", "O"]
        assert is_full(board)


class TestAvailableMoves:
    def test_empty_board_all_moves(self):
        board = [" "] * 9
        assert available_moves(board) == list(range(9))

    def test_partial_board_some_moves(self):
        board = ["X", " ", "O", " ", "X", " ", " ", " ", " "]
        assert available_moves(board) == [1, 3, 5, 6, 7, 8]

    def test_full_board_no_moves(self):
        board = ["X", "O", "X", "O", "X", "O", "O", "X", "O"]
        assert available_moves(board) == []


class TestMinimax:
    def test_ai_wins(self):
        board = ["O", "O", " ", " ", " ", " ", " ", " ", " "]
        score, move = minimax(board, True, -10, 10)
        assert score == 1
        assert move == 2  # Should block or win

    def test_human_wins(self):
        board = ["X", "X", " ", " ", " ", " ", " ", " ", " "]
        score, move = minimax(board, False, -10, 10)
        assert score == -1

    def test_draw(self):
        board = ["X", "O", "X", "O", "X", "O", "O", "X", " "]
        score, move = minimax(board, True, -10, 10)
        assert score == 0
        assert move == 8
