class Bird:
    """An abstract class representing birds"""
    enClassName = "A bird"
    ruClassName = "Птица"
    objInstancesCnt = 0

    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        Bird.objInstancesCnt += 1

    def get_info(self):
        print(f"{Bird.enClassName} named {self.name}:")
        print(f"species - {self.species};")
        print(f"age - {self.age};")
