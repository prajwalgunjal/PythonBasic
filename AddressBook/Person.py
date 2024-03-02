class Contact:
    def __init__(self, name, phone, email,address,city, state,pincode):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.city = city
        self.state = state
        self.pincode = pincode
    def __str__(self):
        return f"Name :{self.name}, Phone: {self.phone}, EmailL: {self.email}, Address : {self.address}, City : {self.city}, State {self.state}, Pincode {self.pincode}"