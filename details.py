# This program is about collecting client details and adding them to their specific folder or file.
# TWU means still with us.

from datetime import datetime

clients = {
    "Sibusiso": {"Surname": "Ndlulu", "Gender": "male", "age": 18, "Join date": "13 August 2024", "contacts": "27633064346", "status": "TWU"},
    "Sibahle": {"Surname": "Khulane", "Gender": "female", "age": 25, "Join date": "30 July 2024", "contacts": "27734619374", "status": "TWU"},
    "Khaya": {"Surname": "Tyesi", "Gender": "male", "age": 17, "Join date": "3 December 2024", "contacts": "27675439574", "status": "left"},
    "Sisipho": {"Surname": "Buzile", "Gender": "female", "age": 23, "Join date": "29 June 2024", "contacts": "27749364925", "status": "TWU"},
    "jada": {"Surname": "lkazeli", "Gender": "female", "age": 16, "Join date": "29 March 2024", "contacts": "276346789498", "status": "TWU"},
}

# Add new clients
while True:
    name = input("Enter a name (or 'stop' to finish): ").strip()
    if name.lower() == "stop":
        break

    surname = input("Please enter surname: ")
    while not surname.isalpha():
        print("Surname must contain letters only.")
        surname = input("Please enter surname: ")

    gender = input("Please enter gender (male/female): ").lower()
    while gender not in ("male", "female"):
        print("Invalid gender. Type 'male' or 'female'.")
        gender = input("Enter gender: ").lower()

    while True:
        try:
            age = int(input("Please enter age: "))
            break
        except ValueError:
            print("Age must be a number.")

    date_str = input("Enter joining date (Example: 29 March 2024): ")
    while True:
        try:
            joining_date = datetime.strptime(date_str, "%d %B %Y")
            break
        except ValueError:
            print("Invalid format! Example: 29 March 2024")
            date_str = input("Enter date: ")

    contacts = input("Please enter phone number: ")
    while not (contacts.isdigit() and 10 <= len(contacts) <= 12):
        print("Invalid number! Use digits only (10–12 digits).")
        contacts = input("Enter contact number: ")

    status = input("Are they still with the company? (TWU/left): ").upper()
    while status not in ("TWU", "LEFT"):
        print("Use only 'TWU' or 'LEFT'.")
        status = input("Are they still with the company? (TWU/LEFT): ").upper()

    clients[name] = {
        "Surname": surname,
        "Gender": gender,
        "age": age,
        "Join date": joining_date.strftime("%d %B %Y"),
        "contacts": contacts,
        "status": status
    }

# Save clients to file
with open("clients.txt", "w") as file:
    for name, info in clients.items():
        file.write(f"Name: {name}\n")
        for key, value in info.items():
            file.write(f"  {key}: {value}\n")
        file.write("\n")

# Separate clients by age and status
underage_file = []
adult_file = []

for name, info in clients.items():
    if info["age"] < 18:
        underage_file.append((name, info))
    else:
        adult_file.append((name, info))

ex_clients = [
    (name, info)
    for name, info in underage_file + adult_file
    if info["status"].lower() == "left"
]

# Remove ex-clients from main lists
underage_file = [(n, i) for n, i in underage_file if (n, i) not in ex_clients]
adult_file = [(n, i) for n, i in adult_file if (n, i) not in ex_clients]

# Function to print any list with enumeration
def print_clients(file_name, client_list):
    print(f"\n--- {file_name} ---")
    if not client_list:
        print("No clients in this file.\n")
        return
    for i, (name, info) in enumerate(client_list, start=1):
        print(f"{i}. {name}")
        for key, value in info.items():
            print(f"   {key}: {value}")
        print()

# User commands
def commands():
    while True:
        print("\nWhat do you want to do?")
        print("1. Open underage file")
        print("2. Open adult file")
        print("3. Open ex-client file")
        print("4. Stop")

        choice = input("Enter a number (1-4): ")

        if choice == "4":
            break
        elif choice == "1":
            print_clients("UNDERAGE CLIENTS", underage_file)
        elif choice == "2":
            print_clients("ADULT CLIENTS", adult_file)
        elif choice == "3":
            print_clients("EX CLIENTS", ex_clients)
        else:
            print("Invalid option. Try again.\n")

def search_client():
    name = input("Enter the client name to search: ").strip()
    client = clients.get(name)
    if client:
        print(f"\n{name}:")
        for key, value in client.items():
            print(f"  {key}: {value}")
    else:
        print("Client not found.")

commands()
search_client()