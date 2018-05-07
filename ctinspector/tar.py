import tarfile
from os.path import join, exists
from os import makedirs
from tempfile import gettempdir, NamedTemporaryFile, mkdtemp
from shutil import move

def extract_image(image):
    image_cache_prefix = join(gettempdir(), "ctinspector", "image.cache")
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
        for member in image_tar.getmembers():
            image_tar.extract(member, tmp_dir)
        move(tmp_dir, image_cache_path)

    return image_cache_path

def extract_layer(image_content_path, layer_path):
    cache_prefix = join(gettempdir(), "ctinspector", "layer.cache")
    cache_path = join(cache_prefix, layer_path)
    if not exists(cache_prefix):
        makedirs(cache_prefix, 0o700)

    # Image is not yet cached, save and extract it
    if not exists(cache_path):
        tarfile.os.mknod = lambda x, y, z: 0  # Monkey patch mknod because some layers include devices
        image_tar = tarfile.open(join(image_content_path, layer_path))
        tmp_dir = mkdtemp()
        image_tar.extractall(tmp_dir)
        move(tmp_dir, cache_path)

    return cache_path
