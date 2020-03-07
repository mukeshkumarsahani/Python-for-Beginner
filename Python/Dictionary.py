monthConversion = {
    "jan": "january",
    "feb": "february",
    "mar": "march",
    "apr": "april",
    "may": "may",
    "jun": "june",
    "jul": "july",
    "aug": "august",
    "sep": "september",
    "oct": "october",
    "nov": "november",
    "dec": "december"
}

print(monthConversion["nov"])  #november

print(monthConversion.get("jan"))  # january

print(monthConversion.get("mks"))  # None

print(monthConversion.get("mks","Not a Valid key"))    # Not a Valid key