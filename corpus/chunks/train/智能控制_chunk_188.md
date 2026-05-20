# 2. 按模糊控制的线性特性分类

对开环模糊控制系统 S, 设输入变量为 u, 输出变量为 v。对任意输入偏差 $\Delta u$ 和输出偏差 $\Delta v$ , 满足 $\frac{\Delta v}{\Delta u} = k, u \in U, v \in V$ 。

定义线性度 $\delta$ ，用于衡量模糊控制系统的线性化程度，即

$$\delta = \frac {\Delta v _ {\max}}{2 \xi \Delta u _ {\max} m} \tag {4.3}$$

式中， $\Delta v_{\max}=v_{\max}-v_{\min},\Delta u_{\max}=u_{\max}-u_{\min},\xi$ 为线性化因子，m 为模糊子集 V 的个数。

设 $k_{0}$ 为一经验值，则定义模糊系统的线性特性为：① 当 $\left|k-k_{0}\right|\leqslant\delta$ 时，系统 S 为线性模糊系统；② 当 $\left|k-k_{0}\right|>\delta$ 时，系统 S 为非线性模糊系统。
