from models.aquatic_organism import AquaticOrganism

class Alga(AquaticOrganism):
    def __init__(self):
        super().__init__()
    
    def split(self) -> "Alga":
        new_alga = Alga()
        new_alga.pv = self.pv // 2
        self.pv = self.pv // 2
        return new_alga
    
    def __str__(self) -> str:
        return f"Alga [{self.pv} pv - age: {self.age}] -- {'🌿' if self.is_alive else '💀'}"