import pandas as pd


def filter_contacts(filename):
    all_contacts = pd.read_csv(filename)
    all_contacts = all_contacts[["Name", "Given Name"]]
    print("Type Given name if you wish to include them in your Spam list.")
    print("To break, Enter x")
    print("To keep it same as the given name(the one after -), press f")
    wishing_contacts = dict()
    for index, row in all_contacts.iterrows():
        print(str(row['Name'])+"  -  "+str(row['Given Name']))
        y = input()
        if y == 'x':
            break
        if y == 'f':
            wishing_contacts[str(row['Name'])] = str(row['Given Name'])
        elif y != '':
            wishing_contacts[str(row['Name'])] = y
    return wishing_contacts
