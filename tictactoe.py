from typing import List, Tuple, Optional
from enum import Enum
from dataclasses import dataclass


class GameState(Enum):
    IN_PROGRESS = "in_progress"
    X_WINS = "x_wins"
    O_WINS = "o_wins"
    DRAW = "draw"


class Player(Enum):
    X = "X"
    O = "O"
    
    def opponent(self) -> 'Player':
        return Player.O if self == Player.X else Player.X


@dataclass(frozen=True)
class Position:
    row: int
    col: int
    
    def is_valid(self, board_size: int = 3) -> bool:
        return 0 <= self.row < board_size and 0 <= self.col < board_size


class Board:
    EMPTY_CELL = ' '
    BOARD_SIZE = 3
    
    def __init__(self):
        self._grid: List[List[str]] = [
            [self.EMPTY_CELL] * self.BOARD_SIZE 
            for _ in range(self.BOARD_SIZE)
        ]
    
    def get_cell(self, position: Position) -> str:
        return self._grid[position.row][position.col]
    
    def set_cell(self, position: Position, value: str) -> None:
        self._grid[position.row][position.col] = value
    
    def is_empty(self, position: Position) -> bool:
        return self.get_cell(position) == self.EMPTY_CELL
    
    def is_full(self) -> bool:
        return all(
            self._grid[i][j] != self.EMPTY_CELL 
            for i in range(self.BOARD_SIZE) 
            for j in range(self.BOARD_SIZE)
        )
    
    def get_winner(self) -> Optional[Player]:
        for player in Player:
            if self._check_win(player.value):
                return player
        return None
    
    def _check_win(self, symbol: str) -> bool:
        return (
            self._check_rows(symbol) or 
            self._check_columns(symbol) or 
            self._check_diagonals(symbol)
        )
    
    def _check_rows(self, symbol: str) -> bool:
        return any(
            all(self._grid[i][j] == symbol for j in range(self.BOARD_SIZE))
            for i in range(self.BOARD_SIZE)
        )
    
    def _check_columns(self, symbol: str) -> bool:
        return any(
            all(self._grid[j][i] == symbol for j in range(self.BOARD_SIZE))
            for i in range(self.BOARD_SIZE)
        )
    
    def _check_diagonals(self, symbol: str) -> bool:
        main_diagonal = all(
            self._grid[i][i] == symbol 
            for i in range(self.BOARD_SIZE)
        )
        anti_diagonal = all(
            self._grid[i][self.BOARD_SIZE - 1 - i] == symbol 
            for i in range(self.BOARD_SIZE)
        )
        return main_diagonal or anti_diagonal
    
    def display(self) -> str:
        lines = ['\n']
        for i, row in enumerate(self._grid):
            lines.append(' | '.join(row))
            if i < self.BOARD_SIZE - 1:
                lines.append('-' * (self.BOARD_SIZE * 4 - 1))
        lines.append('\n')
        return '\n'.join(lines)


class InputHandler:
    @staticmethod
    def get_move(player: Player, board: Board) -> Position:
        while True:
            try:
                user_input = input(
                    f"Player {player.value}, enter row and column (1-3, 1-3): "
                )
                position = InputHandler._parse_input(user_input)
                
                if not position.is_valid():
                    print("Position out of bounds. Try again.")
                    continue
                
                if not board.is_empty(position):
                    print("Cell already occupied. Try again.")
                    continue
                
                return position
            except ValueError as e:
                print(f"Invalid input: {e}. Try again.")
    
    @staticmethod
    def _parse_input(user_input: str) -> Position:
        parts = user_input.replace(',', ' ').split()
        if len(parts) != 2:
            raise ValueError("Enter exactly two numbers")
        
        row = int(parts[0]) - 1
        col = int(parts[1]) - 1
        return Position(row, col)


class TicTacToeGame:
    def __init__(self):
        self._board = Board()
        self._current_player = Player.X
        self._state = GameState.IN_PROGRESS
    
    def play(self) -> None:
        print("Welcome to Tic Tac Toe")
        print(self._board.display())
        
        while self._state == GameState.IN_PROGRESS:
            self._execute_turn()
            print(self._board.display())
            self._update_state()
        
        self._display_result()
    
    def _execute_turn(self) -> None:
        position = InputHandler.get_move(self._current_player, self._board)
        self._board.set_cell(position, self._current_player.value)
    
    def _update_state(self) -> None:
        winner = self._board.get_winner()
        
        if winner == Player.X:
            self._state = GameState.X_WINS
        elif winner == Player.O:
            self._state = GameState.O_WINS
        elif self._board.is_full():
            self._state = GameState.DRAW
        else:
            self._current_player = self._current_player.opponent()
    
    def _display_result(self) -> None:
        if self._state == GameState.X_WINS:
            print("Player X wins!")
        elif self._state == GameState.O_WINS:
            print("Player O wins!")
        elif self._state == GameState.DRAW:
            print("It's a draw!")


def main() -> None:
    game = TicTacToeGame()
    game.play()


if __name__ == '__main__':
    main()
