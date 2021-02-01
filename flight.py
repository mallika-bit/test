class Flight():
     def  __init__(self,capacity):
        self.capacity = capacity
        self.passengers = []

     def add_passengers(self,name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

     def open_seats(self):
        return self.capacity - len(self.passengers)


flight = Flight(3)  

people = ["mallika","santosh","shlahga","shoubhit"]

for i in people:
    success = flight.add_passengers(i)
    if success:
        print(f"we added {i} to flight successfully")
    else:
        print(f"no available seats {i}")   

