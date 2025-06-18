MAX_NAME_LENGTH = 10
MAX_UNITS = 200
MIN_WEIGHT = 1
MAX_WEIGHT = 200

class Pet:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.alive = True

    def feed(self, units):
        if self.alive:
            self.weight += units
            self._check_alive()

    def exercise(self, minutes):
        if self.alive:
            self.weight -= minutes
            self._check_alive()

    def _check_alive(self):
        if self.weight <= 0:
            self.alive = False

    def get_status(self):
        if not self.alive:
            return "RIP"
        elif self.weight > MAX_WEIGHT:
            return ":-("
        else:
            return str(self.weight)

def main():
    pets = []

    # Get pet names and weights
    while True:
        name = input("Enter pet name (or 'XXX' to finish): ").strip()
        if name.upper() == "XXX":
            break
        if len(name) > MAX_NAME_LENGTH:
            print(f"Name too long. Must be {MAX_NAME_LENGTH} characters or less.")
            continue
        try:
            weight = int(input("Enter initial weight: "))
            if weight < MIN_WEIGHT:
                print("Weight must be a positive number.")
                continue
            pets.append(Pet(name, weight))
        except ValueError:
            print("Invalid weight. Please enter a whole number.")

    while True:
        for pet in pets:
            action = input(f"{pet.name} (current weight: {pet.weight}) - Action (F=feed, E=exercise, Q=nothing): ").strip().upper()
            if action == "Q":
                continue
            elif action in ("F", "E"):
                try:
                    value = int(input("Enter amount (1-200): "))
                    if 1 <= value <= MAX_UNITS:
                        print("Amount must be between 1 and 200.")
                        continue
                    if action == "F":
                        pet.feed(value)
                    elif action == "E":
                        pet.exercise(value)
                except ValueError:
                    print("Invalid number. Try again.")
        
        if input("Do you want to continue? (Y/N): ").strip().upper() != "Y":
            break

    print("\nFinal Status of Pets:")
    for pet in pets:
        print(f"{pet.name}: {pet.get_status()}")

if __name__ == "__main__":
    main()