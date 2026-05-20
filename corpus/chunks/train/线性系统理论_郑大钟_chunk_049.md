<table><tr><td> $v_{3} - v_{2} = 1$ </td><td> $v_{2} - v_{1} = 2$ </td><td> $v_{1} - v_{0} = 2$ </td></tr><tr><td> $v_{11}^{(2)} \triangle v_{11}$ </td><td> $v_{12}^{(2)} \triangle v_{12}$  $v_{11}^{(2)} \triangle (2I - A)v_{11}$ </td><td> $v_{12}^{(1)} \triangle (A - 2I)v_{12}$  $v_{11}^{(1)} \triangle (A - 2I)^{2}v_{11}$ </td></tr></table>

并且，由满足

$$(A - 2 I) ^ {3} v _ {1 1} = 0 \text {和} (A - 2 I) ^ {2} v _ {1 1} \neq 0$$

可定出一个列向量为 $v_{11} = [001000]^T$ ，从而有

$$
\boldsymbol {v} _ {\mathrm{II}} ^ {(1)} \triangleq (A - 2 I) ^ {2} \boldsymbol {v} _ {\mathrm{II}} = \left[ \begin{array}{l} 2 \\ 2 \\ 0 \\ 0 \\ 0 \\ - 0 \end{array} \right], \quad \boldsymbol {v} _ {\mathrm{II}} ^ {(2)} \triangleq (A - 2 I) \boldsymbol {v} _ {\mathrm{II}} = \left[ \begin{array}{c} 1 \\ - 1 \\ 0 \\ 0 \\ 0 \\ - 0 \end{array} \right], \quad \boldsymbol {v} _ {\mathrm{II}} ^ {(3)} \triangleq \boldsymbol {v} _ {\mathrm{II}} = \left[ \begin{array}{l} 0 \\ 0 \\ 1 \\ 0 \\ 0 \\ - 0 \end{array} \right]
$$

再由满足

$$\{\pmb {v} _ {1 2}, \pmb {v} _ {1 1} ^ {(2)} \} \text {线性无关,} (A - 2 I) ^ {2} \pmb {v} _ {1 2} = 0, (A - 2 I) \pmb {v} _ {1 2} \neq 0$$

可定出一个列向量 $v_{12} = [0 0 1 - 1 1 1]^T$ ，从而又可导出

$$
\boldsymbol {v} _ {1 2} ^ {(1)} \triangleq (A - 2 I) \boldsymbol {v} _ {1 2} = \left[ \begin{array}{r} 0 \\ 0 \\ - 2 \\ - 2 \\ 0 \\ 0 \end{array} \right], \boldsymbol {v} _ {1 2} ^ {(2)} \triangleq \boldsymbol {v} _ {1 2} = \left[ \begin{array}{r} 0 \\ 0 \\ 1 \\ - 1 \\ 1 \\ 1 \end{array} \right]
$$

④ 确定 A 的属于 $\lambda_{2}=0$ 的特征向量 $v_{1}$

由 $(A - \lambda_{i}I)v_{2} = Av_{2} = 0$ ，可定出 $A$ 的属于 $\lambda_{2} = 0$ 的一个特征向量为

$$
\boldsymbol {v} _ {2} = \left[ \begin{array}{l l l l l l} 0 & 0 & 0 & 0 & 1 & - 1 \end{array} \right] ^ {T}
$$

⑤ 组成变换阵 Q

$$
\begin{array}{l} Q = \left[ \begin{array}{l l l l l l} v _ {1 1} ^ {(1)} & v _ {1 1} ^ {(2)} & v _ {1 1} ^ {(3)} & v _ {1 2} ^ {(1)} & v _ {1 2} ^ {(2)} & v _ {2} \end{array} \right] \\ = \left[ \begin{array}{c c c c c c} 2 & - 1 & 0 & 0 & 0 & 0 \\ 2 & - 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & - 2 & 1 & 0 \\ 0 & 0 & 0 & - 2 & - 1 & 0 \\ 0 & 0 & 0 & 0 & 1 & 1 \\ - 0 & 0 & 0 & . 0 & 1 & - 1 \end{array} \right] \\ \end{array}
$$

其逆可求出为：

$$
Q ^ {- 1} = \left[ \begin{array}{c c c c c c} \frac {1}{4} & \frac {1}{4} & 0 & 0 & 0 & 0 \\ \frac {1}{2} - \frac {1}{2} & 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 1 & 0 & 0 \\ 0 & 0 & 0 - \frac {1}{2} - \frac {1}{4} & - \frac {1}{4} \\ 0 & 0 & 0 & 0 & \frac {1}{2} & \frac {1}{2} \\ 0 & 0 & 0 & 0 & \frac {1}{2} & - \frac {1}{2} \end{array} \right]
$$

⑥ 导出状态方程的约当规范形
