from elements import elements
real_elements=elements()
#根据元素序列查找
def number_search(elements,number):
    return number in elements
#直接判断number是否在elements里，返回True，False
#根据元素符号查找
def mark_check(elements,mark):    
    for outer_key,inner_dict in elements.items():
        if inner_dict["symbol"]==mark:
           return inner_dict
    return None            
#按周期显示
def period_reveal(elements,period):
   result=[]  
   for outer_key,inner_dict in elements.items():
       if inner_dict["period"]==period:
          result.append(inner_dict)
   return result    
#按族显示
def group_reveal(elements,group):
    result=[]
    for outer_key,inner_dict in elements.items():
        if inner_dict["group"]==group:
            result.append(inner_dict)
    return result   
 #知识小测试
def knowledge_test(elements):
    import random
    number=random.randint(1,20)
    print(f"原子序数{number}")
    name=input("请输入该序数对应元素").strip().capitalize()
    found=False
    if elements[number]["symbol"]==name:
        found=True
    return found   
#数字输入安全函数
def safe_int_input(advice,min,max):
    while True:
        try:
            value=int(input(advice))
        except Exception:
            print("请输入正确内容")
            continue
        if value<min or value>max:
            print(f"请输入正确元素信息,介于{min}和{max}之间")  
            continue
        return value      
#字符串非空安全函数
def safe_str_input(prompt):
    while True:
        value=input(prompt).strip()
        if value:
            return value
        else:
            print("输入内容不能为空")