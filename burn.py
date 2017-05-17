print "Use this to find your burnout rate.\n"

print "How much money do you have?",
money = int(raw_input())

print "How much for bills and shit?",
bills = int(raw_input())

print "How long do you need it to last you?"
days = int(raw_input())

cash = money - bills

burnrate = cash / days
#burnrate = (money - bills) / days
print "\nYour will have $%r to spend over %r days at a rate of $%r per day." % (cash, days, burnrate)
