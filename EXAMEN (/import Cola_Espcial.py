import Cola_Especial

maxSize = 10
arr = Cola_Especial.Cola(maxSize)

cadena =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]



arr.push(77)
arr.push(99)
arr.push(100)
arr.push(12)
arr.push(44)
arr.push(55)
arr.push(12.34)
arr.push(0)
arr.push(21)
arr.push(-17)
arr.push(22)


print("Array containing", len(arr), "items")
arr.traverse()