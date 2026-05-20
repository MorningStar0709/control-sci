其中，由于 $\operatorname{det}(sI - A_i)$ ， $i = 1, 2$ ，均为首1多项式，因此必有 $\beta_0\beta_2 / \beta_1 = 1$ 。从而，就完成了证明。

结论 4 系统的各种结构特性, 如左互质性和右互质性、能控性和能观测性等, 在严格系统等价变换下是不变的。

证 ① 先证互质性在严格系统等价变换下不变。设 $S_{2}(s)$ 严格等价于 $S_{1}(s)$ ，则两者满足式(10.107)，于是由此可以导出

$$
\begin{array}{l} \left[ P _ {2} (s) Q _ {2} (s) \right] = [ U (s) 0 ] \left[ \begin{array}{c c} P _ {1} (s) & Q _ {1} (s) \\ - R _ {1} (s) & W _ {1} (s) \end{array} \right] \left[ \begin{array}{c c} V (s) & Y (s) \\ 0 & I _ {p} \end{array} \right] \\ = U (s) \left[ P _ {1} (s) Q _ {1} (s) \right] \left[ \begin{array}{c c} V (s) & Y (s) \\ 0 & I _ {p} \end{array} \right] \tag {10.127} \\ \end{array}
$$

和

$$
\begin{array}{l} \left[ \begin{array}{l} P _ {2} (s) \\ - R _ {2} (s) \end{array} \right] = \left[ \begin{array}{l l} U (s) & 0 \\ X (s) & I _ {q} \end{array} \right] \left[ \begin{array}{c c} P _ {1} (s) & Q _ {1} (s) \\ - R _ {1} (s) & W _ {1} (s) \end{array} \right] \left[ \begin{array}{l} V (s) \\ 0 \end{array} \right] \\ = \left[ \begin{array}{l l} U (s) & 0 \\ X (s) & I _ {q} \end{array} \right] \left[ \begin{array}{l} P _ {1} (s) \\ - R _ {1} (s) \end{array} \right] V (s) \tag {10.128} \\ \end{array}
$$

考虑到(10.128)和(10.127)中,矩阵

$$
U (s), V (s), \left[ \begin{array}{l l} U (s) & 0 \\ X (s) & I _ {q} \end{array} \right], \left[ \begin{array}{c c} V (s) & Y (s) \\ 0 & I _ {p} \end{array} \right] \tag {10.129}
$$

均为单模阵,所以进而可知,对所有 $s \in C$ 成立

$$\operatorname{rank} \left[ P _ {2} (s) Q _ {2} (s) \right] = \operatorname{rank} \left[ P _ {1} (s) Q _ {1} (s) \right] \tag {10.130}$$

和

$$
\operatorname{rank} \left[ \begin{array}{l} P _ {2} (s) \\ - R _ {2} (s) \end{array} \right] = \operatorname{rank} \left[ \begin{array}{l} P _ {1} (s) \\ - R _ {1} (s) \end{array} \right] \tag {10.131}
$$

也即成立

$$\left\{P _ {2} (s), Q _ {2} (s) \right\} \text {左互质} \Leftrightarrow \left\{P _ {1} (s), Q _ {1} (s) \right\} \text {左互质} \tag {10.132}\left\{P _ {2} (s), R _ {2} (s) \right\} \text {右互质} \Longleftrightarrow \left\{P _ {1} (s), R _ {1} (s) \right\} \text {右互质} \tag {10.133}$$

从而，证明了互质性在严格系统等价变换下保持不变。

② 再证明能控性和能观测性在严格系统等价变换下不变。表 $(A_{1}, B_{1}, C_{1}, E_{1}(p))$ 和 $(A_{2}, B_{2}, C_{2}, E_{2}(p))$ 为两个严格系统等价的状态空间描述，则利用上述证得的结论，即可导出
