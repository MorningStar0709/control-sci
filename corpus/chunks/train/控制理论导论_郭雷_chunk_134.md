(ii) 系统 (1.9.1) 的系数矩阵满足秩关系式

$$
\operatorname{rank} \left[ \begin{array}{c c} \boldsymbol {A} & \boldsymbol {B} \\ \boldsymbol {C} & 0 \end{array} \right] = n + m, \tag {1.9.10}
$$

其中 $n$ 为系统的维数， $m$ 为输出（和输入）的维数，且 $\pmb{L}$ 为非奇异.

证明 当 $(A - BK)$ 非奇异时，由于

$$
\begin{array}{l} \left[ \begin{array}{c c} I _ {n} & 0 \\ 0 & C (A - B K) ^ {- 1} B \end{array} \right] = \left[ \begin{array}{c c} I _ {n} & 0 \\ - C (A - B K) ^ {- 1} & I _ {m} \end{array} \right] \left[ \begin{array}{c c} A - B K & B \\ C & 0 \end{array} \right] \\ \times \left[ \begin{array}{c c} (\boldsymbol {A} - \boldsymbol {B K}) ^ {- 1} & (\boldsymbol {A} - \boldsymbol {B K}) ^ {- 1} \boldsymbol {B} \\ 0 & - I _ {m} \end{array} \right] \\ \end{array}
$$

和

$$
\left[ \begin{array}{c c} \boldsymbol {A} - \boldsymbol {B} \boldsymbol {K} & \boldsymbol {B} \\ C & 0 \end{array} \right] = \left[ \begin{array}{c c} \boldsymbol {A} & \boldsymbol {B} \\ \boldsymbol {C} & 0 \end{array} \right] \left[ \begin{array}{c c} I _ {n} & 0 \\ - \boldsymbol {K} & I _ {m} \end{array} \right],
$$

所以

$$
\operatorname{rank} \left[ \begin{array}{c c} I _ {n} & 0 \\ 0 & C (A - B K) ^ {- 1} B \end{array} \right] = \operatorname{rank} \left[ \begin{array}{l l} A & B \\ C & 0 \end{array} \right]. \tag {1.9.11}
$$

充分性．因系统(1.9.1)能用状态反馈镇定，故可取K使 $(A-BK)$ 的特征值均具有负实部，从而保证了 $(A-BK)$ 为非奇异，进而由式(1.9.10)，(1.9.11)得

$$\operatorname{rank} C (A - B K) ^ {- 1} B = m.$$

这表明 $C(A - BK)^{-1}B$ 非奇异，故可取

$$\boldsymbol {L} = - \left[ C (\boldsymbol {A} - \boldsymbol {B K}) ^ {- 1} \boldsymbol {B} \right] ^ {- 1} \widetilde {\boldsymbol {D}},$$

其中

$$
\widetilde {D} = \left[ \begin{array}{c c c} \widetilde {d} _ {1 1} & & \\ & \ddots & \\ & & \widetilde {d} _ {m m} \end{array} \right], \quad \widetilde {d} _ {i i} \neq 0,
$$

并且在上述 $K, L$ 的选取下，闭环系统为渐近稳定，同时成立

$$
\begin{array}{l} \lim _ {s \rightarrow 0} G _ {K L} (s) = \lim _ {s \rightarrow 0} C (s I - A + B K) ^ {- 1} B L \\ = - \left[ C (A - B K) ^ {- 1} B \right] \cdot \left\{- \left[ C (A - B K) ^ {- 1} B \right] ^ {- 1} \tilde {D} \right\} = \tilde {D}, \\ \end{array}
$$

且为非奇异对角线常阵. 在满足条件 (i), (ii) 下, 必存在 $(K, L)$ , 使系统 (1.9.1) 实现静态解耦.

必要性. 根据定义, 系统 (1.9.1) 可实现静态解耦, 当且仅当存在 $(K, L)$ 使闭环系统为渐近稳定, 且 $G_{KL}(0) = -C(A - BK)^{-1}BL$ 为非奇异对角阵. 于是由闭环系统的渐近稳定要求知条件 (i) 成立. 再由 $L$ 的非奇异性知, $G_{KL}(0)$ 非奇异等价于 $C(A - BK)^{-1}B$ 非奇异. 进而由式 (1.9.11) 知条件 (ii) 成立. 所以必要性得证.
