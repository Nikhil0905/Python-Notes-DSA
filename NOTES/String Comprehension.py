# (1) HelloMyNameIsNikhil
s="HelloMyNameIsNikhil"
p=[i for i in s]
print(p)


# (2) to Join elements in List
s="HelloMyNameIsNikhil"
p="".join([i if i.islower() else " " + i for i in s])
print(p)


# (3) To do slicing in result
s="HelloMyNameIsNikhil"
p="".join([i if i.islower() else " " + i for i in s])[1:]
print(p)

# (4) Manipulation inside List
s="HelloMyNameIsNikhil"
p="".join([i if i.islower() else " " + i.lower() if i in ['I']  else " " + i for i in s])[1:]
print(p)
