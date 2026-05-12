import numpy as np
from elements import get_elements
elements=get_elements()
class elements_detection():
    def __init__(self,elements):
        self.elements=elements
        Z_list=[]
        weights_list=[]
        for i in range(1,21):
            Z_list.append(i)
            weights_list.append(elements[i]["weight"])
        self.Z=np.array(Z_list)
        self.weights=np.array(weights_list)
    def elements_statistic(self):
        weights_mean=np.mean(self.weights)
        weights_std=np.std(self.weights)
        weights_max=np.max(self.weights)
        weights_min=np.min(self.weights)
        symbol_list=[]
        for num in self.elements:
            w=self.elements[num]["weight"]
            if w>weights_mean:
                symbol_list.append(self.elements[num]["symbol"])
        relativity=np.corrcoef(self.Z,self.weights)[0,1]
        weights_standardized=(self.weights-weights_mean)/weights_std
        with open("D:\python_numpy\元素性质线性回归分析\countent.txt","w",encoding="utf-8") as f:
            print(f"平均质量为{weights_mean}")
            f.write(f"平均质量为{weights_mean}\n")
            print(f"标准差为{weights_std}")
            f.write(f"标准差为{weights_std}\n")
            print(f"最大质量为{weights_max}")
            f.write(f"最大质量为{weights_max}\n")
            print(f"最小质量为{weights_min}")
            f.write(f"最小质量为{weights_min}\n")
            print(f"大于平均质量的元素有{symbol_list}")
            f.write(f"大于平均质量的元素有{symbol_list}\n")
            print(f"原子序数和原子量的相关系数是{relativity}")
            f.write(f"原子序数和原子量的相关系数是{relativity}\n")
            print(f"标准化原子量数据为{weights_standardized}")
            f.write(f"标准化原子量数据为{weights_standardized}\n")
    def fit_linear_model(self):    
        X=np.column_stack([np.ones_like(self.Z),self.Z])
        w=np.linalg.inv(X.T@X)@X.T@self.weights
        self.b=w[0]#截距
        self.a=w[1]#斜率
        print(f"拟合结果：原子量={self.a}*原子序数+{self.b}")   
        weights_pred_list=[]         
        for i in self.Z:
            weights_pred_list.append(self.a*i+self.b)
        weight_pred=np.array(weights_pred_list)
        print(f"预测前二十元素质量为{weight_pred}")
        RMSE=(np.sum((weight_pred-self.weights)**2)/20)**0.5
        print(f"方均根误差是{RMSE}") 
        with open("D:\python_numpy\元素性质线性回归分析\countent.txt","a",encoding="utf-8") as f:
            f.write(f"拟合结果：原子量={self.a}*原子序数+{self.b}\n") 
            f.write(f"预测前二十元素质量为{weight_pred}\n")
            f.write(f"方均根误差是{RMSE}\n")
    def predict(self):
        if not hasattr(self, 'a') or not hasattr(self, 'b'):
            print("❌ 错误：请先调用 fit_linear_model() 拟合模型！")
            return
        num=int(input("请输入预测元素序数："))
        print("预测原子质量为：",self.a*num+self.b)   
try1=elements_detection(elements)
try1.fit_linear_model()

