import os
import random
import time
from pathlib import Path

# image tag from docker build
IMG_TAG = "linnobck/docker_hw:part1"
CONTAINER_NAME = "pt_mnist"
# paths for local and docker
HOST_IMG = Path(__file__).parent / "images"
CONT_IMG = "/app/images"


def start():
    # stop  old container
    os.system(f"docker rm -f {CONTAINER_NAME} > /dev/null 2>&1")
    # start new one
    os.system(
        f'docker run -d --rm --name {CONTAINER_NAME} '
        f'-v "{HOST_IMG.resolve()}:{CONT_IMG}:ro" {IMG_TAG}'
    )
    time.sleep(3)

def stop():
    os.system(f"docker stop {CONTAINER_NAME} > /dev/null 2>&1")

def get_prediction(output):
    for ch in output:
        if ch.isdigit():
            return int(ch)
    return -1

def test_infer():
    # if no image folder
    if not HOST_IMG.exists():
        raise Exception("Image folder missing")

    images = list(HOST_IMG.glob("*.png"))
    
    sample = random.sample(images, min(3, len(images)))
    start()
    try:
        for img in sample:
            # run classifier in container
            cmd = f"docker exec {CONTAINER_NAME} python pt_classify.py --input {CONT_IMG}/{img.name}"
            stream = os.popen(cmd)
            output = stream.read()
            gt = int(img.name[0])
            pred = get_prediction(output)
            print(f"{img.name} -> got {pred} (expected {gt})")
            assert gt == pred
    finally:
        stop()