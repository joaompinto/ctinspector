from __future__ import print_function
import docker
import ctinspector.tar
import ctinspector.image
import ctinspector.layer
from ctinspector.colorhelper import info, print_info
#from ctinspect.utils import print_list

def image_info(image_name):
    docker_client = docker.from_env()
    try:
        image = docker_client.images.get(image_name)
    except docker.errors.ImageNotFound:
        print("Image %s was not found, you can use:\n    docker pull %s" % (info(image_name), info(image_name)))
        exit(2)
    print_info("Id:", image.id)
    image_path = ctinspector.tar.extract_image(image)
    ctinspector.image.show_info(image_path, image.id)

def container_info(container_id):
    print(container_id)
