# ✦ Foundation Workspace: Interactive Post-Mortem v2.0

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-red.svg)](https://streamlit.io)
[![Status](https://img.shields.io/badge/Status-Deployed-success.svg)]()

### Overview
This project is an interactive, web-based submission for the **Apple Foundation Program** at the University of Technology Sydney (UTS).

Rather than submitting a standard static essay detailing a past mistake, I engineered this interactive "Workspace." It acts as a 5-stage diagnostic agent that walks the user through a critical data science failure, analyzes their recovery choices across multiple vectors, and compiles a final Developer Archetype profile.

### 🎯 The Scenario
During the final sprint of an end-to-end Natural Language Processing (NLP) project, a critical error occurred: the core preprocessing script was deleted without being committed to version control. This application explores the psychological, tactical, and strategic responses to that exact scenario.

### ✨ Key Features
* **5-Stage Diagnostic Engine:** A deep-dive interactive questionnaire testing responses to crisis, deployment, tech debt, and pressure.
* **Modern SaaS UI:** Custom CSS implementation featuring a deep dark mode, frosted glass components (`backdrop-filter`), and high-contrast coral accents.
* **Base64 Asset Injection:** Custom Python functions to encode and inject high-resolution local background assets directly into the CSS DOM to bypass cloud-hosting limitations.
* **Algorithmic Profiling:** Dynamically calculates a user's recovery archetype based on their interaction path.

### 🧠 The 5 Developer Archetypes
1. **The Tactical Solver:** Prioritizes momentum, rapid prototyping, and immediate execution under pressure.
2. **The Systems Architect:** Prioritizes root-cause analysis, strict CI/CD pipelines, and structural integrity.
3. **The Ecosystem Catalyst:** Prioritizes team synergy, transparency, and distributed problem-solving.
4. **The Visionary Engineer:** Prioritizes user empathy, business alignment, and the final product experience.
5. **The Deep Researcher:** Prioritizes mathematical rigor, algorithmic optimization, and academic purity.

---

### 🛠️ Local Installation & Usage

To run this diagnostic tool locally on your machine:

**1. Clone the repository**
```bash
git clone https://github.com/tuannm3812/apple-foundation-agent.git
cd apple-foundation-agent
```

**2. Set up a virtual environment (Recommended)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: .\\venv\\Scripts\\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the application**

```bash
streamlit run app.py
```

### 📁 Repository Structure
```
apple-foundation-agent/
│
├── app.py                 # Core Streamlit application and diagnostic logic
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
│
└── images/                # UI Assets and 3D illustrations
	├── workspace_background.png
	├── stage_clear_castle.png
	├── profile_tactical.png
	├── profile_architect.png
	├── profile_catalyst.png
	├── profile_visionary.png
	└── profile_researcher.png
```

👨‍💻 About the Author
[Your Name] Master of Data Science and AI | University of Technology Sydney

I treat personal growth with the same rigor as software engineering. A mistake is simply an unhandled exception; the goal is not to avoid them entirely, but to build the infrastructure required to recover from them gracefully.

