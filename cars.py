class Car:
    def __init__(self, id, brand, model, size, costofrent, availability):
        self.id = id
        self.brand = brand
        self.model = model
        self.size = size
        self.costofrent = costofrent
        self.availability = availability

    def print_available(self):
        if self.availability == True:
            print("ID:", self.id)
            print("Brand:", self.brand)
            print("Model:", self.model)
            print("Size:", self.size)
            print("Cost of rent:", self.costofrent)
            print("\n")
        
    def print_by_cost(self, cost):
        if self.availability == True and self.costofrent < cost:
            print("ID:", self.id)
            print("Brand:", self.brand)
            print("Model:", self.model)
            print("Size:", self.size)
            print("Cost of rent:", self.costofrent)
            print("\n")

    def print_by_size(self, size):
        if self.availability == True and self.size.lower() == size.lower():
            print("ID:", self.id)
            print("Brand:", self.brand)
            print("Model:", self.model)
            print("Size:", self.size)
            print("Cost of rent:", self.costofrent)
            print("\n")
            
