bl_info = {
    'name': 'SuperCoolModel (SCM) Importer/Exporter',
    'author': 'Colin Basnett',
    'version': (0, 1, 0),
    'blender': (4, 0, 0),
    'description': 'SCM Import/Export (.scm)',
    'warning': '',
    'doc_url': 'https://github.com/DarklightGames/io_scene_scm',
    'tracker_url': 'https://github.com/DarklightGames/io_scene_scm/issues',
    'category': 'Import-Export'
}

if 'bpy' in locals():
    import importlib

    importlib.reload(scm_data)
    importlib.reload(scm_reader)
else:
    from .scm import data as scm_data
    from .scm import reader as scm_reader

import bpy

classes = tuple()  # TODO: populate with classes from other modules


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == '__main__':
    register()
