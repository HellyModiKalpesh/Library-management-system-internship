
user_list = [(1, "helly", "satellite", "helly@mail.com", 912345)]

class User:
    def __init__(self, id, name, address, email, number):
        self.id = id
        self.name = name
        self.address = address
        self.email = email
        self.number = number


    def new_user(self):
        user_info = (self.id, self.name, self.address, self.email, self.number)
        user_list.append(user_info)
        return user_list
