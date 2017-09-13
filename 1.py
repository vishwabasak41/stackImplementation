ss=input("Enter your string")
stack=[]

def push(key,stk):
	stk.append(key)
	print("added to stack is ",key," and so stack is",stk)

def pop(key,stk):
	length=len(stk)
	r=0
	if key==')' and stk[length-1]=='(':
		del stk[length - 1]
		r=1
	elif key == ']' and stk[length - 1] == '[':
		del stk[length - 1]
		r=1
	else:
		r=0
	return r
	print("stack is",stk)

for i in ss:
	if i=='(' or i=='[':
		push(i,stack)
	elif i==')' or i==']':
		result =pop(i,stack)
		if result==0:
			print("Error:at ",ss.index(i)+1)
	else:
		continue
if len(stack)==0:
	print ("sucess!")
else:
	print("error!")