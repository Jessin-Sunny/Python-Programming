class InvalidAgeException(Exception):
    def __init__(self, age, message="Age must between 18 and 100"):
        self._age = age
        self._message = message
        super().__init__(self._message)


age = 10
if(age < 18 or age > 100):
    raise InvalidAgeException(age)
