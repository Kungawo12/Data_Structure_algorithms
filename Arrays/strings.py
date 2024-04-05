# NOTE:Strings To Do 1


# TODO:Remove Blanks
# Create a function that, given a string, returns all of that string’s contents, but without blanks. 
#If given the string " Pl ayTha tF u nkyM usi c ", return "PlayThatFunkyMusic".
def remove_blanks(str):
    strings= ""
    for char in str:
        if char != "":
            strings += char
    return strings

print(remove_blanks("PlayThatFunkyMusic"))


#TODO: Get Digits
# Create a JavaScript function that given a string, returns the integer made from the string’s digits. 
# Given "0s1a3y5w7h9a2t4?6!8?0", the function should return the number 1357924680.
def get_digits(str):
    results = ""
    for char in str:
        if char.isnumeric():
            results+= char
    return results

print(get_digits("0s1a3y5w7h9a2t4?6!8?0"))


# TODO: Acronyms
# Create a function that, given a string, returns the string’s acronym (first letters only, capitalized). 
#Given " there's no free lunch - gotta pay yer way. ", return "TNFL-GPYW". 
#Given "Live from New York, it's Saturday Night!", return "LFNYISN".
def acronyms(str):
    string =str.split()
    acronyms = ""
    for char in string:
        acronyms += char[0].upper()
    return acronyms
    
print(acronyms("there's no free lunch - gotta pay yer way"))
print(acronyms("Live from New York, it's Saturday Night!"))

# NOTE: Zip Arrays into Dictionary
# Dictionaries are sometimes called maps because a key (string) maps to a value.
# Given two arrays, create an associative array (map) containing keys of the first, and values of the second. 
# For arr1 = ["abc", 3, "yo"] and arr2 = [42, "wassup", true], return {"abc": 42, 3: "wassup", "yo": true}.
def zip_arraY(list1, list2):
    new_dict = {}
    for i in range(min(len(list1),len(list2))):
            new_dict[list1[i]] = list2[i]
    return new_dict

print(zip_arraY(["abc", 3, "yo"],[42, "wassup", True]))
print(zip_arraY(["abc", 3, "yo","main"],[42, "wassup", True,"no"]))

#TODO: Invert Hash
# Dictionaries are also called hashes (we’ll learn why later). Build invertHash(assocArr) to convert hash keys to values, 
# and values to keys.Example: given {"name": "Zaphod", "charm": "high", "morals": "dicey"},
# return object {"Zaphod": "name", "high":"charm", "dicey": "morals"}.

def invertedHash(assocARR):
    new_dict = {}
    for key,value in assocARR.items():
        new_dict[value]= key
    return new_dict

print(invertedHash( {"name": "Zaphod", "charm": "high", "morals": "dicey"}))



