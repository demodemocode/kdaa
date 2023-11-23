def square(x, y):
	if x < 10 or y < 10 :
		return x * y
	
	x_str, y_str = str(x), str(y)
	n = len(x_str)
	hl = (n+1)//2
	
	xh,xl = int(x_str[:-hl] or 0),int(x_str[-hl:])
	yh,yl = int(y_str[:-hl] or 0),int(y_str[-hl:])
	
	z2 = square(xh,yh)
	z1 = square(xh+xl,yh+yl)
	z0 = square(xl,yl)
	
	return(z2*(10**(2*hl)) + (z1-z2-z0)*(10**(hl)) + z0)

N = int(input("Enter 20 digit number: "))
print(f"Square of {N} is {square(N,N)}")
