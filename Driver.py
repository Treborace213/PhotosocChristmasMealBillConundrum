from Bill import Bill

bill = Bill()

# Charge for 13 meals, 9 lots of 2 courses and 4 lots of 3 courses
bill.charge_2c(9)
bill.charge_3c(4)
bill.charge_specific(1)  # For the £1 potatoes or whatever it was
bill.charge_specific(9.6)  # For the £2.85 and £6.75 items

print(f"Total Bill: {bill.get_total()}")

# Pay
# On reciept
#   Remove the 9.6 charge
bill.pay_specific(9.6)

#   Rest of pay
bill.pay_2c(4)
bill.pay_3c(4)
bill.charge_specific(0.6)

# Off the recipt

# Chiara pays
bill.pay_3c(1)

# What Becca payed for
bill.pay_2c(3)
bill.pay_specific(1)
b_owed = 22.95  # Owed for 1 two course meal and the £1 potato thing

print("\n-----What is unncounted for-----")
print("\nBills not payed:")
print(f"2 Course meal/s: {bill.toPay_2s}")
print(f"3 Course meal/s: {bill.toPay_3s}")
print(f"\nDeposit refund (should be £10): £{bill.get_deposit()}.")
print(
    "\nIssue: Someone has overpayed (payed a 3 course and not a 2 course).\nAnd 2 people have not payed for their 2 course."
)

# Test for fix
bill.charge_3c(1)
bill._deposit += bill._deposit_pp  # Manualy re-incriment the deposit
bill.pay_2c(2)

print("\n-----After Suggested Solution-----")
print("\nBills not payed:")
print(f"2 Course meal/s: {bill.toPay_2s}")
print(f"3 Course meal/s: {bill.toPay_3s}")
print(
    f"\nMissing money: £{bill.get_total()} - expected as someone slightly underpayed"
)
print(f"\nDeposit refund: £{bill.get_deposit()}.")

# Summary
print("\n-----Summary-----")
print(
    "\nTo summarize, I think someone overpayed by a course and that 2 people who attened did not pay."
)
