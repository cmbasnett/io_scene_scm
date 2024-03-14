import ctypes

from .data import ScmData
from typing import BinaryIO
from ctypes import c_char, c_int32


def read_scm(stream: BinaryIO) -> ScmData:

    class ScmHeader(ctypes.Structure):
        _fields_ = [
            ('magic', c_char * 4),
            ('version', c_int32),
            ('model_type', c_int32),
            ('resource_path', c_char * 256),
            ('export_path', c_char * 256),
        ]

    scm = ScmData()
    return scm