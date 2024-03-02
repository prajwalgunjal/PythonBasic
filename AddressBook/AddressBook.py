from Person import Contact  # Importing directly without the dot

class AddressBook:
    def __init__(self):
        self.contacts= []

    def Add_Contact(self, contact):
        try:
            self.contacts.append(contact)
        except Exception as e:
            print(f"Error While Inserting in List{e}")

    def Display(self):
        try:
            if not self.contacts:
                print("No Contacts to Display")
            else:
                for contacts in self.contacts:
                    print(contacts)
        except Exception as e:
            print (f"An Exception occurs {e}")

if __name__ == "__main__":
    addressBook = AddressBook()

    try:
        while True:
            print("\nAddress Book Menu:")
            print("1. Add Contact")
            print("2. Display Contacts")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter Name: ")
                phone = input("Enter Phone: ")
                email = input("Enter Email: ")
                address = input("Enter Address: ")
                city = input("Enter City: ")
                state = input("Enter State: ")
                pincode = input("Enter Pincode: ")
                new_contact = Contact(name, phone, email, address,city, state,pincode)
                addressBook.Add_Contact(new_contact)
                print("Contact added successfully!")

            elif choice == "2":
                print("\n--- All Contacts ---")
                addressBook.Display()

            elif choice == "3":
                print("Exiting Address Book.")
                break
            else:
                print("Invalid choice. Please try again.")          
    except Exception as e:
        print(f"An unexpected error occurred: {e}")