import random
total_amount = float(input("total amount = ").replace('$',''))
tax = "18 %"
total_a = int(total_amount * 18/100)
a = 15/100 * total_a
b = 18/100 * total_a
c = 20/100 * total_a

d = (a,b,c)
tip = random.choice(d)

print(f"your total amount {total_a} and tip will be {tip:.2f}")
print(f"In total you have to pay {(total_a + tip):.2f}")
