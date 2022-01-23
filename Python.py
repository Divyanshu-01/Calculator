from art import logo

def add(n1,n2):
  return n1+n2
def sub(n1,n2):
  return n1-n2
def mul(n1,n2):
  return n1*n2
def div(n1,n2):
  return n1/n2

operations={
  "+":add,
  "-":sub,
  "*":mul,
  "/":div
}
def calculations():
  print(logo)
  num1=float(input("Whats the first number"))

  for symbol in operations:
    print(symbol)
  should_continue=True
  while should_continue: 
    operation_symbol=input("Pick an operation from the line above")
    num2=float(input("Whats the next number"))
    cal_function=operations[operation_symbol]
    answer=cal_function(num1,num2)
    print(f"{num1} {operation_symbol} {num2} ={answer}")
    op=input("do you want to continue n for start new calculations")
    if op=="y":
      num1=answer
    else:
      should_continue=False
      calculations()

calculations()
    


  

