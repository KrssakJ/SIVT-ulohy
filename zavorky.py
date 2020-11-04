
def checkParentheses(text):
	print(text)
	lefties=0
	leftpar=["("] # ,"[","{","<"
	rightpar=[")"] # ,"]","}",">"
	for i in text:
		if(i in leftpar):
			lefties+=1
		elif(i in rightpar):
			lefties-=1
		if(lefties<0):
			return("False")
	if(lefties==0):
		return("True")
	return("False")

text=input("Write parentheses here: ")
results=checkParentheses(text)
print(results)
			
# validni musi byt () nebo nekolik (()())
# invalidni je treba ())(()

# tezko rict jak by to slo s jinymi typy zavorek, napada me jenom ze bych tam udelal 3 dalsi promenny a po kazdy zavorce provedl 4 checky, ale to je strasne pomaly
