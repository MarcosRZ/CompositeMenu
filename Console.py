__doc__ = "Client class that builds the application menus"

from Menu import Menu
from Actions import *

# Main, Talk and Calc menus (MenuComponents)
main = Menu("Main Menu")
talk = Menu("Talk")
calc = Menu("Calc")

# Version Action for Main menu
version = PrintVersionAction("Print Version")

# Talk items (leafs)
hello = HelloAction()
goodbye = GoodbyeAction()

# Calc items (leafs)
sum = SumAction()
sub = SubAction()

# Main Menu items
main.addItem(talk)
main.addItem(calc)
main.addItem(version)

# Adding items to talk menu
talk.addItem(hello)
talk.addItem(goodbye)

# Adding items to calc menu
calc.addItem(sum)
calc.addItem(sub)

# Fire in the hole, mowerfreaker!
main.execute()