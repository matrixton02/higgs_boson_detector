import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("higgs_candidates.csv")
higs_candidate = df["Higgs_mass"]

plt.hist(higs_candidate, bins=50, range=(100, 150), histtype='step', color='blue', label='4μ invariant mass')

higgs_mass = 125
tolerance = 2
plt.axvline(x=higgs_mass, color='red', linestyle='--', label=f'Higgs mass ({higgs_mass} GeV)')
plt.axvspan(higgs_mass - tolerance, higgs_mass + tolerance, color='yellow', alpha=0.5, label=f'Peak region ±{tolerance} GeV')

plt.xlabel("4-Muon Invariant Mass [GeV]")
plt.ylabel("Events")
plt.title("Higgs → ZZ → 4μ Candidate (with Higgs region highlighted)")
plt.grid(True)
plt.legend()
plt.show()
