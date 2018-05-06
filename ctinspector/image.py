from __future__ import print_function
import tarfile
import json
from os.path import join, exists
from os import makedirs
from shutil import move
from tempfile import gettempdir, NamedTemporaryFile, mkdtemp
from ctinspector.utils import print_list

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


def show_info(image_content_path):
    with open(join(image_content_path, 'manifest.json')) as manifest_file:
        manifest_data = manifest_file.read()
    image_manifest = json.loads(manifest_data)
    for manifest_item in image_manifest:
        config_fn = manifest_item['Config']
        with open(join(image_content_path, config_fn)) as config_file:
            config_data = config_file.read()
            manifest_item_config = json.loads(config_data)
            original_cmd = manifest_item_config['config']['Cmd'][:]
            manifest_item_config['config']['Cmd'] = ' '.join(original_cmd)
            print_list("Config", manifest_item_config['config'])
