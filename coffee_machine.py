from machine_states import States


class CoffeeMachine:

    def __init__(self, ):
        self.water_current = 400
        self.milk_current = 540
        self.coffee_current = 120
        self.cups_current = 9
        self.cash_current = 550
        self.state = States.choosing_an_action

    def make_action(self, instruction):
        if self.state == States.choosing_an_action:
            if instruction == "remaining":
                print(self)
            elif instruction == "buy":
                self.state = States.choosing_coffee
                self.make_action(coffe_selection())
            elif instruction == "fill":
                fill(self)
                self.state = States.choosing_an_action
            elif instruction == "take":
                take(self)
                self.state = States.choosing_an_action
            elif instruction == "exit":
                self.state = States.exit
        elif self.state == States.choosing_coffee:
            if instruction == "back":
                self.state = States.choosing_an_action
            else:
                buy(self, int(instruction))
                self.state = States.choosing_an_action

    def __str__(self):
        return f"""
        The coffee machine has:
        {self.water_current} ml of water
        {self.milk_current} ml of milk
        {self.coffee_current} g of coffee beans
        {self.cups_current} disposable cups
        {self.cash_current} of money
        """


def has_enough_supplies(coff_mach, water_, milk_, coffee_):
    enough_water = coff_mach.water_current - water_ > 0
    enough_milk = coff_mach.milk_current - milk_ > 0
    enough_coffee = coff_mach.coffee_current - coffee_ > 0
    enough_cups = coff_mach.cups_current - 1 > 0

    insufficient_items = []
    if not enough_water:
        insufficient_items.append("water")
    if not enough_milk:
        insufficient_items.append("milk")
    if not enough_coffee:
        insufficient_items.append("coffee")
    if not enough_cups:
        insufficient_items.append("cups")

    if len(insufficient_items) == 0:
        print("I have enough resources, making you a coffee!")
        return True
    else:
        print(f"Sorry, not enough {', '.join(insufficient_items)}!")
        return False


def make_coffee(coff_mach, water, milk, coffee, price):
    if has_enough_supplies(coff_mach, water, milk, coffee):
        coff_mach.water_current -= water
        coff_mach.milk_current -= milk
        coff_mach.coffee_current -= coffee
        coff_mach.cups_current -= 1
        coff_mach.cash_current += price


def buy(coff_mach, coffee_id):
    if coffee_id == 1:
        make_coffee(coff_mach, 250, 0, 16, 4)
    elif coffee_id == 2:
        make_coffee(coff_mach, 350, 75, 20, 7)
    elif coffee_id == 3:
        make_coffee(coff_mach, 200, 100, 12, 6)


def fill(coff_mach):
    print("Write how many ml of water you want to add: ")
    coff_mach.water_current += int(input())
    print("Write how many ml of milk you want to add: ")
    coff_mach.milk_current += int(input())
    print("Write how many grams of coffee beans you want to add: ")
    coff_mach.coffee_current += int(input())
    print("Write how many disposable cups you want to add:")
    coff_mach.cups_current += int(input())


def take(coff_mach):
    print(f"I gave you ${coff_mach.cash_current}")
    coff_mach.cash_current = 0


def define_action():
    print("Write action (buy, fill, take, remaining, exit): ")
    return input()


def coffe_selection():
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    return input()


if __name__ == '__main__':
    cm = CoffeeMachine()
    while cm.state != States.exit:
        cm.make_action(define_action())
