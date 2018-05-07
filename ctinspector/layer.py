from __future__ import print_function
import os
import re
import ctinspector.tar
from os.path import dirname, basename, join, getsize, exists
from ctinspector.utils import print_list, human_size


def show_info(image_content_path, layer_path):
    info_dict = {}
    layer_id = basename(dirname(layer_path))[:12]
    layer_full_path = join(image_content_path, layer_path)
    info_dict["Size"] = ('%s' % human_size(getsize(layer_full_path)))
    layer_tar = ctinspector.tar.extract_layer(image_content_path, layer_path)
    file_count = 0
    dir_count = 0
    dir_list = []
    file_list = []
    base_len = len(layer_tar)
    for root, dirs, files in os.walk(layer_tar, topdown=False):
        relevant_root = root[base_len:]
        for name in files:
            file_list.append(relevant_root+"/"+name)
            file_count += 1
        # Skip when dir is parent of a previously found dir
        for name in dirs:
            dir_name = relevant_root+"/"+name
            must_add = True
            for i in file_list:
                if i.startswith(dir_name):
                    must_add = False
                    break
            for i in dir_list:
                if i.startswith(dir_name):
                    must_add = False
                    break
            if must_add:
                dir_list.append(dir_name)
                dir_count += 1
    if file_count <= 10:
        info_dict["Files"] = ' '.join(file_list)
    else:
        info_dict["File Count"] = file_count
    if dir_count <= 10:
        info_dict["Dirs"] = ' '.join(dir_list)
    else:
        info_dict["Dir Count"] = dir_count

    info_dict["Distro"] = identify_distro(layer_tar)

    print_list("Layer %s" % layer_id, info_dict)

def identify_distro(layer_path):
    distro_map = {
        'os-release' : ['etc/os-release', r'^NAME="([^"]+)', r'^VERSION_ID="?([\w\.]+)']
        }
    for detection_type, items in distro_map.items(): # pylint: disable=W0612
        (file_name, name_regex, version_regex) = items
        full_file_name = join(layer_path, file_name)
        if exists(full_file_name):
            with open(full_file_name) as release_file:
                release_data = release_file.read()
            name = re.findall(name_regex, release_data, re.MULTILINE)
            if name:
                name = name[0]
                version = re.findall(version_regex, release_data, re.MULTILINE)
                if version:
                    name += " "+version[0]
            return name
    return None
