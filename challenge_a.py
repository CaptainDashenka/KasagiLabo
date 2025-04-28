import random
import string
import csv

def generate_object(object_type: str) -> str:
    """
    Function to generate an object of a certain type

    Parameters: object_type (str): The type of object to generate.
    """
    characters = None

    match object_type:
        case "alphabetical string": 
            characters = string.ascii_letters
        case "real number":
            characters= string.digits + "."
        case "integer":
            characters = string.digits
        case "alphanumeric":
            characters = string.ascii_letters + string.digits
        case _:
            raise Exception("Invalid object type specified.")

    # a kilobyte is 1024 bytes
    object_length = 2621440
    return ''.join(random.choice(characters) for i in range(object_length))

if __name__ == "__main__":
    # generate the 4 objects
    obj1 = generate_object("alphabetical string")
    obj2 = generate_object("real number")
    # this solution can result in multiple decimal points follwoing each other. 
    # possible solution is to replace these decimal points with a single decimal point
    obj3 = generate_object("integer")
    obj4 = generate_object("alphanumeric")
    #special case alphanumeric string; add leading and trainling spaces
    space_count = random.randint(1,5)
    obj4_with_spaces = " " * space_count + obj4[space_count:]
    obj4_with_spaces = obj4_with_spaces[:-space_count] + " " * space_count

    #save the objects to a csv file
    with open("objects.csv", "w", newline='', encoding='ASCII') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([obj1, obj2, obj3, obj4_with_spaces])
    # the 'with' block would raise an exception and still close the file resource should there be any problems with the file system    
