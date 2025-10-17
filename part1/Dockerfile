# use  official python image as base image
FROM python:3.12-slim

# working dir inside container
WORKDIR /app

COPY pt_train.py pt_classify.py /app/

# install basic tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# install pytorch, torchvision, ...
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir \
        torch torchvision pillow numpy --index-url https://download.pytorch.org/whl/cpu

# run training script
# download MNIST and train model
RUN python pt_train.py

# keep container running after start
CMD ["tail", "-f", "/dev/null"]