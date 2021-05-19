import matplotlib.pyplot as plt#导入库
import numpy as np 
# linspace 第一个参数序列起始值, 第二个参数序列结束值,第三个参数为样本数默认50
x = np.linspace(0, 3 * np.pi, 100)#0到3π区间100等分
y = np.sin(x)#y的函数

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.subplot(1,2,1)#显示一个FIGURE图形生成一行两列两个子图，subplot(1,2,1)后面一个1表示当前激活第一个子图。
plt.title(r'$f(x)=sin(x)$') #显示x=sinx的
plt.plot(x, y)#可以绘制点和线, 
#plt.show()

x1 = [t*0.375*np.pi for t in x]#
y1 = np.sin(x1)
plt.subplot(1,2,2)#显示一个FIGURE图形生成一行两列两个子图，subplot(1,2,2)后面一个1表示当前激活第二个子图
# plt.title(u"测试2") #注意：在前面加一个u
plt.title(r'$f(x)=sin(\omega x), \omega = \frac{3}{8} \pi$') #显示标题
plt.plot(x1, y1)
plt.show()#显示