结论 存在 $\{K, L\}$ ，可使受控系统（5.123）实现静态解耦的充分必要条件是

(i) 受控系统是用状态反馈能镇定的。

(ii) 受控系统的系数矩阵满足秩关系式:

$$
\operatorname{rank} \left[ \begin{array}{l l} A & B \\ C & 0 \end{array} \right] = n + p \tag {5.129}
$$

其中，n 为系统的维数，p 为输出(和输入)的维数，且 L 为非奇异。

证 分成三步来证明:

① 首先,要证明

$$
\operatorname{rank} \left[ \begin{array}{c c} I _ {s} & 0 \\ 0 & C (A - B K) ^ {- 1} B \end{array} \right] = \operatorname{rank} \left[ \begin{array}{l l} A & B \\ C & 0 \end{array} \right] \tag {5.130}
$$

为此，设 $(A - BK)^{-1}$ 存在，则由

$$
\left[ \begin{array}{c c} I _ {n} & 0 \\ 0 & C (A - B K) ^ {- 1} B \end{array} \right] = \left[ \begin{array}{c c} I _ {n} & 0 \\ - C (A - B K) ^ {- 1} & I _ {p} \end{array} \right] \left[ \begin{array}{c c} A - B K & B \\ C & 0 \end{array} \right]

\circ \left[ \begin{array}{c c} (A - B K) ^ {- 1} & (A - B K) ^ {- 1} B \\ 0 & - I _ {p} \end{array} \right] \tag {5.131}
$$

和

$$
\left[ \begin{array}{c c} A - B K & B \\ C & 0 \end{array} \right] = \left[ \begin{array}{l l} A & B \\ C & 0 \end{array} \right] \left[ \begin{array}{l l} I _ {s} & 0 \\ - K & I _ {p} \end{array} \right] \tag {5.132}
$$

即可导出(5.130)。

② 其次，证明充分性。已知受控系统能用状态反馈镇定，故取 $K$ 使 $(A - BK)$ 的特征值均具有负实部，从而保证了 $(A - BK)$ 为非奇异，也即 $(A - BK)^{-1}$ 存在。进而，由(5.129)和(5.130)，可以导出

$$\operatorname{rank} C (A - B K) ^ {- 1} B = p \tag {5.133}$$

表明 $C(A - BK)^{-1}B$ 为非奇异，故可取

$$L = - \left[ C (A - B K) ^ {- 1} B \right] ^ {- 1} \widetilde {D} \tag {5.134}$$

其中

$$
\tilde {D} = \left[ \begin{array}{c c c} \tilde {d} _ {i i} & & \\ & \ddots & \\ & & \tilde {d} _ {p p} \end{array} \right], \quad \tilde {d} _ {i i} \neq 0 \tag {5.135}
$$

并且，在上述 $\{K, L\}$ 的选取下，闭环系统为渐近稳定，同时成立

$$
\begin{array}{l} \lim _ {s \rightarrow 0} G _ {K L} (s) = \lim _ {s \rightarrow 0} C (s I - A + B K) ^ {- 1} B L \\ = - \left[ C (A - B K) ^ {- 1} B \right] \cdot \left\{- \left[ C (A - B K) ^ {- 1} B \right] ^ {- 1} \widetilde {D} \right\} = \widetilde {D} \tag {5.136} \\ \end{array}
$$

也即其为非奇异对角线常阵。这说明，在满足结论的两个条件下，必存在 $\{K, L\}$ ，使受控系统实现静态解耦。充分性得证。

③ 最后, 证明必要性。根据定义, 受控系统可实现静态解耦, 当且仅当存在 $\{K, L\}$ , 使闭环系统为渐近稳定, 且 $G_{KL}(0) = -C(A - BK)^{-1}BL$ 为非奇异对角线阵。于是, 由闭环系统的渐近稳定要求条件 (i) 成立。再因 $L$ 为非奇异, 因此由此可知, $G_{KL}(0)$ 的非奇异等价于 $C(A - BK)^{-1}B$ 的非奇异。从而, 由此并利用 (5.130) 又可知, 这即等同于要求条件 (ii) 成立。所以, 必要得证。至此, 整个证明完成。

而且，不难看出，上述证明过程中还提供了寻找 $\{K, L\}$ 使受控系统实现静态解耦的算法。现将其加以归纳，可列出算法的主要步骤为：

第1步：判断 $\{A, B\}$ 是否能稳定或能控，判断系数矩阵的秩条件是否成立。

第2步：对于满足可静态解耦条件的系统，按极点配置算法，确定一个状态反馈增益矩阵 $K$ ，使 $(A - BK)$ 的特征值均具有负实部。

第3步：按照静态解耦后各单输入-单输出自治系统的稳态增益要求，确定 $\tilde{d}_{ii}(i=1,2,\cdots,p)$ 的值，且取 $\widetilde{D}=\mathrm{diag}\left(\tilde{d}_{11},\cdots,\tilde{d}_{pp}\right)$ 。

第4步：取输入变换阵 $L = -[C(A - BK)^{-1}B]^{-1}\widetilde{D}$ ，则 $G_{KF}(0) = \widetilde{D}$ 。
