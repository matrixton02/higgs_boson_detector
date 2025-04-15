import uproot
import numpy as np
import pandas as pd
from itertools import combinations

def get_px(pt,phi):
    return pt*np.cos(phi)

def get_py(pt,phi):
    return pt*np.sin(phi)

def get_pz(pt,eta):
    return pt*np.sinh(eta)

def get_energy(pt,eta,mass):
    return np.sqrt(pt**2 * np.cosh(eta**2 + mass**2))

def invariant_mass(particles):
    px,py,pz,E=0,0,0,0

    for idx in particles:
        pt,eta,phi,m=idx

        px+=get_px(pt,phi)
        py+=get_py(pt,phi)
        pz+=get_pz(pt,eta)
        E+=get_energy(pt,eta,m)
    mass_squared=E**2-(px**2+py**2+pz**2)
    if(mass_squared>0):
        return np.sqrt(mass_squared)
    return 0

file = uproot.open("ZZTo4mu.root")
tree = file["Events"]

muon_pt = tree["Muon_pt"].array()
muon_eta = tree["Muon_eta"].array()
muon_phi = tree["Muon_phi"].array()
muon_mass = tree["Muon_mass"].array()
muon_charge=tree["Muon_charge"].array()
nmuon=tree["nMuon"].array()

print(len(muon_pt))

higs_candidate=[]
for evt in range(0,50000):
    if(nmuon[evt]>=4 and nmuon[evt]<=6):
        four_muon_combo=list(combinations(range(len(muon_charge[evt])),4))
        for combo in four_muon_combo:
            i,j,k,l=combo
            pairings=[((i,j),(k,l)),((i,k),(j,l)),((i,l),(j,k))]
            best_mass_delta=float('inf')
            best_4mu_mass=None
            for (a,b),(c,d) in pairings:
                q1=muon_charge[evt][a]
                q2=muon_charge[evt][b]
                q3=muon_charge[evt][c]
                q4=muon_charge[evt][d]

                if(q1+q2==0 and q3+q4==0):
                   z1=[(muon_pt[evt][a],muon_eta[evt][a],muon_phi[evt][a],muon_mass[evt][a]),(muon_pt[evt][b],muon_eta[evt][b],muon_phi[evt][b],muon_mass[evt][b])]
                   z2=[(muon_pt[evt][c],muon_eta[evt][c],muon_phi[evt][c],muon_mass[evt][c]),(muon_pt[evt][d],muon_eta[evt][d],muon_phi[evt][d],muon_mass[evt][d])]

                   z1_mass=invariant_mass(z1)
                   delta=abs(z1_mass-91.2)

                   if(delta<best_mass_delta):
                       best_mass_delta=delta
                       four_mu=z1+z2
                       best_4mu_mass=invariant_mass(four_mu)
            if(best_4mu_mass):
                higs_candidate.append(best_4mu_mass)

df=pd.DataFrame({"Higgs_mass":higs_candidate})
df.to_csv("higgs_candidates.csv",index=False)
print("Calculated mass of higs candidate saved")
