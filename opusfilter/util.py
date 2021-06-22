"""Utility functions"""

import bz2
import gzip
import io
import lzma
import os

import ruamel.yaml


def file_open(filename, mode='r', encoding='utf8'):
    """Open file with implicit gzip/bz2 support

    Uses text mode by default regardless of the compression.

    In write mode, creates the output directory if it does not exist.

    """
    if 'w' in mode and not os.path.isdir(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))
    if filename.endswith('.bz2'):
        if mode in {'r', 'w', 'x', 'a'}:
            mode += 't'
        return bz2.open(filename, mode=mode, encoding=encoding)
    if filename.endswith('.xz'):
        if mode in {'r', 'w', 'x', 'a'}:
            mode += 't'
        return lzma.open(filename, mode=mode, encoding=encoding)
    if filename.endswith('.gz'):
        if mode in {'r', 'w', 'x', 'a'}:
            mode += 't'
        return gzip.open(filename, mode=mode, encoding=encoding)
    return open(filename, mode=mode, encoding=encoding)


yaml = ruamel.yaml.YAML()


def yaml_dumps(obj):
    """Return a string containing YAML output from input object"""
    with io.StringIO() as iostream:
        yaml.dump(obj, iostream)
        iostream.seek(0)
        return iostream.read()
