# Manim Explanations: ResNet & FedAvg

Educational visualizations for understanding Federated Averaging and Residual Networks.

**Choose your learning style:** Interactive web platform or high-quality video animations.

---

## Two Learning Options

### Interactive Web Platform (Quick Start)
**Try it now - No installation required**

- Open in browser instantly
- Control pace with step-by-step progression
- Adjust parameters in real-time
- Dark/Light mode
- Works offline

**[Go to Interactive Platform](Interactive/)**

**Best for:** Quick exploration, parameter testing, hands-on learning

---

### Manim Video Animations (Deep Dive)
**Professional animated explanations**

- High-quality rendered videos
- Polished mathematical visualizations
- Detailed step-by-step walkthroughs
- Perfect for presentations

**[FedAvg Animations](FedAvg_Manim/) | [ResNet Animations](ResNet_Manim/)**

**Best for:** In-depth understanding, video presentations, offline study

---

## Repository Structure

```
Manim explanations (ResNet & FedAvg)/
│
├── Interactive/                        # Interactive Web Platform
│   ├── fedavg-resnet-interactive.html        # Main file (just open it!)
│   └── README.md                          # Usage guide
│
├── FedAvg_Manim/                      # FedAvg Video Animations
│   ├── federated_averaging.py             # Manim script
│   ├── requirements.txt                   # Python dependencies
│   └── README.md                          # Setup & rendering guide
│
└── ResNet_Manim/                      # ResNet Video Animations
    ├── resnet_explainer.py                # Manim script
    ├── assets/                            # Image assets
    └── README.md                          # Setup & rendering guide
```

---

## Quick Start

### Start Learning NOW (30 seconds)

1. Open `Interactive/` folder
2. Download `fedavg-resnet-improved.html`
3. Double-click the file
4. Start exploring

**No installation. No setup. Just learn.**

---

### Professional Video Animations (5 minutes setup)

**For FedAvg:**
```bash
cd FedAvg_Manim
pip install -r requirements.txt
manim -pql federated_averaging.py FederatedAveraging
```

**For ResNet:**
```bash
cd ResNet_Manim
pip install manim numpy
manim -pql resnet_explainer.py ImageExample
```

Full setup instructions: [FedAvg README](FedAvg_Manim/README.md) | [ResNet README](ResNet_Manim/README.md)

---

## What You'll Learn

### Federated Averaging (FedAvg)
- Privacy-preserving distributed machine learning
- How multiple clients train without sharing data
- Key parameters: C (client fraction), E (epochs), η (learning rate)
- Server aggregation with weighted averaging
- Real-world applications: healthcare, mobile devices, finance

### Residual Networks (ResNet)
- Why deep networks have vanishing gradient problems
- How skip connections solve this challenge
- Layer types: Conv, BatchNorm, ReLU, Add
- ResNet architectures: 18, 34, 50, 101, 152 layers
- Image transformation examples

---


## Recommended Learning Path

### For Beginners
1. Start with **Interactive Platform** (FedAvg tab)
2. Experiment with different parameters
3. Watch **FedAvg Manim video** for deeper understanding
4. Return to interactive to solidify learning

### For Visual Learners
1. Watch **Manim animations** first to see the flow
2. Use **Interactive Platform** to explore details
3. Adjust parameters to understand their impact

### For Hands-On Learners
1. Jump into **Interactive Platform** immediately
2. Learn by doing and experimenting
3. Reference **Manim videos** when needed

---

## Technical Requirements

### Interactive Platform
- **Browser:** Any modern browser (Chrome, Firefox, Safari, Edge)
- **Internet:** Not required (works offline)
- **Installation:** None needed
- **File Size:** Single 75KB HTML file

### Manim Animations
- **Python:** 3.10 or 3.11 recommended
- **Manim:** Community Edition v0.19.0+
- **FFmpeg:** Required for rendering
- **OS:** Windows, macOS, or Linux

---

## Documentation

### Interactive Platform
**[Interactive Platform README](Interactive/README.md)**
- How to use the interface
- Parameter explanations
- Control buttons guide
- Troubleshooting

### Manim Animations
**[FedAvg Manim README](FedAvg_Manim/README.md)**
- Installation steps
- Rendering commands
- Scene descriptions
- Quality options

**[ResNet Manim README](ResNet_Manim/README.md)**
- Setup instructions
- Available scenes
- Image assets info
- Output locations

---

## Educational Use

### For Students
- **Interactive:** Self-paced exploration and experimentation
- **Manim:** Watch before class or for exam review
- **Combined:** Best of both worlds

### For Teachers
- **Interactive:** Live classroom demonstrations
- **Manim:** Pre-recorded video assignments
- **Combined:** Flipped classroom approach

### For Researchers
- **Interactive:** Quick parameter testing
- **Manim:** High-quality presentation visuals
- **Combined:** Complete reference toolkit

---

## Features

### Interactive Platform Features
- Step-by-step algorithm walkthrough
- Adjustable parameters with sliders
- Auto-play and manual control modes
- Dark/Light theme toggle
- Color-coded visual elements
- Real-time explanations
- Progress tracking
- Mobile-friendly

### Manim Animation Features
- Professional-quality rendering
- Mathematical precision
- Smooth animations
- Multiple quality levels (480p to 4K)
- Customizable scenes
- Export to video format
- Perfect for presentations

---

## FAQ

**Q: Which should I try first?**  
**A:** Try the Interactive Platform - it's instant and requires no setup.

**Q: Can I use both?**  
**A:** Absolutely! They complement each other perfectly.

**Q: Do I need programming knowledge?**  
**A:** Not for the Interactive Platform. Manim requires basic Python knowledge.

**Q: Can I modify the code?**  
**A:** Yes! Both are open for customization.

**Q: Which is better for presentations?**  
**A:** Manim videos for formal presentations, Interactive for live demos.

**Q: Are they explaining the same concepts?**  
**A:** Yes! Just in different formats to suit different learning styles.

---

## Additional Resources

### Federated Learning
- [FedAvg Paper (McMahan et al., 2017)](https://arxiv.org/abs/1602.05629)
- [Google's Federated Learning](https://federated.withgoogle.com/)

### ResNet
- [ResNet Paper (He et al., 2015)](https://arxiv.org/abs/1512.03385)
- [Deep Residual Learning Explained](https://towardsdatascience.com/introduction-to-resnets-c0a830a288a4)

### Visualization Tools
- [Manim Community Docs](https://docs.manim.community/)

---


## Contributing

Contributions welcome! Suggestions:
- Additional interactive features
- More Manim scenes
- Bug fixes and improvements
- Documentation enhancements

---

## License

Educational use - provided as-is for learning purposes.

---

## Quick Navigation

| Resource | Link |
|----------|------|
| **Interactive Platform** | [Open Now](Interactive/) |
| **Interactive Guide** | [README](Interactive/README.md) |
| **FedAvg Animations** | [Folder](FedAvg_Manim/) |
| **FedAvg Guide** | [README](FedAvg_Manim/README.md) |
| **ResNet Animations** | [Folder](ResNet_Manim/) |
| **ResNet Guide** | [README](ResNet_Manim/README.md) |

---
