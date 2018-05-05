from __future__ import print_function
import docker
import image_driver
from colorhelper import info, print_info


def print_list(label, items):
    if not items:
        return
    print("%s:" % label)
    for item in items:
        print_info("\t"+item)


def image(image_name):
    client = docker.from_env()
    try:
        image = client.images.get(image_name)
    except docker.errors.ImageNotFound:
        print("Image %s was not found, you can use %s" % (info(image_name), info("--pull")))
        exit(2)
    print_info("Id: ", image.id)
    print_list("Tags", image.tags)
    print_list("Labels", image.labels)
    image_driver.show_info(image.attrs['GraphDriver'])


def container(container_id):
    print(container_id)
