# Define a base class for all ales
class Ale:
    def __init__(self, name: str, abv: float):
        # Store the name and alcohol by volume of the ale
        self.name = name
        self.abv = abv

    def alcohol_content(self, volume_in_oz: float) -> float:
        # Multiply abv by the volume to get total alcohol content
        return self.abv * volume_in_oz

    def description(self) -> str:
        # Return a simple message showing the abv as a percentage
        return f"{self.name}: {self.abv * 100:.1f}% ABV"


# Subclasses that use the Ale superclass
class PaleAle(Ale):
    def __init__(self):
        super().__init__("Pale Ale", 0.055)


class IPA(Ale):
    def __init__(self):
        super().__init__("IPA", 0.065)


class Stout(Ale):
    def __init__(self):
        super().__init__("Stout", 0.07)


class Porter(Ale):
    def __init__(self):
        super().__init__("Porter", 0.06)

if __name__ == "__main__":
    pale = PaleAle()
    ipa = IPA()
    stout = Stout()
    porter = Porter()

    print(pale.description())
    print("Alcohol in 12 oz:", pale.alcohol_content(12))  # Expected: ~0.66

    print(ipa.description())
    print("Alcohol in 16 oz:", ipa.alcohol_content(16))  # Expected: ~1.04

    print(stout.description())
    print("Alcohol in 10 oz:", stout.alcohol_content(10))  # Expected: ~0.7

    print(porter.description())
    print("Alcohol in 8 oz:", porter.alcohol_content(8))  # Expected: ~0.48

"""

Reflection
I reviewed the posted solutions from Week 06 and compared them with my code.

Comments
My comments did not over explain. I will try adding docstrings in the future to make my code clearer.

Output and Testing
I tested all three of my functions by running the full file in the terminal. The output matched exactly what the professor expected, and everything worked.

Logic
My logic was simple and not too advanced. I will work on adding small safety checks like in the solutions to next time, so my code handles different types of input more reliably.

Overall, my code followed the rules and gave the correct output. I’m learning how to write cleaner code, test properly, and explain my work better.

"""

#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  IF THERE IS ANY CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓         PLEASE DO NOT MODIFY IF       ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 