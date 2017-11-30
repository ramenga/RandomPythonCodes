class FlexibleAdopter(Adopter):
    def __init__(self, name, desired_species, considered_species):
        Adopter.__init__(self, name, desired_species)
        self.considered_species = considered_species
        
    def get_score(self,adoption_center):
        num_other = 0
        for speci in self.considered_species:
            num_other += self.considered_species[speci]
        score = Adopter.get_score(adoption_center)+0.3*num_other
        return score
        
class FearfulAdopter(Adopter):
    def __init__(self, name, desired_species, feared_species):
        Adopter.__init__(self, name, desired_species)
        self.considered_species = feared_species
        
    def get_score(self,adoption_center):
        num_feared = 0
        for speci in self.feared_species:
            num_feared += self.feared_species[speci]
        score = Adopter.get_score(adoption_center)-0.3*num_feared
        return score