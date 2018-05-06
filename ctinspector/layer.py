from __future__ import print_function
import json
from os.path import join
from ctinspector.utils import print_list

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
