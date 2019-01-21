a = "hello"
b = 'world'
c = '''a multiple
line string'''
d = """More
multiple"""
e = ("Three" "Strings" "Together")

emails = ("a@example.com", "b@example.com")
message = {
    "subject": "You Have Mail!",
    "message": "Here's some mail for you!"
}

formatted = f"""
From: <{emails[0]}>
To: <{emails[1]}>
Subject: {message['subject']}
{message['message']}"""

print (formatted)

class EMail:
    def __init__(self, from_addr, to_addr, subject, message):
        self.from_addr, self.to_addr, self.subject, self._message =(
            from_addr, to_addr, subject, message
        )

    def message(self):
        return self._message

email = EMail(
    "a@example.com", "b@example.com", "You Have Mail!", "Mail for you!"
) 

formatted = f"""
From: <{email.from_addr}>
To: <{email.to_addr}>
Subject: {email.subject}

{email.message()}"""
print(formatted)


f"{['a' for a in range(5)]}"
f"{'yes' if True else 'no'}"

subtotal = 12.32
tax = subtotal * 0.07
total = subtotal + tax

print(
    "Sub: ${0} Tax: ${1} Total: ${total}".format(
        subtotal, tax, total=total
    )
)

print(
    "Sub: ${0:0.2f} Tax:${1:0.2f} "
    "Total: ${total:0.2f}".format(subtotal, tax, total=total)
)

orders = [
    ("burger", 2, 5), ("fries", 3.5, 1), ("cola", 1.75, 3)
]

print("PRODUCT QUANTITY PRICE SUBTOTAL")
for product, price, quantity in orders:
    subtotal = price * quantity
    print (
        f"{product:10s}{quantity:^9d} "
        f"${price:<8.2f}${subtotal:>7.2f}"
    )
 

import datetime
the_date = datetime.datetime.now()  
print(f"{the_date:%Y-%m-%d %I:%M%p}")

template = "abc {number:*^10d}"
template.format(number = 32)
template.format(number = 1000)



b=bytearray(b"abcdefgh")
b[4:6] = b"xy"
b

mrbs = bytearray(b"hello")
mrbs.pop()
mrbs