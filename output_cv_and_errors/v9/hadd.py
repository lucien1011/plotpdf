import os
files = [
    "%sJet_envCvRelHist_le3j_eq0b.root",
    "%sJet_envCvRelHist_le3j_eq1b.root",
    "%sJet_envCvRelHist_le3j_eq2b.root",
    "%sJet_envCvRelHist_le3j_eq3b.root",
    "%sJet_envCvRelHist_ge4j_eq0b.root",
    "%sJet_envCvRelHist_ge4j_eq1b.root",
    "%sJet_envCvRelHist_ge4j_eq2b.root",
    "%sJet_envCvRelHist_ge4j_eq3b.root",
    "%sJet_envCvRelHist_ge4j_ge4b.root",]

for jet in ["pf","calo"]:
    cmd = " ".join(["hadd -f", "%sJet_envCvRelHist.root" % jet] + [x % jet for x in files])
    os.system(cmd)
