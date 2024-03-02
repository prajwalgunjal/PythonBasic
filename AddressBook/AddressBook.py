from Person import Contact  # Importing directly without the dot
import json
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
                for contact in self.contacts:
                    print(f"Name: {contact.name}")
                    print(f"Phone: {contact.phone}")
                    print(f"Email: {contact.email}")
                    print(f"Address: {contact.address}")
                    print(f"City: {contact.city}")
                    print(f"State: {contact.state}")
                    print(f"Pincode: {contact.pincode}")
                    print("-" * 20)
        except Exception as e:
            print(f"An Exception occurs: {e}")

    def SaveTOJson(self):
        try:
            contacts_as_dict = [contact.to_dict() for contact in self.contacts]
            with open('D:\Pyhton\AddressBook\Contact.json','w') as json_File:
                json.dump(contacts_as_dict,json_File,indent=2)
                print("Contacts stored as JSON in 'contacts.json'")
        except Exception as e :
            print("Exception While converting to json")

    
    def SerchContact(self,name):
        try:
            if not self.contacts:
                print(f"No Count Found of name :- {name}")
            else:
                isPresent = None 
                for contact in self.contacts:
                    if contact.name == name:
                        isPresent= True
                    else:
                        isPresent = False
                if isPresent:
                    print(f"{name} Contact Found:")
        except Exception as e:
            print(f"Exception while searching the contact")

    def DeleteContact(self, name):
        try:
            if not self.contacts:
                print("No Contacts to Delete")
                return False
            else:
                found_contact = None
                for contact in self.contacts:
                    if contact.name == name:
                        found_contact = contact
                        break
                if found_contact:
                    self.contacts.remove(found_contact)
                    print(f"Contact '{name}' deleted successfully.")
                    return True
                else:
                    print(f"Contact '{name}' not found.")
                    return False

        except Exception as e:
            print(f"Exception Occurs While deleting Contacts {e}")
            return False

if __name__ == "__main__":
    addressBook = AddressBook()

    try:
        while True:
            print("\nAddress Book Menu:")
            print("1. Add Contact")
            print("2. Display Contacts")
            print("3. Delete Contacts")
            print("4. Search By name")
            print("5. Convert to json")
            print("6. Read Json")
            print("0. Exit")

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
            elif choice =="3":
                NameTodelete = input("Enter Name of the contact which you want to delete")
                isdeleted =addressBook.DeleteContact(NameTodelete)
                if isdeleted:
                    want_toSeeUpdated =input("Press y to See Updated List")
                    if want_toSeeUpdated.lower() == "y":
                        addressBook.Display()
            elif choice == "0":
                print("Exiting Address Book.")
                break
            elif choice =="4":
                nameToSearch = input("Enter name to Search :- ")
                addressBook.SerchContact(nameToSearch)
            elif choice == "5":
                addressBook.SaveTOJson()
            #elif choice =="6":
                #addressBook.readJson()
            else:
                print("Invalid choice. Please try again.")          
    except Exception as e:
        print(f"An unexpected error occurred: {e}")