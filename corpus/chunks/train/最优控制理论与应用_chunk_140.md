$$\boldsymbol {X} _ {k + 1} = \boldsymbol {\Phi} _ {k + 1, k} \boldsymbol {X} _ {k} + \boldsymbol {\Gamma} _ {k} \boldsymbol {U} _ {k} + \boldsymbol {W} _ {k} \tag {8-14}\boldsymbol {Z} _ {k + 1} = \boldsymbol {H} _ {k + 1} \boldsymbol {X} _ {k + 1} + \boldsymbol {V} _ {k + 1} \tag {8-15}$$

其中 $W_{k}, V_{k}$ 是零均值高斯分布的白噪声，满足

$$E \left[ \boldsymbol {W} _ {k} \right] = 0 \quad E \left[ \boldsymbol {W} _ {k} \boldsymbol {W} _ {j} ^ {\mathrm{T}} \right] = \boldsymbol {Q} _ {k} \boldsymbol {\delta} _ {k j}E \left[ \boldsymbol {V} _ {k} \right] = 0 \quad E \left[ \boldsymbol {V} _ {k} \boldsymbol {V} _ {j} ^ {\mathrm{T}} \right] = \boldsymbol {R} _ {k} \boldsymbol {\delta} _ {k j}E \left[ \boldsymbol {W} _ {k} \boldsymbol {V} _ {j} ^ {\mathrm{T}} \right] = 0 \tag {8-16}$$

对于这样一类线性随机系统,在设计最优反馈控制时,由于状态向量 $X_{k}$ 的随机性,式(8-8)所表示的性能指标也是随机变量,直接考虑它的最小化问题是没有意义的。把式(8-8)的数学期望作为随机最优控制的指标函数并省去 $\frac{1}{2}$ 这个因子。

$$
\begin{array}{l} J = E \left\{\boldsymbol {X} _ {N} ^ {\mathrm{T}} \boldsymbol {P} _ {N} \boldsymbol {X} _ {N} + \sum_ {k = 0} ^ {N - 1} \left(\boldsymbol {X} _ {k} ^ {\mathrm{T}} \overline {{{\boldsymbol {Q}}}} _ {k} \boldsymbol {X} _ {k} + \boldsymbol {U} _ {k} ^ {\mathrm{T}} \overline {{{\boldsymbol {R}}}} _ {k} \boldsymbol {U} _ {k}\right) \right\} \\ = E \left\{\sum_ {k = 0} ^ {N} \left(\boldsymbol {X} _ {k} ^ {\mathrm{T}} \overline {{\boldsymbol {Q}}} _ {k} \boldsymbol {X} _ {k} + \boldsymbol {U} _ {k - 1} ^ {\mathrm{T}} \overline {{\boldsymbol {R}}} _ {k - 1} \boldsymbol {U} _ {k - 1}\right) \right\} \tag {8-17} \\ \end{array}
$$

其中 $\overline{\pmb{Q}}_N = \pmb{P}_N$ (8-18)

注意,为了与噪声方差阵符号区分,这里把加权阵改为 $\overline{Q}_{k},\overline{R}_{k}$ 。

对于线性高斯随机系统式(8-14)、(8-15)的最优控制问题,就是要求找到一组最优控制量 $U_{0}$ 、 $U_{1}$ 、…、 $U_{N-1}$ 使指标函数式(8-17)取得极小值。对于这种LQG问题,最优控制规律可按确定性系统式(8-7)来求,只是将状态变量的反馈改为状态变量估计值的反馈,这就是分离定理。将它表达如下:

分离定理 对于由方程(8-14)、(8-15)以及指标函数式(8-17)所描述的线性高斯随机控制系统,其最优控制为

$$\boldsymbol {U} _ {k} = - \boldsymbol {\Lambda} _ {k + 1} \boldsymbol {\Phi} _ {k + 1, k} \hat {\boldsymbol {X}} _ {k} \tag {8-19}$$

其中 $X_{k}$ 是 $X_{k}$ 的最优线性滤波估计， $A_{k+1}$ 的求法与确定性系统的公式 (8-10) 相同。

证明 用第6章中动态规划的最优性原理来证明。从最后一区间向后倒退计算，即依次计算 $U_{N-1}, U_{N-2}, \cdots, U_0$ 。
