# Interactive FedAvg & ResNet Explainer

Interactive web-based visualizations for understanding Federated Averaging and Residual Networks.

**No installation required - just open and explore!**

---

## Quick Start

1. **Download** `fedavg-resnet-improved.html`
2. **Double-click** to open in your browser
3. **Start learning!**

That's it! Works offline, no setup needed.

---

## Using the Platform

### Navigation
Click the **tabs at the top** to switch between:
- **Federated Averaging** - Distributed machine learning
- **ResNet Architecture** - Deep neural networks with skip connections

### Basic Controls
- **Start** - Begin visualization
- **Next Step** - Advance one step (recommended for learning)
- **Auto Play** - Automatic progression (2-second intervals)
- **Reset** - Start over

### Theme Toggle
Click the **moon/sun icon** in the top-right corner to switch between dark and light modes.

---

## Federated Averaging Tab

### How to Use
1. Adjust parameters in the left sidebar (optional)
2. Click **"Start Algorithm"**
3. Use **"Next Step"** to go through each phase
4. Read explanations at the bottom

### Key Parameters
- **Client Fraction (C)** - Percentage of clients selected (default: 60%)
- **Local Epochs (E)** - Training rounds per client (default: 5)
- **Learning Rate (η)** - How fast model learns (default: 0.01)
- **Number of Clients** - Total devices in federation (default: 6)
- **Communication Rounds (T)** - Total training rounds (default: 10)

### What You'll Learn
How multiple devices (phones, hospitals, banks) train a shared model without sharing their private data.

**Real Examples:**
- Hospitals training on medical images (MIMIC-CXR)
- Phones improving keyboards
- Banks detecting fraud

---

## ResNet Architecture Tab


### How to Use
1. Click **"Start Forward Pass"**
2. Use **"Next Layer"** to see each transformation
3. Watch the active layer glow
4. Observe value changes in the grid

### Understanding the Grid
The **"Current Values"** grid shows how data transforms through each layer:
- Numbers show actual values at each step
- Darker blue = higher values
- Watch: Input → Conv → BatchNorm → ReLU → Output

### What You'll Learn
How ResNet uses skip connections to train very deep networks (100+ layers).

**ResNet Variants:**
- **ResNet-18** - 18 layers, fast for experiments
- **ResNet-50** - 50 layers, most popular
- **ResNet-152** - 152 layers, highest accuracy

---

### Common Questions

**Q: Parameters won't change?**  
A: Click Reset first, then adjust them before starting.

**Q: Too fast?**  
A: Use "Next Step" instead of Auto Play for better control.

**Q: What do colors mean?**  
A: Check the Legend section in the left sidebar.

**Q: What are "Current Values"?**  
A: They show data transforming through ResNet layers - watch the numbers change!

---

## What You'll Learn

### Federated Averaging
- Privacy-preserving machine learning
- How distributed training works
- Server aggregation with weighted averaging
- Impact of different parameters

### ResNet
- Why deep networks have gradient problems
- How skip connections solve it
- What each layer type does
- Why ResNet enables 100+ layer networks

---

## Troubleshooting

**Platform not working?**
- Use Chrome, Firefox, Safari, or Edge (recent version)
- Enable JavaScript in browser settings
- Try refreshing the page (F5)

**Canvas blank?**
- Resize browser window
- Switch tabs and come back
- Reload the page

**Buttons disabled?**
- Click Reset button
- Reload if needed

---

## Want More? Try Manim Animations

For **professional video explanations** with high-quality animations:

**[FedAvg Manim Animations](../FedAvg_Manim/)** - Detailed FedAvg walkthrough  
**[ResNet Manim Animations](../ResNet_Manim/)** - Complete ResNet explanation

**Why try both?**
- **Interactive** = Hands-on exploration
- **Manim** = Polished video presentations
- **Together** = Complete understanding

[Back to Main README](../README.md)

---

## Additional Resources

**Learn More:**
- [FedAvg Paper (McMahan et al., 2017)](https://arxiv.org/abs/1602.05629)
- [ResNet Paper (He et al., 2015)](https://arxiv.org/abs/1512.03385)
- [Manim Community](https://docs.manim.community/)

---

## Features

- No installation required
- Works in any modern browser
- Completely offline-capable
- Dark/Light mode
- Step-by-step control
- Real-time parameter adjustment
- Interactive visualizations
- Detailed explanations
- Mobile-friendly design

---

## Technical Details

- **File Size:** Single 75KB HTML file
- **Technology:** HTML5, CSS3, Vanilla JavaScript
- **Libraries:** None (zero dependencies)
- **Browser:** Chrome, Firefox, Safari, Edge (2020+)
- **Internet:** Not required (works offline)

---

## Start Learning Now

**3 steps to begin:**

1. Open `fedavg-resnet-improved.html`
2. Choose a tab (FedAvg or ResNet)
3. Click Start and explore!

**Recommended first steps:**
- Try **FedAvg** with default parameters
- Use **Manual mode** (Next Step)
- Read each explanation carefully
- Then experiment with different settings

---
