#  Personal Bio Card

#Student details(string variables)
name=" Shraddha"
age=" 21 years"
Course=" GenAI Intership"
College=" SJB Institute of technology"
Email=" shraddhakharvi2228@gmail.com"

#Width of the card(controls alignment)
width=40

# Print top boarder of the card
print("╔" + "═" * width + "╗")

# Title of the card
title="STUDENT BIO CARD"

# Center the title within the card
print("║" + title.center(width) + "║")
print("╔" + "═" * width + "╗")

#Print each field using formatted strings
print("║"+f" Name    :{name}".ljust(width)+"║")
print("║"+f" Age     :{age}".ljust(width)+"║")
print("║"+f" Course  :{Course}".ljust(width)+"║")
print("║"+f" College :{College}".ljust(width)+"║")
print("║"+f" Email   :{Email}".ljust(width)+"║")

print("╚" + "═" * width + "╝")