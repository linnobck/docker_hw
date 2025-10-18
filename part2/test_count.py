import os
import json
import time
from pathlib import Path


# image tag from docker build
IMG_TAG = "linnobck/count_hw:part2"
MAPPER_CONTAINER = "mapper"
REDUCE_CONTAINER = "reduce"
# paths for local and docker
HOST_COUNTS = Path(__file__).parent / "counters"
CONT_COUNTS = "/app/counters"

def start(name, command):
    # stop  old container
    os.system(f"docker rm -f {name} > /dev/null 2>&1")
    # start new one
    os.system(
        f'docker run -d --rm --name {name} '
        f'-v "{HOST_COUNTS.resolve()}:{CONT_COUNTS}:rw" {IMG_TAG} {command}'
    )
    time.sleep(3)

def wait_for_files(path, timeout=30):
    start = time.time()
    while not path.exists():
        if time.time() - start > timeout:
            raise TimeoutError("Reducer output did not appear in time.")
        time.sleep(1)

def test_wordcount():
    # Check counters folder exists, is empty
    os.makedirs(HOST_COUNTS, exist_ok=True)
    for f in HOST_COUNTS.glob("*.json"):
        f.unlink()

    # start 9 mapper containers
    for i in range(1, 10):
        start(f"{MAPPER_CONTAINER}{i}", f"python map.py {i}")

    time.sleep(5)

    # start reducer container
    start(REDUCE_CONTAINER, "python reduce.py")

    #  wait for .json files to finish
    output_file = HOST_COUNTS / "total_counts.json"
    wait_for_files(output_file)

    # check if linux is 16th most common word
    with open(output_file) as f:
        data = list(json.load(f).items())

    linux_at_16 = data[14][0]
    assert linux_at_16.lower() == "linux"
    print(f"linux is the 15th most common word ({data[14]})")

     # cleanup
    os.system(f"docker stop {REDUCE_CONTAINER} > /dev/null 2>&1")
    for i in range(1, 10):
        os.system(f"docker stop {MAPPER_CONTAINER}{i} > /dev/null 2>&1")