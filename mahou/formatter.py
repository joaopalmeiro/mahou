from black import format_str
from IPython.core import magic_arguments
from IPython.core.magic import Magics, cell_magic, magics_class


@magics_class
class Formatter(Magics):
    @cell_magic
    def black(self, line, cell):
        pass
