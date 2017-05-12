class_list = []
name = raw_input("Give the name of the user you want to add: ")
while (True):
    
    date = [ str(i) for i in raw_input("Key in a date (seperated by spaces): ").split(" ")]
    event = [str(i) for i in raw_input("Key in an event (seperated by a comma): ").split(",")]
    #tests = [int(i) for i in raw_input("Test marks (seperated by spaces): ").split(" ")]

    class_list.append({
        #"name": name,
        "date": date,
        "event": event,
        #"tests": tests
    })

    cont = raw_input("Want to add another? (Y/N)")
    if cont == "N":
        break;

print(class_list)