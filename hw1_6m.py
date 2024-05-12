
from collections import UserDict

class Field:   # Базовий клас для полів запису
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
class Name(Field):    # Клас для зберігання імені контакту. Обов'язкове поле
    pass

class Phone(Field):    # Клас для зберігання номера телефону. Має валідацію формату (10 цифр).
    def __init__(self, number):
        super().__init__(number)
        self.number = self.validate_number(number)
        
    def validate_number(self, number):
        digits = ''.join(filter(str.isdigit, number))
        
        if len(digits) == 10:   # Перевіряємо, чи номер має рівно 10 цифр
            return digits
        else:
            print("Номер телефону повинен містити рівно 10 цифр.")
            return None

class Record:    # Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів. Додавання телефонів. 

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    def add_phone(self, phone):   # додає номер телефону
        self.phones.append(Phone(phone))
    
    def remove_phone(self, phone):  # видаляє існуючий номер телефону
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                break
            
    def edit_phone(self, old_phone, new_phone):   # змінює номер телефону зі старого на новий
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                break
            
    def find_phone(self, phone):  # Шукає телефон
        for p in self.phones:
            if p.value == phone:
                return True
        return False
            
    
class AddressBook(UserDict):  # Клас для зберігання та управління записами  
    def __init__(self):
        super().__init__()
        self.data = {}
    def add_record(self, record):  # Додає запис до адресної кники
        self.data[record.name.value] = record  
   
    def find(self, name):  # шукає запис за ім'ям в адресній книзі
        return self.data.get(name)
   
    def delete(self, name):  # Видаляє запис з адресної книги
        if name in self.data:
            del self.data[name]
            return True
        else:
            return False
    
    
book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

for name, record in book.data.items():
    print(record)

john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  

book.delete("Jane")
