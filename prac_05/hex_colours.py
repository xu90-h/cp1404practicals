COLOUR_CODES = {
    "AliceBlue": "#f0f8ff",
    "Coral": "#ff7f50",
    "Crimson": "#dc143c",
    "DarkOrange": "#ff8c00",
    "Gold": "#ffd700",
    "HotPink": "#ff69b4",
    "Indigo": "#4b0082",
    "LimeGreen": "#32cd32",
    "MediumPurple": "#9370db",
    "Navy": "#000080"
}

print(COLOUR_CODES)

colour_code = input("Enter a colour: ").title()
while colour_code !="":
    try:
        print(f"{colour_code} is {COLOUR_CODES[colour_code]}")
    except KeyError:
        print("Invalid colour.")
    colour_code = input("Enter a colour: ").title()