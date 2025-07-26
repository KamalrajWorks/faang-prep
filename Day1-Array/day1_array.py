#Arrays

n=int(input("Enter the size of an array "))
a=[]
for i in range(n):
  a.append(int(input()))
print(a)
maximum = a[0]
minimum = a[0]

for i in range(n):
  if maximum < a[i]:
    maximum = a[i]
  if minimum > a[i]:
    minimum = a[i]
print("Maximum value is", maximum)
print("Minimum value is", minimum)

left = 0
right = len(a)-1
for i in range(n):
  if left < right:
    a[left] , a[right] = a[right] , a[left]
    left += 1
    right -= 1
print(a)