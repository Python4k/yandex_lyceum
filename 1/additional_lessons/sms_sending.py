class Person:
    def __init__(self, first_name, middle_name, last_name, phones):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.phones = phones

    def get_phone(self):
        return self.phones.get('private', None)
    
    def get_name(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'
    
    def get_work_phone(self):
        return self.phones.get('work', None)
    
    def get_sms_text(self):
        return f'Уважаемый {self.first_name} {self.middle_name}! Примите участие в нашем беспроигрышном конкурсе для физических лиц.'
    

class Company:
    def __init__(self, name, type, phones, *employees):
        self.name = name
        self.type = type
        self.phones = phones
        self.employees = list(employees)
        
    def get_name(self):
        return self.name
    
    def get_sms_text(self):
        return f"Для компании {self.name} есть супер предложение! Примите участие в нашем беспроигрышном конкурсе для {self.type}"
        
    def get_phone(self):
        if 'contact' in self.phones:
            return self.phones['contact']
        for employee in self.employees:
            if employee.get_work_phone():
                return employee.get_work_phone()
        return None
        
        
def send_sms(*persons_and_companies):
    for item in persons_and_companies:
        if isinstance(item, Person) and not (item.get_phone() is None):
            print(f"Отправлено СМС на номер {item.get_phone()} с текстом: {item.get_sms_text()}")
        elif isinstance(item, Company) and not (item.get_phone() is None):
            print(f"Отправлено СМС на номер {item.get_phone()} с текстом: {item.get_sms_text()}")
        else:
            print(f"Не удалось отправить сообщение абоненту: {item.get_name()}") 



# Тесты 
# 1

person1 = Person("Ivan", "Ivanovich", "Ivanov", {"private": 123, "work": 456})
person2 = Person("Ivan", "Petrovich", "Petrov", {"private": 789})
person3 = Person("Ivan", "Petrovich", "Sidorov", {"work": 789})
person4 = Person("John", "Unknown", "Doe", {})
company1 = Company("Bell", "ООО", {"contact": 111}, person3, person4)
company2 = Company("Cell", "АО", {"non_contact": 222}, person2, person3)
company3 = Company("Dell", "Ltd", {"non_contact": 333}, person2, person4)
send_sms(person1, person2, person3, person4, company1, company2, company3)     
print(person3.get_phone())                
                
                
                
                
                