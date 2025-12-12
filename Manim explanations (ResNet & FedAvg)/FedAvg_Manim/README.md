# FedAvg Explainer – Federated Learning Animation

An animated educational project that explains the Federated Averaging (FedAvg) algorithm using Manim, a Python engine for mathematical animations. The animation tells the "story" of one FedAvg round, from client selection to server aggregation, highlighting why FedAvg is important for federated learning.

## Project Overview

This project creates a single, self-contained animation that walks through:

- **What Federated Averaging is** and why it matters in federated learning
- **Key FedAvg parameters:**
  - `C`: fraction of clients selected per round
  - `E`: number of local epochs
  - `η`: learning rate
  - `T`: number of communication rounds
- **Client selection** and local training on their own data
- **Local gradient computation** and model updates
- **Server aggregation** using the FedAvg formula with weights `n_k / n`
- **Global model improvement** over multiple communication rounds

All of this is implemented in a single Manim scene named `FederatedAveraging`.

## Project Structure

```
FedAvg_Manim/
├── federated_averaging.py    # Main Manim animation script
├── media/                     # Generated outputs (created by Manim)
│   └── videos/
│       └── federated_averaging/
│           └── 480p15/        # Low-quality renders
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

**Note:** You are expected to create your own virtual environment (see Installation below).

## Scene Included

### FederatedAveraging

The main scene that:
- Introduces FedAvg and its importance
- Explains key parameters (C, E, η, T)
- Shows client selection and local training
- Visualizes gradient computation and local model updates
- Animates server aggregation with the FedAvg formula and n_k/n weights
- Concludes with a high-level summary of what FedAvg achieves

## Requirements

- Python 3.10 or 3.11
- Manim Community v0.19.0
- FFmpeg (for video rendering)
- NumPy

These dependencies are listed in `requirements.txt`.

## Installation

### Step 1: Navigate to the project folder

```bash
cd FedAvg_Manim
```

### Step 2: Create a virtual environment

```bash
python -m venv fedavg-env
```

### Step 3: Activate the environment

**Windows (PowerShell):**
```powershell
fedavg-env\Scripts\Activate.ps1
```

**Windows (cmd):**
```cmd
fedavg-env\Scripts\activate.bat
```

**Linux / macOS:**
```bash
source fedavg-env/bin/activate
```

### Step 4: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Verify FFmpeg installation

Ensure FFmpeg is installed and available on your PATH:

```bash
ffmpeg -version
```

This should print version information. If not, install FFmpeg from [ffmpeg.org](https://ffmpeg.org/).

## Usage

All commands below assume:
- You are in the `FedAvg_Manim/` folder
- Your virtual environment (`fedavg-env`) is activated
- `federated_averaging.py` is present

### Render the FedAvg scene (low-quality preview)

```bash
manim -pql federated_averaging.py FederatedAveraging
```

**Flags:**
- `-p`: Play the video after rendering
- `-ql`: Low-quality render (480p15) for fast previews

### Render at higher quality (optional)

For a 1080p60 high-quality version:

```bash
manim -pqh federated_averaging.py FederatedAveraging
```

This will create a new folder:
```
media/videos/federated_averaging/1080p60/
```

### Other quality options

- `-ql`: Low quality (480p15) – fastest
- `-qm`: Medium quality (720p30)
- `-qh`: High quality (1080p60)
- `-qk`: 4K quality (2160p60) – slowest

## Output

Rendered videos are stored in:
```
media/videos/federated_averaging/<quality>/FederatedAveraging.mp4
```

You can:
- Open these `.mp4` files with any video player
- Embed them in slides or reports
- Replace them by re-running the Manim commands after editing the script

## Notes

- This project uses **Manim Community Edition**. See the [official documentation](https://docs.manim.community/) for more flags, resolution settings, and configuration options.
- Rendering time depends on your hardware and chosen quality level.
- The virtual environment (`fedavg-env`) is local to your machine and is **not** included in this repository. Other users should follow the installation steps to set up their own environment.

## Learn More

- [Manim Community Documentation](https://docs.manim.community/)
- [FedAvg Paper](https://arxiv.org/abs/1602.05629) – McMahan et al., 2017
- [Federated Learning Overview](https://federated.withgoogle.com/)

## Contributing

Feel free to modify `federated_averaging.py` to add new scenes, adjust animations, or extend the explanation. After making changes, re-render using the commands above.

## License

This project is provided as-is for educational purposes.