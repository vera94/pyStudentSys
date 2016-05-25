class Person:
    def __init__(self, personal_number, name, surname, address, phone, email, password):
        self.__personal_number = personal_number
        self.__name = name
        self.__surname = surname
        self.__address = address
        self.__phone = phone
        self.__email = email
        self.__password = password

    def __eq__(self, other):
        return self.__personal_number == other.__personal_number

def Teacher(Person):
    def __init__(self, personal_number, name, surname, address, phone, email, password, subject):
        Person.__init__(self, personal_number, name, surname, address, phone, email, password)
        self.__subject = subject
        self.__student_groups = {}

def Student(Person):
    def __init__(self, personal_number, name, surname, address, phone, email, password, fac_num, speciality, points):
        Person.__init__(self, personal_number, name, surname, address, phone, email, password)
        self.__fac_num = fac_num
        self.__speciality = speciality
        self.__points = points

    def __eq__(self, other):
        return self.__fac_num == other.__fac_num
        
    


    
