"""Kinda module documentation"""

from arrays import Array2D


class LifeGrid:
    """
    Implements the LifeGrid ADT for use with the Game of Life.
    """
    DEAD_CELL = 0
    LIVE_CELL = 1

    def __init__(self, num_rows, num_cols):
        """
        Creates the game grid and initializes the cells to dead.
        :param num_rows: the number of rows.
        :param num_cols: the number of columns.
        """
        self._grid = Array2D(num_rows, num_cols)
        self.configure(list())

    def num_rows(self):
        """
        Returns the number of rows in the grid.
        :return: the number rows in the grid.
        """
        return self._grid.num_rows()

    def num_cols(self):
        """
        Returns the number of columns in the grid.
        :return:Returns the number of columns in the grid.
        """
        return self._grid.num_cols()

    def configure(self, coord_list):
        """
        Configures the grid to contain the given live cells.

        :param coord_list:
        :return:
        """
        for i in range(self.num_rows()):
            for j in range(self.num_cols()):
                self._grid[i, j] = 1 if (i, j) in coord_list else 0

    def is_live_cell(self, row, col):
        """
        Does the indicated cell contain a live organism?

        :param row: row of the cell.
        :param col: column of the cell.
        :return: the result of check.
        """
        return bool(self._grid[row, col])

    def clear_cell(self, row, col):
        """
        Clears the indicated cell by setting it to dead.
        :param row: row of the cell.
        :param col: column of the cell.
        """
        self._grid[row, col] = 0

    def set_cell(self, row, col):
        """
        Sets the indicated cell to be alive.
        :param row: row of the cell.
        :param col: column of the cell.
        """
        self._grid[row, col] = 1

    def num_live_neighbors(self, row, col):
        """
        Returns the number of live neighbors for the given cell.
        :param row: row of the cell.
        :param col: column of the cell.
        :return:
        """
        n = 0
        try:
            if self.is_live_cell(row+1, col):
                n += 1
        except AssertionError:
            pass
        try:
            if self.is_live_cell(row-1, col):
                n += 1
        except AssertionError:
            pass
        try:
            if self.is_live_cell(row, col+1):
                n += 1
        except AssertionError:
            pass
        try:
            if self.is_live_cell(row, col-1):
                n += 1
        except AssertionError:
            pass
        try:
            if self.is_live_cell(row-1, col-1):
                n += 1
        except AssertionError:
            pass
        try:
            if self.is_live_cell(row+1, col-1):
                n += 1
        except AssertionError:
            pass
        try:
            if self.is_live_cell(row-1, col+1):
                n += 1
        except AssertionError:
            pass
        try:
            if self.is_live_cell(row+1, col+1):
                n += 1
        except AssertionError:
            pass
        return n

    def __str__(self):
        """
        Returns string representation of LifeGrid
        in form of:
        DDLDD
        DLDLD
        DLDLD
        DDLDD
        DDDDD
        Where D - dead cell, L - live cell
        """
        return "\n".join("".join("L" if self.is_live_cell(i, j) else "D"
                                 for j in range(self.num_cols()))
                         for i in range(self.num_rows()))
