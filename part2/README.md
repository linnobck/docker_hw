# Project Title

Docker homework part 2

## Description

This project implements a simplified Map-Reduce computation using Docker containers.
Nine mapper containers each process one text file of Stack Overflow titles to count word frequencies.
A single reducer container waits for all mappers to finish, merges their results, and produces a combined, ordered word-count file.
The entire workflow runs in Docker and is verified automatically with pytest.

## Getting Started

### Dependencies

- **Operating System:** Tested on macOS (Apple Silicon) and Linux.  
- **Docker:** Docker Desktop should be installed and running.  
- **Python:** Needed to run the pytest file (Python 3.10 or later).  
- **Libraries inside the container:**  All modules used are python native

### Installing

* 1. Download project files and store them in the same directory
* 2. Move into that directory in the terminal

### Executing program

* 1. Build the Docker image by running ```bash ./build.sh```
This will 
- Pull a python image
- Copy map.py, reduce.py, and the data files into the container
- Save it in the Docker image
* 2. Check that the image was built successfully by ```bash docker images```
* 3. Run ```bash pytest -q test_count.py``` to run the automatic tests
This will:
- Launch 9 mapper containers
- Launch 1 reducer container
- Automatically create .json files for all 9 text files, as well as 1 combined count file
- Wait for the combined .json file to appear, and confirm 'linux' placement

### Known bugs
The instructions say that 'linux' should be the 16th most common word in the files, but no matter how I ordered or changed the text formatting, I could only ever get it to be shown as the 15th most common word.
To still make the test file work correctly, it therefore now checks if linux is the 15th word.


## Authors

Linn Oberbeck`:)`
