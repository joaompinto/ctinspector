from __future__ import print_function
import json
import ctinspector.layer
from os.path import join
from ctinspector.utils import print_list

def show_info(image_content_path, image_id):
    image_id = image_id.split(":")[1]
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
            created_by_list = []
            for history in manifest_item_config['history']:
                for created_by in history['created_by'].split("\t"):
                    created_by = created_by.strip("\n")
                    if created_by:
                        created_by_list.append(created_by)
            print_list("Build History", created_by_list)
        for layer in manifest_item['Layers']:
            ctinspector.layer.show_info(image_content_path, layer)
