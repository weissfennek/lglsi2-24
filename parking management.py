class Car:
    def __init__(self, brand, color, plate_number):
        self.brand = brand
        self.color = color
        self.plate_number = plate_number

class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.occupied_spaces = 0
        self.available_spaces = self.capacity

    def park_car(self, car):
        if self.available_spaces > 0:
            self.available_spaces -= 1
            self.occupied_spaces += 1
            print(f"A {car.color} {car.brand} with plate number {car.plate_number} is parked.")
        else:
            print("Sorry, the parking lot is full.")

    def unpark_car(self, car):
        if self.occupied_spaces > 0:
            self.available_spaces += 1
            self.occupied_spaces -= 1
            print(f"The {car.brand} with plate number {car.plate_number} is leaving the parking lot.")
        else:
            print("There are no cars in the parking lot.")

def main():
    parking_lot = ParkingLot(10)

    car1 = Car("Toyota", "Blue", "ABC123")
    car2 = Car("Honda", "Red", "XYZ456")
    car3 = Car("Ford", "Green", "DEF789")

    parking_lot.park_car(car1)
    parking_lot.park_car(car2)
    parking_lot.park_car(car3)

    parking_lot.unpark_car(car2)
    parking_lot.unpark_car(car3)
    parking_lot.unpark_car(car1)

if __name__ == "__main__":
    main()
