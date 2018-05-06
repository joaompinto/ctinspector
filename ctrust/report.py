from __future__ import print_function
import docker
import ctrust.image
import ctrust.layer
from ctrust.colorhelper import info
#from ctrust.utils import print_list

def image_info(image_name):
    docker_client = docker.from_env()
    try:
        image = docker_client.images.get(image_name)
    except docker.errors.ImageNotFound:
        print("Image %s was not found, you can use %s" % (info(image_name), info("--pull")))
        exit(2)
    image_path = ctrust.image.extract(image)
    ctrust.layer.show_info(image_path)

def container_info(container_id):
    print(container_id)
