numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[0:5])
print(numbers[5:])
print(numbers[:5])
print(numbers[::2])



##normal way

number =[]
for i in range(1,6):
    number.append(i)
print(number)   # [1,2,3,4,5]

#comprehension way -one line 

numbers = [i for  i in range(1,6)]
print(numbers)

#even number
evens =  [i for  i in range(1,11) if 1%2==0]
print(evens) #[2,4,,6,8]

#squares
squares =[i*i for i in range(1,6)]
print(squares)  #[1,4,9,16,25]