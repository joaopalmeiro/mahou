from argparse import ArgumentDefaultsHelpFormatter

from IPython.core.magic_arguments import MagicHelpFormatter


class MagicArgumentDefaultsHelpFormatter(
    MagicHelpFormatter, ArgumentDefaultsHelpFormatter
):
    """
    More info:

    - IPython: https://github.com/ipython/ipython/blob/master/IPython/core/magic_arguments.py#L65
    - argparse (`HelpFormatter`): https://github.com/python/cpython/blob/3.8/Lib/argparse.py#L154
    - argparse (`ArgumentDefaultsHelpFormatter`): https://github.com/python/cpython/blob/3.8/Lib/argparse.py#L679

    Check if inheritance is as expected:

    import inspect
    inspect.getmro(MagicArgumentDefaultsHelpFormatter)
    inspect.getmembers(MagicArgumentDefaultsHelpFormatter, predicate=inspect.isfunction)
    """

    def __init__(
        self,
        prog,
        indent_increment=2,
        max_help_position=24,
        width=None,
        magic_prefix="%",
    ):
        super().__init__(
            prog=prog,
            indent_increment=indent_increment,
            max_help_position=max_help_position,
            width=width,
        )

        self.magic_prefix = magic_prefix

    def add_usage(self, usage, actions, groups, prefix="::\n\n  "):
        super(MagicArgumentDefaultsHelpFormatter, self).add_usage(
            usage, actions, groups, f"{prefix}{self.magic_prefix}"
        )
