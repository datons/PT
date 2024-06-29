#!/bin/bash

# Create the environment
mamba env create -f environment.yml

# Activate the environment
source activate llm

# Install IPython kernel
python -m ipykernel install --user --name llm --display-name "Python (LLM)"
