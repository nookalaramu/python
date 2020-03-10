# Take 5 different names from user which should have first name middle name and last name ,
# and should be stored in List called as "nameList" Example:
# 1) suresh kumar angadi
# 2) basappa chennappa gadad
# 3) rakesh kumar miskin
# 4) rithwik ullagaddi mathad
# 5) shankar gowda kumar

# 1)Suresh K.A
# 2)Basappa C.G
# 3)Rakesh K.M
# 4)Rithwik U.M
# 5)Shankar G.K

nameList = ["suresh kumar angadi","basappa chennappa gadad","rakesh kumar miskin","rithwik ullagaddi mathad","shankar gowda kumar"]
print(nameList)
updateList=[]
for i in nameList:
    separate = i.split()
    fname = separate[0].capitalize()
    mname = separate[1][:1].capitalize()
    lname = separate[2][:1].capitalize()
    uname = fname + " " + mname + "."+lname
    updateList.append(uname)
print("Given Name List as ", nameList)
print("Name List is converted to short form as :")
for j in updateList:
    print(j)
    