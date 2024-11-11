#!/usr/bin/env python3

# Find out how long it takes to pay off a mortgage

principal = 500000
payment = 2684.11
rate = 0.05
total_paid = 0

# Extra payment info
extra_payment = 1000
extra_payment_start_month = 1
extra_payment_end_month = 60
month = 0

out = open('schedule.txt', 'w')

print('{:>5s} {:>10s} {:>10s} {:>10s}'.format('Month', 'Interest', 'Principal', 'Remaining'), file=out)
while principal > 0:
    month += 1
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        total_payment = payment + extra_payment
    else:
        total_payment = payment
    interest = principal*(rate/12)
    principal += interest - total_payment
    total_paid += total_payment
    # print("%10s %10.2f %10.2f %10.2f" % (month, interest, total_payment - interest, principal), file=out) # normal spacing
    # print('{:>5d} {:>10.2f} {:>10.2f} {:>10.2f}'.format(month, interest, total_payment - interest, principal), file=out) # right justify
    print('{:<5d} {:<10.2f} {:<10.2f} {:<10.2f}'.format(month, interest, total_payment - interest, principal), file=out) # left justify

out.close()
print("Total paid: %.2f" % total_paid)