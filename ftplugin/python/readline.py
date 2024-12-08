"""HACK: Workaround for ``readline`` scrambling pyflakes-vim terminal with Python 3.13+.

As of 2024-12-07, using pyflakes-vim with Python 3.13 causes vim to emit garbage
characters, scrambling the terminal output and making vim unusable.

The cause has been tracked down to a chain of imports:
    flaker -> pyflakes.checker -> doctest -> pdb -> rlcompleter -> readline

For some strange reason, importing the `readline` package is what suddenly causes the
terminal output to be scrambled.  Fortunately the `rlcompleter` library surrounds the
``import readline`` with a ``try``/``except ImportError`` to gracefully handle
nonexistence of :mod:`readline`.

Because ``pyflakes.vim`` reconfigures ``sys.path`` so that this directory takes
precedence, having a ``readline.py`` file here that simply raises :class:`ImportError`
ensures that the real :mod:`readline` isn't imported, and thus avoiding the terminal-
scrambling landmines.

Note:
    The extent of the :mod:`readline` problem with pyflakes-vim / Python 3.13+ isn't
    clear because it's only been observed on an M1 MacBook Pro with vim installed via
    Homebrew, so this hack might not be necessary on other platforms - YMMV.

See `kkroening/pyflakes-vim#3`_.

.. _kkroening/pyflakes-vim#3:
    https://github.com/kkroening/pyflakes-vim/pull/3
"""

raise ImportError(
    'readline import disabled to avoid scrambling terminal output in pyflakes-vim.'
)
