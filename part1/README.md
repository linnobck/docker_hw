# Project Title

Docker homework part 1

## Description

This project trains a simple MNIST digit classifier inside a Docker image using PyTorch.  
After training, the image can be run as a container to test or classify images anywhere, without needing to set up the environment again.

## Getting Started

### Dependencies

- **Operating System:** Tested on macOS (Apple Silicon) and Linux.  
- **Docker:** Docker Desktop should be installed and running.  
- **Python:** Needed to run the pytest file (Python 3.10 or later).  
- **Libraries inside the container:**  
  The Dockerfile automatically installs everything needed, e.g.: `torch`,`torchvision` and `numpy.

### Installing

* 1. Download project files and store them in the same directory
* 2. Move into that directory in the terminal

### Executing program

* 1. Build the Docker image by running ```bash ./build.sh```
This will 
- Pull a python image
- Install all dependencies
- Train the MNIST model
- Save it in the Docker image
* 2. Check that the image was built successfully by ```bash docker images```
* 3. Next, run ```bash docker run -d --rm --name pt_mnist \ -v "$(pwd)/images:/app/images:ro" \linnobck/docker_hw:part1```
  This builds the container and puts the image inside
  The provided `build.sh` script will automatically build the Docker image (`linnobck/docker_hw:part1`) from the included Dockerfile.
* 4. Run ```bash docker ps and see pt_mnist listed```
* 5. Optional: In the terminal run ```bash docker exec pt_mnist python pt_classify.py --input /app/images/....png``` to manually test
Replace ... with any image from your images folder.
* 6. Run ```bash docker stop pt_mnist``` to stop the container

* To test everything automatically, run ```bash pytest -q test_infer.py```


## Authors

Linn Oberbeck`:)`
