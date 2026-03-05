from elements import elements
from utils import *

print("元素周期表学习系统")
print("该程序具有以下功能：1.显示前二十号元素\n2.按原子序数查找\n3.按元素符号查找\n4.按周期显示\n5.按族显示\n6.知识小测试")
real_elements=elements()
while True:
    try:
        choice=int(input("请输入功能对应数字(0即为停止程序)"))
    except Exception:
        print("请输入数字") 
        continue 
#用try捕获异常，continue使得这次异常被跳过，进入下一次循环      
    if choice==0:
        print("程序结束")
        break
    if choice<1 or choice>6:
        print("请输入正确数字")
    if choice==1:    
        print(real_elements)
    if choice==2:
            num=safe_int_input("请输入元素序列",min=1,max=20)       
            if  number_search(real_elements,num):
                 print(real_elements[num])     
    if choice==3:
        mark=safe_str_input("请输入元素符号：")
        result=mark_check(real_elements,mark)
        if result:
            print(result)
        else:
            print("请输入正确元素符号")    
    if choice==4:
        period=safe_int_input("请输入元素周期",min=1,max=4)
        result=period_reveal(real_elements,period)
        for i in result:
            print(i)    
    if choice==5:
        group=safe_str_input("请输入族数：") 
        result=group_reveal(real_elements,group) 
        if result:
            print(result)
        else:
            print("请输入正确族数")    
    if choice==6:
        if knowledge_test(real_elements):
            print("回答正确")      
        else:
            print("回答错误")    