

#shield for input type
number_check2 <-function(x,y) { 
  n <- as.numeric(x,y)
  {return(ifelse(is.na(n), 'ValueError', 'ValueError'))}
}

#test 
print(number_check2(2,'h'))

number_check1 <-function(x) { 
  as.numeric(x)
  if (is.na(x)) 
  {return('ValueError')}
  }

#test 
print(number_check1('h'))

exponential <-function(x,y){
  if(y<0) 
  {print('nan')}
  else {number_check2(x,y)}
  {return(x**y)}
  }

print(exponential(5,6))
print(exponential(0,6))


add <-function(x,y){
  number_check2(x,y)
  {return(x+y)}
}

print(add(1,6))


subtract <-function(x,y){
  number_check2(x,y)
  {return(x-y)}
}

print(subtract(6,1))


multiply <-function(x,y){
  number_check2(x,y)
  {return(x*y)}
  }

print(multiply(6,6))


divide <-function(x,y){
  if(y == 0) {print('nan')}
  else {number_check2(x,y)}
  {return(x/y)}
  }

print(divide(6,3))

sin <-function(x){
  number_check1(x)
  {return(sin(x))}
}


cos <-function(x){
  number_check1(x)
  {return(cos(x))}
}


tan <-function(x){
  number_check1(x)
  {return(tan(x))}
}

sq <-function(x){
  number_check1(x)
  {return(sqrt(x))}
}

get_numbers <- function() {
  numb_input <- readline("Enter up to two numbers to calculate: ")
  {(return (numbers <- lapply(str_split(numb_input, ""), as.integer)))} #take up to two numbers, use the lapply function to loop over the strings and turn them into intergers, split them at the space, and add to a list
}

operation_2numbers <- function(x,y){ #A function has a definitive number of parameters. Need two functions to cover one and two-number inputs.
  op <- readline(
    "Which operation would you like to use?: \n",
    "[1] Enter 1 for addition. \n",
    "[2] Enter 2 for subtraction. \n",
    "[3] Enter 3 for multiplication. \n",
    "[4] Enter 4 for division. \n" , 
    "[5] Enter 5 for exponential. \n"
  ).as.integer
if (op < 0) or (op > 5)
  {print ('Please enter number in range 1 to 5.')}
else if (op == 1) 
  {print(add(x,y))}
else if (op == 2)
{print(subtract(x,y))}
else if (op == 3) 
  {print(multiply(x,y))}
else if (op == 4)
  {print(divide(x,y))}
else if (op == 5)
{return(exponential(x,y))}
}

operation_1number <- function(x){ 
  op <- readline(
    "Which operation would you like to use?: \n",
    "[1] Enter 1 for sin. \n",
    "[2] Enter 2 for cos. \n",
    "[3] Enter 3 for tan. \n",
    "[4] Enter 4 for sqrt. \n"
  ).as.integer
  if (op < 0) or (op > 4)
  {print ('Please enter number in range 1 to 4.')}
  else if (op == 1) 
  {print(sin(x,y))}
  else if (op == 2)
  {print(cos(x,y))}
  else if (op == 3) 
  {print(tan(x,y))}
  else if (op == 4)
  {return(sq(x,y))}
}

get_numbers()

if len(numbers) == 1:#if length of list is equal to 1...
  print operation_1number(numbers[0])   #run operation one, which will offer sin, cos, and tan, on first index (in this case, the only index)
else: 
  print operation_2numbers(numbers[0],numbers[1])


