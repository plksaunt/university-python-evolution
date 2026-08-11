import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
from matplotlib import rcParams
from scipy.interpolate import interp1d
from scipy.integrate import simpson,trapezoid
from scipy.signal import find_peaks
rcParams['font.sans-serif'] = ['STHeiti']  # 设置字体为中文黑体
df=pd.read_csv("/Users/plksaunt/Documents/python_数据分析/matplotlib/fluorescence_data.csv", encoding="utf-8")
print(df.head())
print(f"缺失值数量：{df.isna().sum().sum()}")
print(f"重复值数量：{df.duplicated().sum()}")
print("------------------缺失值，重复值处理后------------------")
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
print(f"缺失值数量：{df.isna().sum().sum()}")
print(f"重复值数量：{df.duplicated().sum()}")
print(f"有{int(len(df))}个数据")
plt.figure(figsize=(20,10))
plt.plot(df["Wavelength"].tolist(),df["Green"].tolist(),marker="o",color="green",label="绿色吸光度")
plt.plot(df["Wavelength"].tolist(),df["Blue"].tolist(),marker="o",color="blue",label="蓝色吸光度")
plt.plot(df["Wavelength"].tolist(),df["Purple"].tolist(),marker="o",color="purple",label="紫色吸光度")
plt.xlabel("波长")
plt.ylabel("吸光度")
plt.grid(True,axis="y")
plt.legend()
plt.title("三条吸光度变化曲线")
plt.savefig("图片/fig(all).png",dpi=300,bbox_inches="tight")
plt.close()
def model(x, a, b, c, m, n):
        # 高斯峰 + 线性背景 (m*x + n)
        gauss = a * np.exp(-(x - b)**2 / (2 * c**2))
        bg = m * x + n
        return gauss + bg
dict={}
for i in range(1,len(df.columns.to_list())):
    inner_dict={}
    ori_y=df[df.columns.to_list()[i]].to_list()
    a0=max(ori_y)
    b0=df["Wavelength"][np.argmax(ori_y)]
    c0 = (df["Wavelength"].max() - df["Wavelength"].min()) / 6
    popt,pcov=curve_fit(model,df["Wavelength"].tolist(),ori_y,p0=[a0,b0,c0,0,0])
    x_data = np.linspace(df["Wavelength"].min(), df["Wavelength"].max(), len(df))
    y_data=model(x_data,*popt)
    f_linear=interp1d(df["Wavelength"].tolist(),ori_y,kind="linear")
    x_new=np.linspace(397,737,200)
    y_linear=f_linear(x_new)
    plt.plot(x_new,y_linear,label="linear线性插值")
    plt.plot(x_data,y_data,color="red",label="拟合曲线")
    plt.xlabel("波长")
    plt.ylabel("吸光度")
    plt.title("高斯+线性背景拟合曲线 - " + str(df.columns.to_list()[i]))
    plt.legend()
    area_simpson=simpson(y_linear,x_new)
    area_trapezoid=trapezoid(y_linear,x_new)
    peaks,properties=find_peaks(y_linear,height=max(y_linear)-50,distance=5)
    print(f"-----------------{str(df.columns.to_list()[i])}-----------------")
    print("峰所在索引:", peaks)
    inner_dict["峰所在索引"]=peaks[0]
    print("峰位置 (nm):", x_data[peaks])
    inner_dict["峰位置(nm)"]=x_data[peaks][0]
    print("峰高度:", properties['peak_heights'])
    inner_dict["峰高度"]=f"{properties['peak_heights'][0]:.2f}"
    print(f"辛普森面积:{area_simpson:.2f}")
    inner_dict["辛普森面积"]=f"{area_simpson:.2f}"
    print(f"梯形法面积:{area_trapezoid:.2f}")
    inner_dict["梯形法面积"]=f"{area_trapezoid:.2f}"
    a_fit, b_fit, c_fit ,M,N= popt
    print(f"振幅a={a_fit:.2f}, 峰值波长b={b_fit:.2f} nm, 半高宽σ={c_fit:.2f} nm")
    inner_dict["振幅a"]=f"{a_fit:.2f}"
    inner_dict["峰值波长b(nm)"]=f"{b_fit:.2f}"
    inner_dict["半高宽σ(nm)"]=f"{c_fit:.2f}"
    # 计算残差（误差）
    residuals = np.array(ori_y) - model(x_data, *popt)
    # 计算 RMSE
    rmse = np.sqrt(np.mean(residuals**2))
    print(f"平均误差: {rmse:.3f}")
    inner_dict["平均误差"]=f" {rmse:.3f}"
    plt.tight_layout()
    plt.savefig(f"图片/fig{i}.png",dpi=300,bbox_inches="tight")
    plt.close()
    dict[str(df.columns.to_list()[i])]=inner_dict
new_df=pd.DataFrame(dict)
new_df.to_csv("/Users/plksaunt/Documents/python_数据分析/matplotlib/summary_of_fitting_results.csv",index=True)    
