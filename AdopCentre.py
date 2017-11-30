class AdoptionCenter(object):
    def __init__(self, name, species_types, location):
        self.name = name
        self.species_types =  species_types
        self.location = location
        
        
        
    def get_name(self):
        return self.name
    
    def get_location(self):
        #for i in range(len(self.location)):
            #self.location[i]=float(self.location[i])
    
        return self.location
        
    def get_species_count(self):
        return self.species_types.copy()
        
    def get_number_of_species(self,species):
        if species in self.species_types:
            return self.species_types[species]
        else:
            return None
            
    def adopt_pet(self,species):
        if self.species_types[species] != 0:
            self.species_types[species] -=1
        if self.species_types[species] == 0:
            del self.species_types[species]