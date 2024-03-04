class Contact:
    def __init__(self, name, phone, email, address, city, state, pincode):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.city = city
        self.state = state
        self.pincode = pincode

    def to_dict(self):
            return {
                'name': self.name,
                'phone': self.phone,
                'email': self.email,
                'address': self.address,
                'city': self.city,
                'state': self.state,
                'pincode': self.pincode
            }
    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}, City: {self.city}, State: {self.state}, Pincode: {self.pincode}"
#https://github.com/prajwalgunjal/Day28_Adv_AddressBook/blob/main/main/java/com/bridgelabz/AddressBookMain.java
    #https://github.com/prajwalgunjal?page=3&tab=repositories
    #https://github.com/prajwalgunjal?page=3&tab=repositories