
We process muon data, compute invariant masses of 4-muon combinations, and visualize candidate events near the Higgs boson mass (~125 GeV).

---

## 📁 Dataset

- **Source**: Public ROOT data from CERN Open Data Portal  
- **File**: `ZZTo4mu.root`  
- **Content**: Muon 4-vectors (pt, eta, phi, mass), charge, and event structure

---

## 🧪 Analysis Pipeline

✅ Load ROOT file using `uproot`  
✅ Filter events with 4–6 muons  
✅ Form all valid 4-muon charge-neutral combinations  
✅ Reconstruct Z boson pairs  
✅ Calculate 4-muon **invariant mass**  
✅ Store Higgs candidates and plot the mass distribution

---

## 📊 Sample Plot

*4-muon invariant mass showing Higgs candidates around 125 GeV:*

![image](https://github.com/user-attachments/assets/92dda4db-9182-4ce6-9f41-455a9560bbf6)


---

## 🧠 Concepts Used

- Lorentz invariance of mass (special relativity)
- Four-vector kinematics
- Invariant mass calculations
- Particle decay reconstruction
- Real scientific data processing

---

## 🛠 Tools & Libraries

- Python 🐍  
- `uproot`, `awkward`, `vector`, `numpy`, `matplotlib`, `pandas`  
- CMS ROOT data

---

## 📦 Running the Code

```bash
# Install dependencies (you can use pip or conda)
pip install uproot awkward vector pandas matplotlib
Install the root data file and keep in the same folder as code
# Run the main analysis
python higgs_detection_2.py

# View the plot
python visualize.py
