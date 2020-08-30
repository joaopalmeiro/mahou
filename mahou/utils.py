from argparse import ArgumentDefaultsHelpFormatter

from IPython.core.magic_arguments import MagicHelpFormatter
from IPython.utils.text import dedent


class MagicArgumentDefaultsHelpFormatter(
    MagicHelpFormatter, ArgumentDefaultsHelpFormatter
):
    """
    More info:

    - IPython: https://github.com/ipython/ipython/blob/master/IPython/core/magic_arguments.py#L65
    - argparse: https://github.com/python/cpython/blob/3.8/Lib/argparse.py#L679

    Check if inheritance is as expected:

    import inspect
    inspect.getmro(MagicArgumentDefaultsHelpFormatter)
    inspect.getmembers(MagicArgumentDefaultsHelpFormatter, predicate=inspect.isfunction)
    """

    def add_usage(self, usage, actions, groups, prefix="teste"):
        super(MagicArgumentDefaultsHelpFormatter, self).add_usage(
            usage, actions, groups, prefix
        )
