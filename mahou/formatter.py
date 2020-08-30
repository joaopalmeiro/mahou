from functools import partial

from black import DEFAULT_LINE_LENGTH, FileMode, format_str
from IPython.core import magic_arguments

# from IPython.core.debugger import set_trace
from IPython.core.magic import Magics, cell_magic, magics_class

from .utils import MagicArgumentDefaultsHelpFormatter


@magics_class
class Formatter(Magics):
    @magic_arguments.magic_arguments()
    @magic_arguments.kwds(
        description="IPython cell magic to format code cells using Black.",
        formatter_class=partial(MagicArgumentDefaultsHelpFormatter, magic_prefix="%%"),
        epilog="For more info about Black, please check: https://github.com/psf/black",
    )
    @magic_arguments.argument(
        "-l",
        "--line-length",
        type=int,
        default=DEFAULT_LINE_LENGTH,
        help="Number of characters allowed per line.",
        dest="line_length",
        metavar="INT",
    )
    @magic_arguments.argument(
        "-S",
        "--skip-string-normalization",
        action="store_true",
        help="Don't normalize string quote marks and prefixes.",
        dest="string_normalization",
    )
    @magic_arguments.argument(
        "-N",
        "--skip-final-newline-character-removal",
        action="store_true",
        help="Don't remove the newline character (`\\n`) at the end of the cell after formatting.",
        dest="final_newline",
    )
    @cell_magic
    def black(self, line, cell):
        args = magic_arguments.parse_argstring(self.black, line)

        # More info about the `--target-version` option: https://github.com/psf/black/issues/751
        mode = FileMode(
            line_length=args.line_length,
            string_normalization=not args.string_normalization,
        )

        formatted_cell = format_str(cell, mode=mode)
        formatted_cell = (
            formatted_cell[:-1]
            if not args.final_newline and formatted_cell and formatted_cell[-1] == "\n"
            else formatted_cell
        )

        self.shell.set_next_input(formatted_cell, replace=True)
