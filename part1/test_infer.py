import re
import random
import subprocess
import time
from pathlib import Path

# image tag from docker build
IMG_TAG = "linnobck/docker_hw:part1"
CONTAINER_NAME = "pt_mnist"
# paths for local and docker
HOST_IMG = Path(__file__).parent / "images"
CONT_IMG = "/app/images"

def start():
    # stop old container
    subprocess.run(["docker", "rm", "-f", CONTAINER_NAME], check=False)
    #start new container
    subprocess.run([
        "docker", "run", "-d", "--rm",
        "--name", CONTAINER_NAME,
        "-v", f"{HOST_IMG.resolve()}:{CONT_IMG}:ro",
        IMG_TAG
    ])
    time.sleep(2)

def stop():
    subprocess.run(["docker", "stop", CONTAINER_NAME], check=False)

def test_infer():
    # if no image folder
    if not HOST_IMG.exists():
        raise Exception("Image folder is missing")

    images = list(HOST_IMG.glob("*.png"))
    sample = random.sample(images, min(3, len(images)))
    start()
    try:
        for img in sample:
            # run classification in container
            result = subprocess.run(
                ["docker", "exec", CONTAINER_NAME, "python", "pt_classify.py",
                 "--input", f"{CONT_IMG}/{img.name}"],
                capture_output=True, text=True
            )
            gt = int(img.name[0])
            m = re.search(r"(\d)", result.stdout)
            pred = int(m.group(1)) if m else -1
            print(f"{img.name} -> got {pred} (expected {gt})")
            assert gt == pred
    finally:
        stop()