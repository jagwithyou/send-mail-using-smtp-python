def get_contact_list(filename):
    """
    Return a list of list having name and email read from a file specified by filename.
    """
    
    contact_list = []
    file_type = filename.split(".")[-1]
    if file_type == 'txt':
        with open(filename, mode='r', encoding='utf-8') as contacts_file:
            for a_contact in contacts_file:
                contact_list.append(a_contact.split())
        return contact_list

    elif file_type == "xlsx":
        import pandas as pd
        df = pd.read_excel (filename, usecols= ['name','email']) #for an earlier version of Excel, you may need to use the file extension of 'xls'
        for _,(name,email) in df.iterrows():
            contact_list.append([name, email])
        return contact_list
    elif file_type == "csv":
        import pandas as pd
        df = pd.read_csv (filename, usecols= ['name','email']) #for an earlier version of Excel, you may need to use the file extension of 'xls'
        for _,(name,email) in df.iterrows():
            contact_list.append([name, email])
        return contact_list


if __name__ == '__main__':
    filename = "contact_list.txt"
    contact_list = get_contact_list(filename)
    print(contact_list)
    filename = "contact_list.xlsx"
    contact_list = get_contact_list(filename)
    print(contact_list)
    filename = "contact_list.csv"
    contact_list = get_contact_list(filename)
    print(contact_list)