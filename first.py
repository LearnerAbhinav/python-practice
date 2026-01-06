#---------------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      abhin
#
# Created:     04-01-2026
# Copyright:   (c) abhin 2026
# Licence:     <your licence>
#---------------------------------------------------------------------------------------

# List :- List are changable means mutable in nature duplicate allowed hai 
nums=[1,2,3,4]

# for x in nums:
#     print(x)
    
# for i in range(len(nums)):
#     print(i,nums[i])

# i=0
# while i<len(nums):
#     print(nums[i])
#     i+=1


# for i,val in enumerate(nums):
#     print(i,val)


# # Tuple :- like list but locked
# s={1,2,3,3,4}
# print(s)

# s.add(5)
# s.remove(2)


# # Dictionary (key value)
# student={
#     "name":"Abhi",
#     "age":21,
#     "branch": "IT"
# }
# print(student["name"])

# student["age"]=22
# student["city"]="Noida"
# print(student)

# for k,v in student.items():
#     print(k,v)

nums=[1,2,3,4,5]

for i in nums:
    if i%2==0:
        print(i)