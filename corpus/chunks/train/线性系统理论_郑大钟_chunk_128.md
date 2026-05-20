$\overline{B}_{o}$ 无特殊形式 (3.203)

式(3.202)中用“\*”表示的元为可能的非零元。

龙伯格规范形 下面，简要地给出有关龙伯格能控规范形和龙伯格能观测规范形的有关结果。

结论1 对完全能控的多输入-多输出线性定常系统（3.178）， $\operatorname{rank} B = r$ ，并按行搜索方案找出其能控性矩阵 $Q_{c}$ 的 $n$ 个线性无关的列，且表

$$P ^ {- 1} = \left[ b _ {1}, A b _ {1}, \dots , A ^ {\mu_ {1} - 1} b _ {1}; b _ {2}, A b _ {2}, \dots , A ^ {\mu_ {2} - 1} b _ {2}; \dots ; b _ {r}, A b _ {r}, \dots , A ^ {\mu_ {r} - 1} b _ {r} \right] \tag {3.204}$$

其中， $\left\{\mu_{1},\mu_{2},\cdots,\mu_{r}\right\}$ 为系统的能控性指数集， $\mu_{1}+\mu_{2}+\cdots+\mu_{r}=n$ 。再令

$$
P = \left[ \begin{array}{c} \boldsymbol {e} _ {1 1} ^ {T} \\ \vdots \\ \boldsymbol {e} _ {1 \mu_ {1}} ^ {T} \\ \hdashline \vdots \\ \vdots \\ \hdashline \boldsymbol {e} _ {r 1} ^ {T} \\ \vdots \\ \vdots \\ \boldsymbol {e} _ {r \mu r} ^ {T} \end{array} \right] \tag {3.205}
$$

进而取 P 的每个块阵中的末行 $e_{1\mu_{1}}^{T}, e_{2\mu_{2}}^{T}, \cdots, e_{r\mu_{r}}^{T}$ 来构成变换矩阵

$$
S ^ {- 1} = \left[ \begin{array}{c} \boldsymbol {e} _ {1 \mu_ {1}} ^ {T} \\ \boldsymbol {e} _ {1 \mu_ {1}} ^ {T} A \\ \vdots \\ \boldsymbol {e} _ {1 \mu_ {1}} ^ {T} A ^ {\mu_ {1} - 1} \end{array} \right]

\left[ \begin{array}{c} - \\ \vdots \\ \vdots \\ \hline e _ {r \mu_ {r}} ^ {T} \\ e _ {r \mu_ {r}} ^ {T} A \\ \vdots \\ e _ {r \mu_ {r}} ^ {T} A ^ {\mu_ {r} - 1} \end{array} \right] \tag {3.206}
$$

则通过引入线性非奇异变换 $x = S^{-1}x$ ，即可导出系统的龙伯格能控规范形为：

$$
\begin{array}{l} \Sigma_ {e L}: \quad \dot {\hat {x}} = \hat {A} _ {e} \hat {x} + \hat {B} _ {e} u \\ y = \hat {C} _ {e} \hat {x} \end{array} \tag {3.207}
$$

其中

$$
\hat {A} _ {s} = S ^ {- 1} A S = \left[ \begin{array}{c c c} \hat {A} _ {1 1} & \dots & \hat {A} _ {1 r} \\ \vdots & & \vdots \\ \hat {A} _ {r 1} & \dots & \hat {A} _ {r r} \end{array} \right] \tag {3.208}

\hat {A} _ {\left(\mu_ {i} \times \mu_ {j}\right)} = \left[ \begin{array}{c c c c c} 0 & 1 & & & \\ \vdots & & \cdot & & \\ \vdots & & & \cdot & \\ 0 & & & & 1 \\ \hline * & - & * & \dots & * \end{array} \right], i = 1, 2, \dots , r \tag {3.209}

\hat {A} _ {\left(u _ {i \times} ^ {i j}\right)} = \left[ \begin{array}{c c c} 0 & \dots & 0 \\ \vdots & & \vdots \\ \vdots & & \vdots \\ 0 & \dots & 0 \\ * & \dots & * \end{array} \right], \quad i \neq j \tag {3.210}

\hat {B} _ {\varepsilon_ {(n \times p)}} = S ^ {- 1} B = \left[ \begin{array}{c c c c c c c c} 0 & & & & * & \dots & * \\ \vdots & & & & & & \\ 0 & & & & & & \\ 1 & * & & & \vdots & & \vdots \\ - & \ddots & & & \vdots & & \vdots \\ & & 0 & & & & \\ & & \vdots & & & \\ & & 0 & & & \\ & & 1 & * & \dots & * \end{array} \right] ^ {2)} \tag {3.211}
\hat {C} _ {\text {(4×s)}} = C S (\text {无特殊形式}) \tag {3.212}
$$

上述关系式中，用“\*”表示的元为可能的非零元
