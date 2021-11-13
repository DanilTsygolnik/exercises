class Bird:
    """An abstract class representing birds"""
    enClassName = "A bird"
    ruClassName = "Птица"
    objInstancesCnt = 0

    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age
        Bird.objInstancesCnt += 1

    def get_info(self):
        print(f"{Bird.enClassName} named {self.name}:")
        print(f"id - {self.id};")
        print(f"age - {self.age};")
