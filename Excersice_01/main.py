from ClassDef import Boson, Higgs

def main():
    print("---BOSON---")
    photon = Boson(name = "Photon", spin = 1, momentum = 100)
    photon.PrintInfo()
    
    print("\n---HIGGS BOSON---")
    higgs = Higgs(name = "Higgs Boson", spin = 0, momentum = 50, MassMean = 125)
    higgs.PrintInfo()
    higgs.Energy()
    
if __name__ == "__main__":
    main()