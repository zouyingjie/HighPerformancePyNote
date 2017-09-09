# -*- coding: utf-8 -*-

def list_unique_names(phonebook):
    unique_names = []
    for name, phonenumber in phonebook:
        first_name, last_name = name.split(" ", 1)
        for unique in unique_names:
            if unique == first_name:
                break
            else:
                unique_names.append(first_name)
    return len(unique_names)

def set_unique_names(phonebook):
    unique_names = set()
    for name, photonumber in phonebook:
        first_name, last_name = name.split(" ", 1)
        unique_names.add(first_name)
    return len(unique_names)

phonebook = [
    ('John dOE', '555-555-5555'),
    ('Albert ABC', '212-555-5555'),
    ('John Murphey', '202-555-5555'),
    ('Alebrt Ruter', '654-555-5555'),
    ('Elaine YAYA', '301-555-5555'),
]

print("number of from set:", set_unique_names(phonebook))
print("number of from list:", list_unique_names(phonebook))