$$\operatorname{rank} \left[ D _ {1} (s), D _ {2} (s) \right] = p, \forall s \in \mathcal {C} \tag {11.13}$$

也即 $\{D_1(s), D_2(s)\}$ 为左互质。同理，也可证明，当 $G_1(s)$ 和 $G_2(s)$ 没有公共极点时， $\{D_{L1}(s), D_{L2}(s)\}$ 为右互质。于是，根据结论1可知，在满足本结论所给出的条件下， $S_p$ 必是能控和能观测的。这样，就完成了证明。

需要再次强调， $G_{1}(s)$ 和 $G_{2}(s)$ 没有公共的极点，并不是并联系统为能控和能观测的必要条件。对此，我们可解释如下：已知 $D_{1}(s)$ 和 $D_{2}(s)$ 均为 $p \times p$ 多项式矩阵，设 $G_{1}(s)$ 和 $G_{2}(s)$ 包含公共的极点，令为 $\lambda_{1}, \cdots, \lambda_{p}$ ，则必成立

$$\operatorname{rank} D _ {1} \left(\lambda_ {i}\right) = \alpha_ {i} < p, \operatorname{rank} D _ {2} \left(\lambda_ {i}\right) = \gamma_ {i} < p \tag {11.14}i = 1, \dots , \beta$$

再令

$$
\left\{ \begin{array}{l} a = \min \left\{\alpha_ {1}, \dots , \alpha_ {\beta} \right\} \\ \gamma = \min \left\{\gamma_ {1}, \dots , \gamma_ {\beta} \right\} \end{array} \right. \tag {11.15}
$$

那么只要 $\alpha + \gamma \geqslant p$ ，就仍有可能使

$$\operatorname{rank} \left[ D _ {1} \left(\lambda_ {i}\right), D _ {2} \left(\lambda_ {i}\right) \right] = p, i = 1, \dots , \beta \tag {11.16}$$

也即仍有可能使

$$\operatorname{rank} \left[ D _ {1} (s), D _ {2} (s) \right] = p, \forall s \in \mathcal {C} \tag {11.17}$$

这就表明，尽管 $G_{1}(s)$ 和 $G_{2}(s)$ 包含公共极点，但并联系统 $S_{P}$ 仍可能是能控和能观测的。然而，如果 $G_{1}(s)$ 和 $G_{2}(s)$ 包含公共极点，且同时有 $\alpha_{i} + \gamma_{i} < p$ ，则此种情况下并联系统 $S_{P}$ 必不是完全能控和不是完全能观测的。进一步，我们来考察单输入-单输出的情况。此时 $p = 1$ ， $D_{1}(s)$ 和 $D_{2}(s)$ 均为标量多项式。对于这种情况，只要 $G_{1}(s)$ 和 $G_{2}(s)$ 包含公共的极点，就一定属于前面讨论中的 $\alpha + \gamma < p$ 的情况。所以， $G_{1}(s)$ 和 $G_{2}(s)$ 没有公共同极点，同时也是并联系统 $S_{P}$ 为能控和能观测的必要条件。下面就是表征这一事实的一个结论。

结论3 如果限于考虑单输入-单输出的情况，则两个子系统的传递函数 $g_{1}(s)$ 和 $g_{2}(s)$ 不包含公共极点，是并联系统 $S_{P}$ 为能控和能观测的既充分又必要的条件。

此外，由结论1还可直接推论出如下的一个结论。

结论4 由 $S_{1}$ 和 $S_{2}$ 的并联构成的系统 $S_{P}$ 可用传递函数矩阵 $G_{1}(s) + G_{2}(s)$ 完全表征，即 $S_{P}$ 为完全能控和完全能观测的充分必要条件是，对 $G_{i}(s)$ 的不可简约的左MFD和右MFD同时成立

和

$$
\begin{array}{r l} & {\{D _ {1} (s), D _ {2} (s) \} \text {为左互质}} \\ & {\{D _ {L 1} (s), D _ {L 2} (s) \} \text {为右互质}} \end{array} \tag {11.18}
$$

串联系统的能控性和能观测性 考虑由两个子系统 $S_{1}$ 和 $S_{2}$ 串联组成的系统 $S_{T}$ , 如图11.2所示, 其中假定 $S_{1}$ 和 $S_{2}$ 分别可由其传递函数矩阵 $G_{1}(s)$ 和 $G_{2}(s)$ 完全表征。令 $G_{i}(s)$ 为 $q_{i} \times p_{i}$ 的有理分式矩阵, 则为了使 $S_{1}$ 和 $S_{2}$ 实现联接, 还必须附加满足条件 $q_{1} = p_{2}$ 。

下面，我们来指出有关串联系统的能控性和能观测性的一些结论。

![](image/29ca30e7812fcc1dd1e4532be77374e66f43e12f29b069aecafc32e13b3f10ab.jpg)  
图11.2 子系统的串联
