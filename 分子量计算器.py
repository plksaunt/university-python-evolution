from elements import get_elements
elements_dict=get_elements()
print("这是分子量计算器")
class Elements_calculate:
    def __init__(self,diction):
        self.weights=diction
        self.cache={}
    def elements_calculate(self): 
        while True:
            example=input("请输入化学式(输入0停止)")
            if example=="0":
                break
            if example.upper() in self.cache:
                print("该分子已缓存")  
                print(f"该分子的元素拆分为{self.cache[example]["counts"]}")
                print(f"该分子质量是{self.cache[example]["weight"]}")
                continue
            elements_count={}
            a=0
            elem=""
            while a<len(example):
                if example[a].isalpha():
                    elem+=example[a]
                    a+=1   
                    while a<len(example) and example[a].islower():
                        elem+=example[a]
                        a+=1    
                    num=0
                    while  a<len(example)and example[a].isdigit():
                        num=num*10+int(example[a])
                        a+=1 
                    if num==0:
                        num=1 
                    if  elem in elements_count:
                        elements_count[elem]+=num
                        elem=""
                    else:
                        elements_count[elem]=num 
                        elem=""     
                elif example[a]=="(":
                    inner_elements={}
                    a+=1 #第一个字母
                    while a<len(example) and example[a]!=")" :
                        inner_elem=""
                        if example[a].isalpha():
                            inner_elem+=example[a]
                            a+=1 #小写字母/数字/第二个大写字母
                            while a<len(example) and example[a].islower():#小写字母的情况
                                inner_elem+=example[a]
                                a+=1 #数字/第二个大写字母   
                            num=0
                            while  a<len(example)and example[a].isdigit():#数字的请况
                                num=num*10+int(example[a])
                                a+=1 #第二个大写字母
                            if num==0:
                                num=1 
                            if  inner_elem in inner_elements:
                                inner_elements[inner_elem]+=num
                            else:
                                inner_elements[inner_elem]=num                  
                        else:
                            a+=1 
                            #循环结束后，a应该为第二个大写字母   
                    if a<len(example)and example[a]==")":
                            a+=1#括号后的数字
                            bracket_num = 0
                            while a < len(example) and example[a].isdigit():
                                bracket_num = bracket_num * 10 + int(example[a])
                                a += 1 
                            for elem, count in inner_elements.items():
                                total = count * bracket_num                  
                                inner_elements[elem] = total   
                    for key,value in inner_elements.items():
                        for outer_key,inner_value in list(elements_count.items()):
                            if outer_key==key:
                                elements_count[outer_key]+=int(value)
                            else:
                                elements_count[key]=int(value)                                                                     
                else:
                    a+=1  
            weight_count=0
            for outer_key,inner_dict in elements_count.items():
                for i in range(1,21):
                    if outer_key==self.weights[i]["symbol"]:
                        weight_count+=self.weights[i]["weight"]*int(inner_dict) 
            self.cache[example.upper()]={"counts":elements_count,"weight":weight_count}            
            print(f"该分子的元素拆分为{elements_count}") 
            print(f"该分子的相对分子质量为{weight_count}")
element1=Elements_calculate(elements_dict)
element1.elements_calculate()                