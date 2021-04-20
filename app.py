'''

Source:
    https://reqres.in/api/users?page=2
    https://geeksforgeeks.org

Author: Talha

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
        print(n[i] +' :: ' + remover(str(type(m[i]))))
        
        
 def remover(s):
    if s=="<class 'str'>":
        s="string"
    else:
        if s=="<class 'int'>":
            s="integer"
        else:
            if s=="<class 'list'>":
                s="list"  
    return s        


if __name__ == "__main__":
    startpy()
