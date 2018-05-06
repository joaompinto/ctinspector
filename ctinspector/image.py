from __future__ import print_function
import tarfile
from os.path import join, exists
from os import makedirs
from shutil import move
from tempfile import gettempdir, NamedTemporaryFile, mkdtemp


def extract(image):
    image_cache_prefix = join(gettempdir(), "ctinspector", "image-cache")
    image_cache_path = join(image_cache_prefix, image.id)
    if not exists(image_cache_prefix):
        makedirs(image_cache_prefix, 0o700)

    # Image is not yet cached, save and extract it
    if not exists(image_cache_path):
        with NamedTemporaryFile(delete=False) as tmp_filename:
            for chunk in image.save():
                tmp_filename.write(chunk)
        image_tar = tarfile.open(tmp_filename.name)
        tmp_dir = mkdtemp()
        image_tar.extractall(tmp_dir)
        move(tmp_dir, image_cache_path)

    return image_cache_path
