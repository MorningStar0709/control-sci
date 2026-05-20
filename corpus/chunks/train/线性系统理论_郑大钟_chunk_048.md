$$\left\{\boldsymbol {v} _ {i 1} ^ {(k)}, k = 1, 2, \dots , r _ {i 1}; \boldsymbol {v} _ {i 2} ^ {(j)}, j = 1, 2, \dots , r _ {i 2}; \dots ; \right.\left. \boldsymbol {v} _ {i a _ {i}} ^ {(\beta)}, \beta = 1, 2, \dots , r _ {i a _ {i}} \right\} \tag {1.75}$$

必是线性无关的，其中 $r_{i1} \geqslant r_{i2} \geqslant \cdots \geqslant r_{ia_i}$ ，且有 $(r_{i1} + r_{i2} + \cdots + r_{ia_l}) = \sigma_{io}$

证 考虑到性质 1 和 $\{v_{i1}, v_{i2}, \cdots, v_{i\alpha_{j}}\}$ 为线性无关，即可证得此性质。

性质 3 矩阵 A 的属于不同特征值的广义特征向量之间必为线性无关。

证 其证明过程和性质 1 的推证过程相类同, 故略去。

（4）化为约当规范形的变换阵的组成 使具有重特征值的系统状态方程化为约当规范形的变换阵 Q，可按如下方式组成：

$$Q = \left[ Q _ {1}: \dots : Q _ {i} \right] - n \times n \text {阵} \tag {1.76}Q _ {i} = \left[ Q _ {i 1}: Q _ {i 2}: \dots : Q _ {i a _ {j}} \right] - n \times \sigma_ {i} \text {阵} \tag {1.77}Q _ {i k} = \left[ v _ {i k} ^ {(1)}, v _ {i k} ^ {(2)}, \dots , v _ {i k} ^ {(r _ {i k})} \right] - n \times r _ {i k} \text {阵} \tag {1.78}$$

其中， $i=1,2,\cdots,l,\ k=1,2,\cdots,\alpha_{i0}$

利用变换 $\hat{x}=Q^{-1}x$ ，通过推导，即可得到约当规范形（1.61）—（1.63）。具体的推导过程略去。

例 给定线性定常系统的状态方程为

$$\dot {x} = A x + B u$$

其中

$$
A = \left[ \begin{array}{c c c c c c} 3 & - 1 & 1 & 1 & 0 & 0 \\ 1 & 1 & - 1 & - 1 & 0 & 0 \\ 0 & 0 & 2 & 0 & 1 & 1 \\ 0 & 0 & 0 & 2 & - 1 & - 1 \\ 0 & 0 & 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 & 1 & 1 \end{array} \right], B = \left[ \begin{array}{c c} 1 & 0 \\ - 1 & 1 \\ 2 & 1 \\ 0 & - 1 \\ 0 & 2 \\ 1 & 0 \end{array} \right]
$$

将其化为约当规范形的计算步骤如下：

① 计算矩阵 A 的特征值

由 $\operatorname{det}(A - \lambda I) = (\lambda - 2)^5\lambda$ ，可定出其特征值为 $\lambda_1 = 2(\sigma_1 = 5)$ 和 $\lambda_2 = 0(\sigma_2 = 1)_0$

② 对 $\lambda_{1} = 2$ ，计算 $\operatorname{rank}(A - \lambda_1 I)^m, m = 0, 1, \dots$

$$
(2 I - A) ^ {0} = I, \operatorname{rank} (2 I - A) ^ {0} = 6, v _ {0} = 0
(A - 2 I) ^ {2} = \left[ \begin{array}{c c c c c c} 1 - 1 & 1 & 1 & 0 & 0 \\ 1 - 1 & - 1 & - 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 & - 1 & - 1 \\ 0 & 0 & 0 & 0 & - 1 & 1 \\ 0 & 0 & 0 & 0 & 1 & - 1 \end{array} \right], \text {rank} (A - 2 I) ^ {2} = 4 \quad v _ {1} = 6 - 4 = 2

(A - 2 I) ^ {2} = \left[ \begin{array}{c c c c c c} 0 & 0 & 2 & 2 & 0 & 0 \\ 0 & 0 & 2 & 2 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 2 & - 2 \\ 0 & 0 & 0 & 0 & - 2 & 2 \end{array} \right], \quad \text { rank } (A - 2 I) ^ {2} = 2 \quad v _ {2} = 6 - 2 = 4

(A - 2 I) ^ {3} = \left[ \begin{array}{c c c c c c} 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & - 4 & - 4 \\ - 0 & 0 & 0 & 0 & 4 & - 4 \end{array} \right], \quad \text { rank } (A - 2 I) ^ {3} = 1, \quad \nu_ {3} = 6 - 1 = 5
$$

因 $v_{3}=\sigma_{1}$ ，故计算可到此为止。

③ 确定 A 的属于 $\lambda_{1}=2$ 的 5 个线性无关的广义特征向量

首先,可列出下表:
