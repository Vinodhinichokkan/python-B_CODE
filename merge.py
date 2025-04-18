#----------------Method1----------
name1 = {"Abi": 25,"riyaan": 2}
name2 = {"Hari": 30}

names = name1 | name2
print(names)                   #{'Abi': 25, 'riyaan': 2, 'Hari': 30}

#--------------method2-----------

name1 = {"Abi": 25,"riyaan": 2}
name2 = {"Hari": 30}

names = {**name1, **name2}
print(names)               #{'Abi': 25, 'riyaan': 2, 'Hari': 30}