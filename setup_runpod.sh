#!/bin/bash
# Setup script for RFdiffusion and ProteinMPNN on Ubuntu with CUDA/RunPod

echo "Updating system and installing dependencies..."
apt-get update && apt-get install -y git wget cuda-command-line-tools-11-7

# Install Miniconda if not present
if ! command -v conda &> /dev/null
then
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
    bash miniconda.sh -b -p $HOME/miniconda
    export PATH="$HOME/miniconda/bin:$PATH"
    conda init
fi

# Clone and setup RFdiffusion
echo "Setting up RFdiffusion..."
git clone https://github.com/RosettaCommons/RFdiffusion.git
cd RFdiffusion
conda env create -f env/SE3nv.yml
conda activate SE3nv
pip install -e .
mkdir weights
wget http://files.ipd.uw.edu/pub/rf_diffusion/6f5902ac2370aa4dda0a36be5a86ed8b/Base_weights.pt -O weights/Base_weights.pt

# Clone and setup ProteinMPNN
echo "Setting up ProteinMPNN..."
cd ..
git clone https://github.com/dauparas/ProteinMPNN.git

echo "Setup complete. Ready for BioForge Phase 2 execution."
