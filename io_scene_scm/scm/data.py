from ctypes import Structure, c_char, c_int32, c_uint8, c_float, c_uint32, c_uint16
from typing import List


class Color(Structure):
    _fields_ = [
        ('r', c_uint8),
        ('g', c_uint8),
        ('b', c_uint8),
    ]


class ScmSkin(object):
    def __init__(self):
        self.name = ""
        self.palette = [Color() for _ in range(256)]
        self.width = 0
        self.height = 0
        self.data = bytearray()


class ScmSkin(Structure):
    _fields_ = [
        ('name', c_char * 32),
        ('palette', Color * 256),
        ('width', c_int32),
        ('height', c_int32),
    ]


class ScmTriangle(object):
    def __init__(self):
        pass


class ScmSkeletalVertexPart(Structure):
    _fields_ = [
        ('position', c_float * 3),  # Position relative to joint.
        ('joint_index', c_uint8),
        ('weight', c_uint8),
    ]


class ScmSkeletalVertex(Structure):
    _fields_ = (
        ('parts', ScmSkeletalVertexPart * 2),
    )


class ScmPolyGroup(Structure):
    _fields_ = [
        ('skin_index', c_uint16),
        ('flags', c_uint32),
        ('damage_joint_index', c_uint8),
        ('name', c_char * 32),
    ]


class ScmPlane(Structure):
    _fields_ = [
        ('normal', c_float * 3),
        ('distance', c_float),
    ]


class ScmJoint(Structure):
    _fields_ = [
        ('name', c_char * 32),
        ('parent_index', c_int32),
        ('child_indices', c_int32 * 4),
        ('group', c_int32),
        ('flags', c_uint32),
        ('collision_box_planes', ScmPlane * 6),
    ]


class ScmMesh(object):
    def __init__(self):
        self.name = ''
        self.triangles: List[ScmTriangle] = []
        self.vertices: List[ScmSkeletalVertex] = []
        self.poly_groups: List[ScmPolyGroup] = []


class ScmSequence(Structure):
    _fields_ = [
        ('name', c_char * 32),
        ('frame_start', c_uint32),
        ('frame_count', c_uint32),
        ('frame_rate', c_float),
        ('is_normalized', c_uint8),
        ('compressed_length', c_uint32),
        # data here
    ]


class ScmData(object):
    def __init__(self):
        self.skins: List[ScmSkin] = []
        self.meshes: List[ScmMesh] = []
        self.joints: List[ScmJoint] = []
        self.events: List[str] = []
        self.sequences: List[ScmSequence] = []
