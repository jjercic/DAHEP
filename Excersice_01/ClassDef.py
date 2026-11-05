import random

class Boson:
    isFermion = False
    
    def __init__(self, name, spin, momentum):
        self.name = name
        self.spin = spin
        self.momentum = momentum
        
    def PrintInfo(self):
        print(f"Name: {self.name}")
        print(f"Spin: {self.spin}")
        print(f"Momentum: {self.momentum}")
     
       
class Higgs(Boson):
    MassSigma = 1
    
    def __init__(self, name, spin, momentum, MassMean = 125):
        super().__init__(name, spin, momentum)
        self.MassMean = MassMean
        
    def Energy(self):
        mass = random.gauss(self.MassMean, self.MassSigma)
        energy = (self.momentum ** 2 + mass ** 2) ** 0.5
        # c = 1
        print(f"Generated Mass: {mass:.3f} GeV")
        print(f"Energy: {energy:.3f} GeV")
        return energy
    
    def PrintInfo(self):
        super().PrintInfo()
        print(f"Mass Mean: {self.MassMean}")
        print(f"Mass Sigma: {self.MassSigma}")
    