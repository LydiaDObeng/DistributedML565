# ResNet Explainer - Introduction to Deep Learning Project

An animated educational project that explains ResNet (Residual Networks) functionality using Manim, a Python animation engine for mathematical visualizations.

## Project Overview

This project creates a series of animated scenes that build understanding of ResNet from the ground up:
- **What is a function?** - Introduction to the basic f(x) = y concept
- **Image transformation example** - How a network can sharpen blurry images
- **Network architecture** - Breaking down ResNet into its constituent layers
- **Residual connections** - Understanding why residual connections improve learning

## Project Structure

```
Intro to DL Project/
├── resnet_manim/
│   ├── resnet_explainer.py    # Main animation script with all scenes
│   ├── assets/                # Image assets for animations
│   │   ├── blury.png
│   │   └── normal.png
│   └── media/                 # Generated output directory
│       ├── images/
│       └── videos/
├── media/                     # High-quality video outputs
│   ├── videos/
│   │   └── resnet_explainer/
│   │       ├── 1080p60/
│   │       └── 480p15/
│   └── texts/
├── .venv/                     # Python virtual environment
└── README.md                  # This file
```

## Scenes Included

The `resnet_explainer.py` contains the following animated scenes:

1. **IntroductionScene** - Introduces the concept of functions and the basic x → f → y transformation
2. **ImageExample** - Demonstrates image enhancement (blurry to sharp) as a practical ResNet use case
3. **WhatIsF** - Breaks down a ResNet architecture into its 5 simplified layers (Conv, BN, ReLU, etc.)
4. **ResidualConnection** - Explains skip connections and their role in residual networks
5. **ResidualExplanation** - Deep dive into why residual connections improve training
6. **CNNExample** - Explores how convolutional layers work in image processing

## Requirements

- Python 3.8+
- Manim Community v0.19.0+
- FFmpeg (for video rendering)
- NumPy

## Installation

1. **Clone or navigate to the project:**
   ```bash
   cd "Intro to DL Project"
   ```

2. **Install dependencies:**
   ```bash
   pip install manim numpy
   ```

## Usage

### Render a Single Scene

From the `resnet_manim/` directory, render any scene using Manim:

```bash
# Render ImageExample scene
manim -pql resnet_explainer.py ImageExample

# Render IntroductionScene
manim -pql resnet_explainer.py IntroductionScene

# Render all scenes
manim -pql resnet_explainer.py
```

**Manim flags:**
- `-p` : Play the video after rendering
- `-q` : Quality level (l=low, m=medium, h=high, k=4K)
- `-l` : Low quality (fastest rendering)

### Available Scenes

Run these commands to render specific scenes:

```bash
manim -pql resnet_explainer.py IntroductionScene
manim -pql resnet_explainer.py ImageExample
manim -pql resnet_explainer.py WhatIsF
manim -pql resnet_explainer.py ResidualConnection
manim -pql resnet_explainer.py ResidualExplanation
manim -pql resnet_explainer.py CNNExample
```

## Output

- **Low quality renders**: Saved to `resnet_manim/media/videos/resnet_explainer/480p15/`
- **Medium quality renders**: Saved to `resnet_manim/media/videos/resnet_explainer/1080p60/`
- **High quality renders**: Saved to `resnet_manim/media/videos/resnet_explainer/1440p60/` or higher

Pre-rendered videos at various qualities are stored in the `media/videos/resnet_explainer/` directory.

## Key Concepts Explained

### ResNet (Residual Network)
- Modern deep neural network architecture that uses skip connections
- Allows for training of very deep networks without vanishing gradients
- Key innovation: adding the input directly to the output of a layer

### Components Shown
- **Convolutional Layers (Conv)**: Extract spatial features from images
- **Batch Normalization (BN)**: Stabilizes training by normalizing activations
- **ReLU**: Activation function that introduces non-linearity
- **Skip Connections**: Allow gradients to flow directly, improving learning

## Image Assets

The project uses two sample images for demonstration:
- `assets/blury.png` - Blurry input image
- `assets/normal.png` - Sharp output image (ideal result)

These illustrate how a ResNet can enhance image quality.

## Notes

- All animations use Manim Community edition
- Rendering times vary by quality level and scene complexity
- Videos are cached to speed up re-renders
- The project is designed for educational purposes as part of an Introduction to Deep Learning course
