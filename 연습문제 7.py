#1부터 100까지 수
#2의 배수는 numbers_1
#3의 배수는 numbers_2
#5의 배수는 numbers_3

#
# a = 0
# while a<100 :
#     a = a + 1
#     print(0+a)
#

# numbers_1 = 0
# while numbers_1<100:
#     numbers_1 = numbers_1+1
#     if numbers_1%2 == 0:
#         print(numbers_1)

numbers_1 = []
numbers_2 = []
numbers_3 = []

for i in range(1, 101):
    if i % 2 == 0:
        numbers_1.append(i)
    if i % 3 == 0:
        numbers_2.append(i)
    if i % 5 == 0:
        numbers_3.append(i)
print(numbers_1)
print(numbers_2)
print(numbers_3)


