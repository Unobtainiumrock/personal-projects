ARG IMAGE_NAME=nvidia/cuda
ARG CUDA_VERSION=12.2
ARG CUDNN_VERSION=8.8
ARG TENSORFLOW_VERSION=2.15.0
ARG PYTHON_VERSION=3.9
ARG BAZEL_VERSION=6.1.0

FROM ${IMAGE_NAME}:${CUDA_VERSION}.1-base-ubuntu22.04 as base

ENV NV_CUDA_LIB_VERSION ${CUDA_VERSION}.1-1
ENV NV_CUDNN_VERSION ${CUDNN_VERSION}.1.3-1+cuda${CUDA_VERSION}

FROM base as base-amd64

# CUDA environment variables
ENV NV_LIBNPP_VERSION ${CUDA_VERSION}.2.3-1
ENV NV_LIBNPP_PACKAGE libnpp-${CUDA_VERSION}=${NV_LIBNPP_VERSION}
ENV NV_LIBCUSPARSE_VERSION ${CUDA_VERSION}.0.103-1
ENV NV_LIBCUBLAS_VERSION ${CUDA_VERSION}.4.1-1
ENV NV_LIBCUBLAS_PACKAGE libcublas-${CUDA_VERSION}=${NV_LIBCUBLAS_VERSION}
ENV NV_LIBNCCL_VERSION 2.19.3-1+cuda${CUDA_VERSION}
ENV NV_LIBNCCL_PACKAGE libnccl2=${NV_LIBNCCL_VERSION}

FROM base as base-arm64

# Repeat CUDA environment variables for ARM64 if necessary

FROM base-${TARGETARCH}

ARG TARGETARCH

LABEL maintainer "NVIDIA CORPORATION <cudatools@nvidia.com>"
	
# Install system packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    cuda-libraries-${CUDA_VERSION}=${NV_CUDA_LIB_VERSION} \
    ${NV_LIBNPP_PACKAGE} \
    cuda-nvtx-${CUDA_VERSION}=${NV_NVTX_VERSION} \
    libcusparse-${CUDA_VERSION}=${NV_LIBCUSPARSE_VERSION} \
    ${NV_LIBCUBLAS_PACKAGE} \
    ${NV_LIBNCCL_PACKAGE} \
    libcudnn8=${NV_CUDNN_VERSION} \
    && rm -rf /var/lib/apt/lists/*

# Prevent auto upgrades of cuBLAS and NCCL
RUN apt-mark hold libcublas-${CUDA_VERSION} libnccl2

# Install Python and pip
RUN apt-get update && apt-get install -y --no-install-recommends \
    python${PYTHON_VERSION} \
    python${PYTHON_VERSION}-dev \
    python${PYTHON_VERSION}-distutils \
    python3-pip \
    && ln -s $(which python${PYTHON_VERSION}) /usr/local/bin/python3 \
    && ln -s $(which python${PYTHON_VERSION}) /usr/local/bin/python \
    && pip3 install --no-cache-dir --upgrade pip setuptools

# Install Bazel
RUN apt-get install -y --no-install-recommends wget && \
    wget https://github.com/bazelbuild/bazel/releases/download/${BAZEL_VERSION}/bazel-${BAZEL_VERSION}-installer-linux-x86_64.sh && \
    chmod +x bazel-${BAZEL_VERSION}-installer-linux-x86_64.sh && \
    ./bazel-${BAZEL_VERSION}-installer-linux-x86_64.sh

# Install TensorFlow GPU
RUN pip3 install --no-cache-dir tensorflow-gpu==${TENSORFLOW_VERSION}

# Confirm that TensorFlow can access the GPU
RUN python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"

# Add entrypoint items
COPY entrypoint.d/ /opt/nvidia/entrypoint.d/
COPY nvidia_entrypoint.sh /opt/nvidia/
ENV NVIDIA_PRODUCT_NAME="CUDA"
ENTRYPOINT ["/opt/nvidia/nvidia_entrypoint.sh"]

