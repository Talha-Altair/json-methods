'''

Source:
    https://reqres.in/api/users?page=2
    https://geeksforgeeks.org

Author: Akshara, Talha, Viruksha

Printing the type of Each Element in the JSON file

'''
import json


def startpy():

    f = open ('users.json', "r")

    data = json.loads(f.read())

    c=(data["data"])

    b=(c[1])

    printer(data)

    printer(b)
    
    f.close()

def getkey(dict):
    list = []
    for key in dict.keys():
        list.append(key)
          
    return list

def getvalue(dict):
    list = []
    for key in dict.values():
        list.append(key)
          
    return list

def printer(d):
    n=(getkey(d))
    m=(getvalue(d))
    for i in range(5):
        print(n[i] +' :: ' + str(type(m[i])))


if __name__ == "__main__":
    startpy()