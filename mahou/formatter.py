from black import DEFAULT_LINE_LENGTH, FileMode, format_str
from IPython.core import magic_arguments
from IPython.core.debugger import set_trace
from IPython.core.magic import Magics, cell_magic, magics_class


@magics_class
class Formatter(Magics):
    @magic_arguments.magic_arguments()
    @magic_arguments.argument(
        "-l",
        "--line-length",
        type=int,
        default=DEFAULT_LINE_LENGTH,
        help="Number of characters allowed per line.",
        dest="line_length",
    )
    @magic_arguments.argument(
        "-S",
        "--skip-string-normalization",
        action="store_true",
        help="Don't normalize string quote marks and prefixes.",
        dest="string_normalization",
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
            if formatted_cell and formatted_cell[-1] == "\n"
            else formatted_cell
        )

        self.shell.set_next_input(formatted_cell, replace=True)
