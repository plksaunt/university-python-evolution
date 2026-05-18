import numpy as np
class Kinetics_Analyzer():
    def __init__(self,filename):
        with open(filename) as f:
            data=f.readlines()
        if not data:
            print("请检查文件位置及内容是否不存在")    
            return
        time=[]
        conc=[]
        for line in data[1:]:
            line=line.strip()
            if not line:
                continue
            t,c=line.split(",")
            time.append(float(t))
            conc.append(float(c))
        self.time=np.array(time)    
        self.conc=np.array(conc)
        self.fit_function=None
    def fit(self):
        log_conc=np.log(self.conc)
        p=np.polyfit(self.time,log_conc,deg=1)
        self.fit_function=np.poly1d(p)
        print(f"速率常数是{-p[0]:.3f},初始浓度是{np.exp(p[1]):.3f}")
        print(f"拟合函数是{self.fit_function}")  
        pred_conc=np.exp(self.fit_function(120))
        with open("一级反应动力学数据的拟合与分析\kinetics_result.txt","w",encoding="utf-8") as f:
            f.write(f"速率常数是{-p[0]:.3f},初始浓度是{np.exp(p[1]):.3f}\n")
            f.write(f"拟合函数是{self.fit_function}\n")
            f.write(f"120min预测值为{pred_conc}\n")
    def fit_analyse(self):
        if self.fit_function is None:
            print("请先调用函数fit")
            return
        conc_pred=np.exp(self.fit_function(self.time))
        Determining_coefficient=1-np.sum((self.conc-conc_pred)**2)/np.sum((self.conc-np.mean(self.conc))**2)
        RMSE=np.sqrt(np.mean((self.conc-conc_pred)**2))
        print(f"决定系数R^2是:{Determining_coefficient}")
        print(f"均方根误差RMSE:{RMSE}")
        with open("一级反应动力学数据的拟合与分析\kinetics_result.txt","a",encoding="utf-8") as f:
            f.write(f"决定系数R^2是:{Determining_coefficient}\n")
            f.write(f"均方根误差RMSE:{RMSE}\n")
example=Kinetics_Analyzer("一级反应动力学数据的拟合与分析\kinetics_data.txt")
example.fit()
example.fit_analyse()