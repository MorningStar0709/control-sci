定理 11.9.5 系统 (11.9.5) 的阵 A 与阵 $I_{c}$ 经置换阵 Q (这里单位元为 [0], 零元为 $[\varepsilon]$ ) 的坐标变换后，具有以下标准结构

$$
\widehat {\boldsymbol {A}} = \left[ \begin{array}{c c} \boldsymbol {A} _ {1 1} & \phi \\ \boldsymbol {A} _ {2 1} & \boldsymbol {A} _ {2 2} \end{array} \right], \quad \widehat {\boldsymbol {I}} _ {c} = \left[ \begin{array}{c c} \phi & \phi \\ \phi & I _ {2} \end{array} \right],
$$

其中 $\phi$ 是元素均为 $[\varepsilon]$ 的阵， $A_{11}$ 和 $A_{22}$ 为左下块三角标准形， $I_2$ 的对角线上元素包含了 $I_c$ 中所有[0]元素，其他元素均为 $[\varepsilon]$ : $\hat{A}$ 与 $\hat{I}_c$ 的分块相同，方阵 $A_{22}$ 对应的状态分量为全部能达分量.

以上两定理的证明完全类似于11.5节中的相应定理，此处略去.

对于能观测性也有类似结果，可参见文献[30].

下面研究监控问题. 近几年研究 TEG 的监控时提出了能控序列这一个重要概念. 系统 (11.9.5) 的能控序列 $y$ 为以下方程的解:

$$\boldsymbol {A} ^ {*} \left(\boldsymbol {I} _ {c} \boldsymbol {y} \oplus \boldsymbol {v}\right) = \boldsymbol {y}. \tag {11.9.6}$$

由双子代数方程的解法，可得最小解

$$\boldsymbol {y} = \left(\boldsymbol {A} ^ {*} \boldsymbol {I} _ {c}\right) ^ {*} \boldsymbol {A} ^ {*} \boldsymbol {v}. \tag {11.9.7}$$

下面应用定理 11.9.5, 把 y 的分量分为 3 类, 揭示出这 3 类分量本质上不同的特点, 并使求解 y 的方法简化.

不失一般性，可设系统(11.9.5)的 $A, I_{c}$ 已化为定理11.9.5的标准结构，并设经坐标变换后 $I_{c}$ 中的0元素已集中在阵 $\hat{I}_{c}$ 对角线的右下方，即

$$
\hat {\boldsymbol {A}} = \left[ \begin{array}{c c c} \boldsymbol {A} _ {1 1} & \phi & \phi \\ \boldsymbol {A} _ {2 1} & \boldsymbol {A} _ {2 2} & \boldsymbol {A} _ {2 3} \\ \boldsymbol {A} _ {3 1} & \boldsymbol {A} _ {3 2} & \boldsymbol {A} _ {3 3} \end{array} \right], \quad \hat {\boldsymbol {I}} _ {c} = \left[ \begin{array}{c c c} \phi & \phi & \phi \\ \phi & \phi & \phi \\ \phi & \phi & \boldsymbol {I} \end{array} \right], \tag {11.9.8}
$$

其中 I 为 N 阶单位阵， $\hat{A}$ 和 $\hat{I}_{c}$ 的分块相同， $A_{11}$ 和 $A_{22}$ 为方阵， $A_{11}$ 对应于不能达分量。坐标变换对于向量 y, v 仅是改变了各分量的排列次序，记坐标变换后的向量为 $\hat{y}, \hat{v}$ 。于是式 (11.9.6) 变为

$$\widehat {\boldsymbol {A}} ^ {*} (\widehat {\boldsymbol {I}} _ {c} \widehat {\boldsymbol {y}} \oplus \widehat {\boldsymbol {v}}) = \widehat {\boldsymbol {y}}, \tag {11.9.9}$$

其中 $\hat{\pmb{y}} = [y_1, y_2, y_3]^{\mathrm{T}}, \hat{\pmb{v}} = [v_1, v_2, v_3]^{\mathrm{T}}$ . 向量的分块与阵 $\hat{\pmb{A}}$ 一致. 由分块阵的乘法法则和 $\hat{\pmb{A}}^*$ 的定义, 易知 $\hat{\pmb{A}}^*$ 仍在 $\hat{\pmb{A}}$ 的 $\phi$ 块处保持为 $\phi$ 块, 即 $\hat{\pmb{A}}^*$ 有形式
