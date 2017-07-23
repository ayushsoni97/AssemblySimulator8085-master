int a = 5;
int b = 7;
loop 20
   loop 20
     int temp = 0;
     if a > b
	a = a - b;
	temp = temp + a;
     else
	a = a + b;
	temp = a - temp;
     endif
   endloop
endloop