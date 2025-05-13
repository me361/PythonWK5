# Base class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.__storage = storage  # private attribute (encapsulation)
     #method 1; the phone can call
    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    #method 2; the phone can install an app
    def install_app(self, app_name):
        print(f"{app_name} is being installed on {self.model}.")

    def get_storage(self):
        return self.__storage  

# Subclass with inheritance and polymorphism
class GamingPhone(Smartphone):
    def install_app(self, app_name):
        print(f"Installing high-performance game: {app_name} on {self.model}!")

    def boost_mode(self):
        print(f"{self.model} is now in gaming boost mode! 🎮")

# Create regular smartphone
phone1 = Smartphone("Samsung", "Galaxy A52", "128GB")
phone1.call("0722000000")
phone1.install_app("WhatsApp")
print("Storage:", phone1.get_storage())

# Create a gaming phone (polymorphic behavior)
gaming_phone = GamingPhone("ASUS", "ROG Phone 6", "256GB")
gaming_phone.call("0799000000")
gaming_phone.install_app("Call of Duty")
gaming_phone.boost_mode()
