from elements import get_elements
elements_dict=get_elements()
print("这是分子量计算器")
symbol_check={"(":")","[":"]","{":"}"}
class Elements_calculate:
    def __init__(self,diction):
        self.weights=diction
        self.cache={}
    def Character_processing(self):
         while True:
            a=0
            example=input("请输入化学式(输入0停止)")
            if example=="0":
                break
            if not example:
                print("输入不能为空")
                continue
            if example.upper() in self.cache:
                print("该分子已缓存")  
                print(f"该分子的元素拆分为{self.cache[example]["counts"]}")
                print(f"该分子质量是{self.cache[example]["weight"]}")
                continue
            result=self.elements_calculate(example,a)
            weight_count=0
            for outer_key,inner_dict in result.items():
                for i in range(1,21):
                    if outer_key==self.weights[i]["symbol"]:
                        weight_count+=self.weights[i]["weight"]*int(inner_dict) 
            self.cache[example.upper()]={"counts":result,"weight":weight_count}            
            print(f"该分子的元素拆分为{result}") 
            print(f"该分子的相对分子质量为{weight_count}")
    def elements_calculate(self,example,a): 
                elements_count={}
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
                    elif example[a] in symbol_check:
                        a+=1
                        inner_count,a=self.elements_calculate(example,a)#将括号内的字符串递归，交给内层函数处理，同时在遇到")"的时候将内层处理的字典保存给外层的inner_count
                        num=0
                        while  a<len(example)and example[a].isdigit():#数字的请况
                            num=num*10+int(example[a])
                            a+=1 #第二个大写字母
                        if num==0:
                            num=1 
                        for elem,cnt in inner_count.items():#这一步将内层的inner_count和主的elements_count融合在一起
                            elements_count[elem]=elements_count.get(elem,0)+cnt*num  #get(elem,0)意思是如果字典中有elem，则表示这个值，没有则表示0
                    elif example[a] in symbol_check.values():
                        return elements_count,a+1#设置内层函数的出口，遇到")"后退出内层函数，同时指向数字                                                                                         
                else:
                    a+=1 
                return elements_count     
element1=Elements_calculate(elements_dict)
element1.Character_processing()                