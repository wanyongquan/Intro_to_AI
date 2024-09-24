#可视化
import matplotlib.pyplot as plt
#数据集
from sklearn.datasets import load_boston
#训练集测试集拆分
from sklearn.model_selection import train_test_split
#预处理部件
from sklearn.preprocessing import StandardScaler
#线性回归
from sklearn.linear_model import LinearRegression

#1.加载数据
boston_data = load_boston()
#print(boston_data)
#print(type(boston_data))

#数据描述
print(boston_data.DESCR)

#获取特征值
features = boston_data['data']
#获取目标值
target = boston_data['target']
#获取特征值名称
feature_names = boston_data['feature_names']

#2 模型训练
# 将特征值与目标值拆分成训练集与测试集
#训练集：测试集=7：3
#返回值：特征值（训练集特征值、测试集特征值）、目标值（训练集目标值、测试集目标值）
#固定数据集
x_train,x_test,y_train,y_test = train_test_split(features,target,test_size=0.3,random_state=1)

print("x_test:\n",x_test)
print("x_train:\n",x_train)

#缺失、异常值处理
#没有缺失值——不需处理

#标准化
#创建实例
stand = StandardScaler()

#标准化转换 (目标值不需要转化)
x_train = stand.fit_transform(x_train)
x_test = stand.fit_transform(x_test)

print(x_train)
print(x_test)

# 构建线性模型——简单线性回归模型（不优化）
#构建线性回归实例
lr = LinearRegression()

#训练数据
lr.fit(x_train,y_train)

#3. 预测数据
y_predict = lr.predict(x_test)

#获取线性回归的权重与偏置
weight = lr.coef_
bais = lr.intercept_
print("weight:\n",weight)
print("bais:\n",bais)

#评估模型——准确率
score = lr.score(x_test,y_test)
print("准确率：\n",score)



#4. 可视化 绘制真实房价走势 与预测的房价走势
#创建画布
plt.figure()

#绘图-准备数据

x = [i for i in range(len(y_predict))]

plt.plot(x,y_test)
plt.plot(x,y_predict)

plt.legend(['真实值','预测值'])

#修改rc参数，增加支持中文
plt.rcParams['font.sans-serif']='SimHei'
#修改rc参数，增加支持负号
plt.rcParams['axes.unicode_minus']=False

plt.title("波士顿房价走势真实与预测值")
#展示
plt.show()