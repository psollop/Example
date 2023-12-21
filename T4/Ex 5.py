# PABLO SOLLO PONCE
# EJ5
class Terminal:
    def __init__(self, phone_number):
        if not self._validate_phone_number(phone_number):
            raise ValueError("Invalid phone number")
        
        self.phone_number = phone_number
        self.conversation_time = 0

    def _validate_phone_number(self, phone_number):
        return (
            len(phone_number) == 9
            and phone_number[0] in ('9', '6', '7')
            and phone_number.isdigit()
        )

    def call(self, other_terminal, duration):
        self.conversation_time += duration
        other_terminal.conversation_time += duration

    def __str__(self):
        return f"{self.phone_number[:3]} {self.phone_number[3:5]} {self.phone_number[5:7]} {self.phone_number[7:]} - Conversation time: {self.conversation_time}s"


class Mobile(Terminal):
    RATES = {"rat": 0.05, "monkey": 0.15, "elephant": 0.30}

    def __init__(self, phone_number, rate):
        super().__init__(phone_number)
        if rate not in Mobile.RATES:
            raise ValueError("Invalid rate")
        
        self.rate = rate
        self.charge = 0

    def change_rate(self, new_rate):
        if new_rate not in Mobile.RATES:
            raise ValueError("Invalid rate")
        
        self.rate = new_rate

    def call(self, other_mobile, duration):
        cost_per_minut = Mobile.RATES[self.rate]
        cost = cost_per_minut * duration/60
        self.charge += cost
        super().call(other_mobile, duration)

    def __str__(self):
        return f"{self.phone_number}- {self.conversation_time}s of conversation - charged {self.charge:.2f}€"


# Test the Terminal class
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

# Test the Mobile class
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
