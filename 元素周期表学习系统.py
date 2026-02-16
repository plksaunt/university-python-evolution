def elements():
    #前20号元素字典
    elements = {
    1: {"symbol": "H", "name": "氢", "weight": 1.008, "period": 1, "group": "1A", "category": "非金属"},
    2: {"symbol": "He", "name": "氦", "weight": 4.003, "period": 1, "group": "8A", "category": "稀有气体"},
    3: {"symbol": "Li", "name": "锂", "weight": 6.941, "period": 2, "group": "1A", "category": "金属"},
    4: {"symbol": "Be", "name": "铍", "weight": 9.012, "period": 2, "group": "2A", "category": "金属"},
    5: {"symbol": "B", "name": "硼", "weight": 10.81, "period": 2, "group": "3A", "category": "半金属"},
    6: {"symbol": "C", "name": "碳", "weight": 12.01, "period": 2, "group": "4A", "category": "非金属"},
    7: {"symbol": "N", "name": "氮", "weight": 14.01, "period": 2, "group": "5A", "category": "非金属"},
    8: {"symbol": "O", "name": "氧", "weight": 16.00, "period": 2, "group": "6A", "category": "非金属"},
    9: {"symbol": "F", "name": "氟", "weight": 19.00, "period": 2, "group": "7A", "category": "非金属"},
    10: {"symbol": "Ne", "name": "氖", "weight": 20.18, "period": 2, "group": "8A", "category": "稀有气体"},
    11: {"symbol": "Na", "name": "钠", "weight": 22.99, "period": 3, "group": "1A", "category": "金属"},
    12: {"symbol": "Mg", "name": "镁", "weight": 24.31, "period": 3, "group": "2A", "category": "金属"},
    13: {"symbol": "Al", "name": "铝", "weight": 26.98, "period": 3, "group": "3A", "category": "金属"},
    14: {"symbol": "Si", "name": "硅", "weight": 28.09, "period": 3, "group": "4A", "category": "半金属"},
    15: {"symbol": "P", "name": "磷", "weight": 30.97, "period": 3, "group": "5A", "category": "非金属"},
    16: {"symbol": "S", "name": "硫", "weight": 32.07, "period": 3, "group": "6A", "category": "非金属"},
    17: {"symbol": "Cl", "name": "氯", "weight": 35.45, "period": 3, "group": "7A", "category": "非金属"},
    18: {"symbol": "Ar", "name": "氩", "weight": 39.95, "period": 3, "group": "8A", "category": "稀有气体"},
    19: {"symbol": "K", "name": "钾", "weight": 39.10, "period": 4, "group": "1A", "category": "金属"},
    20: {"symbol": "Ca", "name": "钙", "weight": 40.08, "period": 4, "group": "2A", "category": "金属"}
}
    return elements
#根据元素序列查找
def number_search(elements,number):
    found=False
    for i in elements.keys():
        if i==number:
            found=True
            break
    return found   
#根据元素符号查找
def mark_check(elements,mark):
    found=False
    for outer_key,inner_dict in elements.items():
        if inner_dict["symbol"]==mark:
            print(elements[outer_key])
            break            
#按周期显示
def period_reveal(elements,period):
   for outer_key,inner_dict in elements.items():
       if inner_dict["period"]==period:
           print(real_elements[outer_key])
#按族显示
def group_reveal(elements,group):
    if group=="1A":
        print(elements[1])
        print(elements[3])
        print(elements[11])
        print(elements[19])
    elif group=="2A":
        print(elements[4])
        print(elements[12])
        print(elements[20])
    elif group=="3A":
        print(elements[5])
        print(elements[13])
    elif group=="4A":
        print(elements[6])
        print(elements[14])
    elif group=="5A":
        print(elements[7])
        print(elements[15])
    elif group=="6A":
        print(elements[8])
        print(elements[16])
    elif group=="7A":
        print(elements[9])
        print(elements[17])
    elif group=="8A":
        print(elements[2])
        print(elements[10])
        print(elements[18])
#知识小测试
def knowledge_test(elements):
    import random
    number=random.randint(1,20)
    print(f"原子序数{number}")
    name=input("请输入该序数对应元素")
    found=False
    if elements[number]["symbol"]==name:
        found=True
    return found    
print("元素周期表学习系统")
print("该程序具有以下功能：1.显示前二十号元素\n2.按原子序数查找\n3.按元素符号查找\n4.按周期显示\n5.按族显示\n6.知识小测试")
real_elements=elements()
while True:
    choice=int(input("请输入功能对应数字(0即为停止程序)"))
    if choice==0:
        print("程序结束")
        break
    if choice<1 or choice>6:
        print("请输入正确数字")
    if choice==1:    
        print(elements())
    if choice==2:
        num=int(input("请输入元素序列：")) 
        if  number_search(real_elements,num):
            print(real_elements[num]) 
        else:
            print("请输入正确元素序列")      
    if choice==3:
        mark=input(("请输入元素符号："))
        mark_check(real_elements,mark)
    if choice==4:
        period=int(input("请输入周期(1——4)"))
        period_reveal(real_elements,period)
    if choice==5:
        group=input("请输入族数：")  
        group_reveal(real_elements,group) 
    if choice==6:
        if knowledge_test(real_elements):
            print("回答正确")      
        else:
            print("回答错误")    