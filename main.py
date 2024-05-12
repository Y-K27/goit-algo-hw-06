from collections import UserDict

#Базовий клас для полів запису.
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

# Клас для зберігання імені контакту. Обов'язкове поле.
class Name(Field):
    # реалізація класу
		pass
# Клас для зберігання номера телефону. Має валідацію формату (10 цифр)
class Phone(Field):
    def __init__(self, phone_number):
        self.phone = phone_number
        if len(self.phone) == 10 and self.phone.isdigit():
            return str(self.phone)
        else:
            print("The number is incorrect. the phone number must consist of 10 digits ")
            

# Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        
    def add_phone(self, phone):
        if phone not in [p.value for p in self.phones]:
            self.phones.append(phone)
            print(f'Phone {phone} has been successfully added from contact {self.name}')
        else:
            print(f"Phone {phone} already recorded for a contact {self.name}")
        pass
    
    def remove_phone(self, phone):
        if phone in [p.value for p in self.phones]:
            self.phones = [p for p in self.phones if p.value != phone]
            print(f'Phone {phone} removed from contact {self.name}')
        else:
            print(f"Phone {phone} not found for contact {self.name}")
    
    def edit_phone(self, old_phone, new_pnone):
        if old_phone in [p.value for p in self.phones]:
            for phone in self.phones:
                if phone.value == old_phone: 
                    phone.value = new_pnone
            print(f'Phone nomber has been successfully modified')
        else:
            print(f"Phone {old_phone} not found for contact {self.name}")
    
    def find_phone(self, phone:Phone):
        if phone in [ph.value for ph in self.phones]:
            print(f'{self.name}: {phone}')
        else:
            print(f"Phone {phone} not found for contact {self.name}")
    

# Виведення всіх записів у книзі
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

 # Створення нової адресної книги
 # Додавання/видалення запису до адресної книги
class AddressBook(UserDict):
    def __init__(self, initial=None):
        if initial is None:
            self.address_book = dict()
        else:
            self.address_book = dict()
		
    def add_record(self, contact:Record):
        if contact.name not in [key for key in self.address_book]:
            self.address_book[contact.name] = contact.phones
            print("The contact has been saved")
        else:
            print("A contact {contact.name} already exists in the contact book")
    
    def find(self, name):
        if name in [key for key in self.address_book]:
            print(f"Contact name: {name}, phones: {self.address_book[name]}")
        else:
            print(f"Contact: {name} are not exist)")
                  
    def delete(self, name):
        if name in [key for key in self.address_book]:
            self.address_book.pop(name)
            print(f"Contact name: {name}, has been deleted")
        else:
            print(f"Contact: {name} are not exist)")
        pass