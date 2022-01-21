#FUNCTION 1
def function_1(Name,age,marks,subject,is_passed,higest_marks,salary):
    print(f"My name is {Name}\
 i am {age}yrs old\
 scored {marks}\
 in subject {subject}\
 and haved passed: {is_passed}\
 my higest score is {higest_marks}\
 and earns Rs-{salary}")    
function_1('Sahil',19,(90,89.11,93),["Maths","DS","CG"],True,{"CG":93},15000.00)

#FUNCTION-2
def function_2(a):
    for key,values in a.items():
        print(f"key is: {key} and its value is: {values}")
dict = {
    'Name':'SAHIL GAIKWAD',
    'Age':19,
    'Marks':91.67,
    'Place':'Navi Mumbai',
    'subject':'CG,DS,Maths',
    'salary': 19000.00
}  
function_2(dict)

#FUNCTION-3
def function_3():
    Name = "Sahil Gaikwad"
    Age = 19   
    return [Name, Age];  
    
list = function_3() 
print(list)
 


