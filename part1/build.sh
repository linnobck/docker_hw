#!/usr/bin/env bash

set -e

GITHUB_USER="linnobck"

IMAGE_TAG="${GITHUB_USER}/docker_hw:part1"

echo "Building Docker image: ${IMAGE_TAG}"

docker build -t "${IMAGE_TAG}" .

echo "Image saved as: ${IMAGE_TAG}"