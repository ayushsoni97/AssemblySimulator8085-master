int a = 5;
int b = 6;
load
int c = 0;
c = a + b;
b = b - a;
a = a + 2;
int logic = 0;
logic = 2 or 4;
print logic
loop 10
	print "loop"
endloop
if a > b
	a = a - 2;
else
	a = a + 2;
endif
func sum r t y
r = t + y;
endfunc
call sum a 23 3
call sum b 2 5
print "done"