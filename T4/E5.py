class Terminal:
    def __init__(self, phone_number:str):
        if not self._validate_phone_number(phone_number):
            raise ValueError("Invalid phone number. Please enter a valid 9-digit number starting with 9, 6, or 7.")
        self._phone_number = phone_number
        self._conversation_time = 0
    
    # Method validate PhoneNumber
    def _validate_phone_number(self, phone_number:str)->bool:
        result = False
        # Review the conditions - (only digits, starting with 9, 6, or 7, and their length is nine digit
        if(phone_number.isdigit() and phone_number[0] in ('9', '6', '7') and len(phone_number) == 9):
            result = True
        return result
    
    # Method Call with other_terminal
    def call(self, other_terminal, duration:int):
        #Validate that other Terminal is an Terminal object.
        if not isinstance(other_terminal, Terminal):
            raise ValueError("Invalid argument. Please provide a valid Terminal object.")
        self._conversation_time += duration
        other_terminal._conversation_time += duration
    
    # Method String
    def __str__(self):
        return f"{self._phone_number[:3]} {self._phone_number[3:5]} {self._phone_number[5:7]} {self._phone_number[7:]} - Conversation time: {self._conversation_time}s"
    

class Mobile(Terminal):
    def __init__(self, phone_number:str, rate:str):
        super().__init__(phone_number)
        if rate not in ("rat", "monkey", "elephant"):
            raise ValueError("Invalid rate. Please enter a valid rate (rat, monkey, or elephant).")
        self._rate = rate
        self._cost_per_minute = 0
        if self._rate == "rat":
            self._cost_per_minute = 0.05
        elif self._rate == "monkey":
            self._cost_per_minute = 0.15
        elif self._rate == "elephant":
            self._cost_per_minute = 0.30
    
    # Method Change Rate
    def change_rate(self, new_rate:str):
        if new_rate not in ("rat", "monkey", "elephant"):
            raise ValueError("Invalid rate. Please enter a valid rate (rat, monkey, or elephant).")
        self._rate = new_rate
        if self._rate == "rat":
            self._cost_per_minute = 0.05
        elif self._rate == "monkey":
            self._cost_per_minute = 0.15
        elif self._rate == "elephant":
            self._cost_per_minute = 0.30
    
    # Method Call with other_terminal
    def call(self, other_terminal, duration:int):
        #Validate that other Terminal is an Terminal object.
        if not isinstance(other_terminal, Terminal):
            raise ValueError("Invalid argument. Please provide a valid Terminal object.")
        self._conversation_time += duration
        cost = duration * self._cost_per_minute
        other_terminal._conversation_time += duration
        print(f"{self} - charged {cost:.2f}€")
    
    # Method String
    def __str__(self):
        return f"{self._phone_number[:3]} {self._phone_number[3:5]} {self._phone_number[5:7]} {self._phone_number[7:]}- {self._conversation_time}s of conversation - charged {self._conversation_time * self._cost_per_minute:.2f}€"


if __name__ == "__main__":
    # Test Terminal
    t1 = Terminal("666112233")
    t2 = Terminal("666744459")
    t3 = Terminal("632128919")
    t4 = Terminal("664135818")
    print(t1)
    print(t2)
    t1.call(t2, 420)
    t1.call(t3, 210)
    print(t1)
    print(t2)
    print(t3)
    print(t4)
    
    # Test Mobile
    m1 = Mobile("666112233", "rat")
    m2 = Mobile("666744459", "monkey")
    m3 = Mobile("632128919", "elephant")
    print(m1)
    print(m2)
    m1.call(m2, 210)
    m1.call(m3, 320)
    m2.call(m3, 450)
    print(m1)
    print(m2)
    print(m3)
