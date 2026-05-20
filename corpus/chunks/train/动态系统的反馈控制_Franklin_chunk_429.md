至此，我们得到算法的设计步骤：给定一个由任意 $(A, B)$ 描述的 $n$ 阶系统和一个期望的 $n$ 阶首一特征多项式 $\alpha_{\mathrm{c}}(s)$ ，（1）取状态变换 $x = Tz$ ，把 $(A, B)$ 变换成能控标准形 $(A_{\mathrm{c}}, B_{\mathrm{c}})$ ；（2）通过观察并利用式(7.87)求出控制增益给出控制律 $u = -K_{\mathrm{c}}z$ ；（3）由于这是相对于能控形求出的增益，因此，必须将增益转换成相对初始状态的增益，从而得到 $K = K_{\mathrm{c}}T^{-1}$ 。

另一种变换方法是阿克曼(Ackermann)公式(1972年)。该公式由三步过程组成：转化为能控形 $(A_{c}, B_{c})$ ，求解增益，再转换到下面这种非常紧凑的形式：

$$
\boldsymbol {K} = \left[ \begin{array}{l l l l} 0 & \dots & 0 & 1 \end{array} \right] \boldsymbol {C} ^ {- 1} \alpha_ {\mathrm{c}} (\boldsymbol {A}) \tag {7.88}
$$

使得

$$
\boldsymbol {C} = \left[ \begin{array}{l l l l l} \boldsymbol {B} & \boldsymbol {A B} & \boldsymbol {A} ^ {2} \boldsymbol {B} & \dots & \boldsymbol {A} ^ {n - 1} \boldsymbol {B} \end{array} \right] \tag {7.89}
$$

其中：C 是 7.4 节中的可控性矩阵；n 为系统的阶数和状态变量的个数； $\alpha_{c}(A)$ 是由下式定义的矩阵：

$$\alpha_ {c} (\mathbf {A}) = \mathbf {A} ^ {n} + \alpha_ {1} \mathbf {A} ^ {n - 1} + \alpha_ {2} \mathbf {A} ^ {n - 2} + \dots + \alpha_ {n} \mathbf {I} \tag {7.90}$$

其中： $\alpha_{i}$ 是期望特征多项式(7.86)的系数。这里需要注意式(7.90)是矩阵方程。对于求阿克曼公式的导数，可参考附录 WD 及 www.fpe7e.com。
