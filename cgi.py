"""
cgi shim for Python 3.13+
Provides minimal replacements for removed functions.
"""

from urllib.parse import parse_qs

def parse_header(line):
    """
    In old cgi, parse_header() returned (main_value, params_dict).
    We'll fake it: just return the line itself and an empty dict.
    """
    return line, {}

def parse_multipart(fp, pdict):
    """
    Old cgi supported multipart parsing. We don’t need it here.
    If called, raise an error.
    """
    raise NotImplementedError("cgi.parse_multipart is not available in this shim.")
