"""Pyglish related-errors."""


class FileDoesNotEndWithPYG(Exception):
    """Files should end with .pyg in order to be compiled by pyglish."""
    pass
