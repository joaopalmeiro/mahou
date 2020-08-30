from black import FileMode, format_str
from IPython.core import magic_arguments
from IPython.core.magic import Magics, cell_magic, magics_class


@magics_class
class Formatter(Magics):
    @cell_magic
    def black(self, line, cell):
        mode = FileMode()

        formatted_cell = format_str(cell, mode=mode)
        formatted_cell = (
            formatted_cell[:-1]
            if formatted_cell and formatted_cell[-1] == "\n"
            else formatted_cell
        )

        self.shell.set_next_input(formatted_cell, replace=True)
