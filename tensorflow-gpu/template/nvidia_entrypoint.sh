#!/bin/bash

# Check if the NVIDIA SMI tool is available and the GPU is accessible
if ! command -v nvidia-smi &> /dev/null || ! nvidia-smi &> /dev/null; then
    echo "NVIDIA SMI tool is not available or the NVIDIA GPU is not accessible."
    echo "Please ensure that the NVIDIA drivers are installed and the GPU is accessible."
    exit 1
fi

echo "NVIDIA GPU is accessible."

# Set NVIDIA-related environment variables
export NVIDIA_VISIBLE_DEVICES=all
export NVIDIA_DRIVER_CAPABILITIES=compute,utility

# Execute any initialization scripts in entrypoint.d
if [ -d "/opt/nvidia/entrypoint.d/" ]; then
    for script in /opt/nvidia/entrypoint.d/*.sh; do
        if [ -x "$script" ]; then
            echo "Running $script..."
            . "$script"
        else
            echo "Skipping $script, not executable."
        fi
    done
else
    echo "No entrypoint.d directory found, skipping initialization scripts."
fi

# Execute the main container command
exec "$@"

