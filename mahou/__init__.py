from .formatter import Formatter

__package_name__ = "mahou"
__version__ = "0.1.0"
__author__ = "João Palmeiro"
__author_email__ = "jm.palmeiro@campus.fct.unl.pt"
__description__ = "A package full of tricks... sorry, full of IPython magic commands."
__url__ = "https://github.com/joaopalmeiro/mahou"


def load_ipython_extension(ipython):
    ipython.register_magics(Formatter)
