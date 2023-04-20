def check(ip):
	if ip > 0:
		print("\nValue is positive")
		
	elif ip == 0:
		print("\n0 is niether +[ve] or -[ve]")
		
	elif ip < 0:
		print("\nNumber is Negative")
		
	elif ip == float(ip):
		check(ip)
	
	else:
		print("Something Went Wrong")
try:		
	ip = float(input("Value: "))
	check(ip)
except:
	ip = int(input("Value: "))
	check(ip)