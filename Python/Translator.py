def translate(phrase):
    translation = ""

    for letter in phrase:

        if letter in "AEIOUaeiou":
            translation = translation +"g"

        else:
            translation = translation + letter

    return translation
    
print(translate(input("Enter the phrase: ")))     # mukesh  ---> mgkgsh
                                                  # sky   --> sky
                        # To be or not to be   ----> Tg bg gr ngt tg bg