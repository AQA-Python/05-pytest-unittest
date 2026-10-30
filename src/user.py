class User:

    def __init__(self, user_id, name, age, email):
        self.id = user_id
        self.name = name
        self.age = age
        self.email = email

    def is_adult(self):
        return self.age >= 18

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "email": self.email
        }