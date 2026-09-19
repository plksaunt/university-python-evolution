import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error,r2_score
plt.rcParams['font.family'] = ['STHeiti']
plt.rcParams['axes.unicode_minus'] = False
df=pd.read_csv("/Users/plksaunt/Documents/machine learnin/house_data.csv")
class sklearn_model:
    def __init__(self,df):
        self.df=df
    def data_generation(self):
        arr=self.df.to_numpy()
        x=[]
        for i in range(self.df.shape[0]):
            x.append(arr[i,:-1].tolist())
        y=self.df.iloc[:,-1]
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=74)
        return  x_train,x_test,y_train,y_test
    def linear_regression(self):
        x_train,x_test,y_train,y_test=self.data_generation()
        scaler=StandardScaler()
        x_train_scaled=scaler.fit_transform(x_train)
        x_test_scaled=scaler.transform(x_test)
        model=LinearRegression()
        model.fit(x_train_scaled,y_train)
        print(f"系数w:{model.coef_}")
        print(f"截距b:{model.intercept_}")
        y_pred=model.predict(x_test_scaled)
        print("MSE(均方误差):", mean_squared_error(y_test, y_pred))
        print("R²(决定系数):", r2_score(y_test, y_pred))
class gradient_descent():
    def __init__(self,df,a,num):
        self.df=df
        self.a=a
        self.w=[0,0,0,0]
        self.b=0
        self.num=num
    def data_processing(self):
        arr=self.df.to_numpy()
        x=[]
        for i in range(self.df.shape[0]):
            x.append(arr[i,:-1].tolist())
        y=self.df.iloc[:,-1].to_numpy()
        x_np=np.array(x,dtype=float)
        for i in range(x_np.shape[1]):
            x_np[:,i]=(x_np[:,i]-np.mean(x_np[:,i]))/np.std(x_np[:,i])  
        return x_np,y
    def data_changing(self):
        x_scaled,y=self.data_processing()
        x_scaled_train=x_scaled.T
        return x_scaled,x_scaled_train,y
    def gradient_descenting(self):
        i_list=[]
        cost_list=[]
        y=self.df.iloc[:,-1].to_numpy()
        w=np.array([self.w])
        x,x_T,y=self.data_changing()
        for i in range(self.num+1):
            dw=np.dot((np.dot(w,x_T)+self.b-y),x)/y.shape[0]
            db=np.sum(np.dot(w,x_T)+self.b-y)/y.shape[0]
            w=w-self.a*dw
            self.b=self.b-self.a*db
            if i%2000==0:
                i_list.append(i)
                cost_list.append(float(np.sum((np.dot(w,x_T)+self.b-y)**2)/(2*y.shape[0])))
                print(f"迭代{i}次后，代价函数值为:{float(np.sum((np.dot(w,x_T)+self.b-y)**2)/(2*y.shape[0])):.3f}") 
                R2=1-(np.sum((np.dot(w,x_T)+self.b-y)**2))/(np.sum((y-np.mean(y))**2)) 
                print(f"迭代{i}次后，R2的值为:{R2}")              
        plt.plot(i_list,cost_list,marker="o",label="代价函数")
        plt.title("多元线性回归中代价函数值随迭代次数变化图例") 
        plt.xlabel("iterations")
        plt.ylabel("J(w,b)")
        plt.legend()
        plt.show()     
machine_regression=sklearn_model(df)
machine_regression.linear_regression()
print("---------------以下为手动梯度下降过程--------------- ")
Regression=gradient_descent(df,0.001,200000) 
Regression.gradient_descenting()       