numbers = [9, 15, 2, 36]
numbers[1:4] = [20, 14, 36]
print(numbers)

person_info = {"name": "Sakib", "salary": 80000}
value = person_info.get("salary")
print(value)
try:
    result =20//5
except:
    print("error happened")
finally:
    print("finally here")