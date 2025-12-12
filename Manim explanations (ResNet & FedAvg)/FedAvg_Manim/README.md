# FedAvg Explainer – Federated Learning Project

An animated educational project that explains the Federated Averaging (FedAvg) algorithm using Manim, a Python engine for mathematical animations. The animation tells the “story” of one FedAvg round, from client selection to server aggregation, and highlights why FedAvg is important for federated learning. [web:22][web:32]

---

## Project Overview

This project creates a single, self‑contained animation that walks through:

- What Federated Averaging is and why it matters in federated learning. [web:21][web:30]
- The key FedAvg parameters:  
  - \(C\): fraction of clients selected per round  
  - \(E\): number of local epochs  
  - \(\eta\): learning rate  
  - \(T\): number of communication rounds [web:23]
- Client selection and local training on their own data.
- Local gradient computation and model updates.
- Aggregation at the server using the FedAvg formula with weights \(n_k / n\).
- How the global model improves over multiple communication rounds.

All of this is implemented in a single Manim scene named `FederatedAveraging`.

---

## Project Structure

After unzipping, you should see something like:

FedAvg_Manim/
├── federated_averaging.py # Main Manim animation script (FederatedAveraging scene)
├── media/ # Generated outputs (created/updated by Manim)
│ └── videos/
│ └── federated_averaging/
│ └── 480p15/ # Existing low‑quality render(s)
├── requirements.txt # Python dependencies for this project
└── README.md # This file


You are expected to create **your own** virtual environment (see below); 

---

## Scene Included

`federated_averaging.py` defines one main scene:

1. **FederatedAveraging**  
   - Introduces FedAvg and its importance.  
   - Explains key parameters \(C, E, \eta, T\).  
   - Shows client selection and local training.  
   - Visualizes gradient computation and local model updates.  
   - Animates server aggregation with the FedAvg formula and \(n_k/n\) weights.  
   - Concludes with a high‑level summary of what FedAvg achieves.

---

## Requirements

- Python 3.10 or 3.11
- Manim Community v0.19.0
- FFmpeg (for video rendering)
- NumPy [web:17][web:22]

These are listed in `requirements.txt`.

---

## Installation – Create Your Own Virtual Environment

You will create and manage your own environment.

1. **Navigate to the project folder:**

cd "FedAvg_Manim"


2. **Create a virtual environment (example: `fedavg-env`):**

python -m venv fedavg-env


3. **Activate the environment:**

- **Windows (PowerShell)**

  ```
  fedavg-env\Scripts\Activate.ps1
  ```

- **Windows (cmd)**

  ```
  fedavg-env\Scripts\activate.bat
  ```

- **Linux / macOS**

  ```
  source fedavg-env/bin/activate
  ```

4. **Install dependencies inside the environment:**

pip install -r requirements.txt


5. **Ensure FFmpeg is installed** and available on your PATH (so `ffmpeg -version` prints version info in a terminal). [web:21]

---

## Usage

All commands below assume:

- You are in the `FedAvg_Manim/` folder.
- Your virtual environment (`fedavg-env`) is activated.
- `federated_averaging.py` is present.

### Render the FedAvg scene (low‑quality preview)

manim -pql federated_averaging.py FederatedAveraging


- `-p` : Play the video after rendering.
- `-q l` : Low‑quality render (`480p15`) for fast previews.

Because this project currently only includes low‑quality outputs, this is the default quality used.

### Render at higher quality (optional)

If you want to generate a higher quality version (e.g., 1080p60), you can run:

manim -pqh federated_averaging.py FederatedAveraging


On first use, this will create a new folder such as:

media/videos/federated_averaging/1080p60/


and write a higher‑resolution `FederatedAveraging.mp4` there. [web:17]

---

## Output

Existing low‑quality renders are stored in:


New renders will appear in the appropriate subfolder based on the quality flag you choose (`480p15`, `1080p60`, etc.).

You can:

- Open these `.mp4` files with any video player.
- Embed them in slides or reports.
- Replace them by re‑running the Manim commands after editing the script.

---

## Notes

- This project uses Manim Community Edition; see the official documentation for more flags, resolution settings, and configuration options. [web:19]
- Rendering time depends on your hardware and chosen quality level.
- The virtual environment (`fedavg-env`) you create is local to your machine and is **not** included in this submission; other users should follow the same steps to set up their own environment.


