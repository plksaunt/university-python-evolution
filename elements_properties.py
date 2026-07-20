import pandas as pd
import numpy as np
df = pd.read_csv("/Users/plksaunt/Documents/python_数据分析/pandas与numpy综合/elements_properties.csv", encoding="utf-8")
#数据清洗
print(df.isna().sum())
print(df.duplicated().any())
print(f"重复值数量:{df.duplicated().sum()}")
print(f"缺失值数量:{df.isna().sum().sum()}")
nanum=df[["discovery_year","electronegativity"]].isna().any(axis=1).sum()
print(f"缺失值占总行数比例：{round(nanum/len(df)*100,3)}%")
df["electronegativity"]=df["electronegativity"].fillna(df["electronegativity"].median())
df["discovery_year"]=df["discovery_year"].fillna(df["discovery_year"].mean())
df=df.drop_duplicates(keep="first")
print("---------------------数据清理后---------------------")
print(f"重复值数量:{df.duplicated().sum()}")
print(f"缺失值数量:{df.isna().sum().sum()}")
print(df["boiling_point"]/df["melting_point"])
class elements_analyse:
    def __init__(self,df):
        self.df=df
    def initial_exploration(self):
        print(f"文件前五行：\n{self.df.head()}")   
        print(f"文件后五行：\n{self.df.tail()}")
        print("基本信息:")
        self.df.info()
    def fundenmental_analyse(self):
        print(f"atomic_weight均值:{self.df["atomic_weight"].mean():3f}\n中位数:{self.df["atomic_weight"].median()}\n标准差:{self.df["atomic_weight"].std():3f}\n最小值:{self.df["atomic_weight"].min()}\n最大值:{self.df["atomic_weight"].max()}")  
        print(f"electronegativity均值:{self.df["electronegativity"].mean():3f}\n中位数:{self.df["electronegativity"].median()}\n标准差:{self.df["electronegativity"].std():3f}\n最小值:{self.df["electronegativity"].min()}\n最大值:{self.df["electronegativity"].max()}") 
        print(f"melting_point均值:{self.df["melting_point"].mean():3f}\n中位数:{self.df["melting_point"].median()}\n标准差:{self.df["melting_point"].std():3f}\n最小值:{self.df["melting_point"].min()}\n最大值:{self.df["melting_point"].max()}")       
        print(f"原子量最大的五个元素:\n{self.df.loc[self.df["atomic_weight"].nlargest(5).index,"symbol"]}")
        print(f"密度最小的五个元素:\n{self.df.loc[self.df["density"].nsmallest(5).index,"symbol"]}")
        print(f"元素分类:\n{self.df["category"].value_counts()}")
    def groupby_analyse(self):
        result1=self.df.groupby("category")[["atomic_weight","density"]].mean()
        print(result1.sort_values(["atomic_weight"],ascending=False))
        result2=df["period"].value_counts().sort_index()
        for i in result2.index:
            print(f"第{i}周期有{result2.loc[i]}个元素")
        result3=self.df.groupby("group")[["electronegativity"]].median()
        print(result3)
        result3_index=result3.idxmax()
        print(f"最大的一组为:\n{result3.max().tolist()}\n组序数是{result3_index.tolist()}")    
    def Condition_Filtering_Sorting (self):
        df1=self.df[(self.df["category"]=="金属")&(self.df["density"]>5)] 
        print("密度大于5的金属元素")  
        print(df1.sort_values("atomic_weight"))
        df2=self.df[self.df["discovery_year"]>1800]
        print(f"晚于1800年发现的元素\n{df2["symbol"]}")
        ratio=self.df["boiling_point"]/self.df["melting_point"]
        top_3=ratio.nlargest(3)
        print(f"比值前三大的元素是\n{self.df.loc[top_3.index.tolist(),"symbol"]}")
    def correlation_analyse(self):
        print(f"原子序数与原子量的相关系数:{np.corrcoef(self.df["atomic_number"].tolist(),self.df["atomic_weight"].tolist())[0,1]}")
        print(f"原子序数与电负性的相关系数:{np.corrcoef(self.df["atomic_number"].tolist(),self.df["electronegativity"].tolist())[0,1]}")
        columns = ["atomic_weight", "electronegativity", "density", "melting_point"]
        correlation_matrix = np.corrcoef(self.df[columns], rowvar=False)
        df1=pd.DataFrame(correlation_matrix,index=["atomic_weight","electronegativity","density","melting_point"],columns=["atomic_weight","electronegativity","density","melting_point"])
        print(f"原子量，电负性，密度，熔点的相关系数列表:\n{df1}")
    def feature_construction(self):
        self.df["temperature_range"]=self.df["boiling_point"]-self.df["melting_point"]    
        self.df["density_rank"]=pd.cut(self.df["density"],[0,1,5,100],labels=["低","中","高"],precision=0,include_lowest=True)
        print("添加温度范围并对密度分箱后:")
        print(self.df.tail())
        print(f"温度范围数据汇总:\n{self.df["density_rank"].value_counts()}")
while True:
    try:
        A=elements_analyse(df)
        num=int(input("1.初步探索\n2.基本统计分析\n3.分组聚合\n4.条件筛选与排序\n5.相关性分析\n6.新特征构造\n7.结束"))
        if num==1:
            A.initial_exploration()
        elif num==2:
            A.fundenmental_analyse()
        elif num==3:
            A.groupby_analyse()
        elif num==4:
            A.Condition_Filtering_Sorting()
        elif num==5:
            A.correlation_analyse()
        elif num==6:
            A.feature_construction()
        elif num==7:
            break     
        else:
            print("请输入1到7之间的数字")                   
    except Exception:
        print("请输入有效数字")