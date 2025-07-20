from models.aquatic_organism import AquaticOrganism

class Alga(AquaticOrganism):
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        return f"Alga [{self.pv} pv] -- {'🌿' if self.is_alive else '💀'}"