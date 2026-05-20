14.11 假设用 $v_{i} = -\beta (x)\sigma \left(\frac{s_{i}}{\varepsilon}\right)$

代换式(14.13)，其中 $\sigma: R \rightarrow R$ 是连续可微且单调递增的奇函数，具有性质

$$\sigma (0) = 0, \quad \lim _ {y \rightarrow \infty} \sigma (y) = 1, \quad y \sigma (y) \geqslant \sigma (1) y ^ {2}, \forall | y | \leqslant 1$$

(a) 验证当 $\sigma(y)=\tanh(y)$ , $\sigma(y)=(2/\pi)\arctan(\pi y/2)$ 和 $\sigma(y)=y/(1+|y|)$ 时, 满足上述性质。  
(b) 证明如果式(14.10)在 $\kappa_{0}<\sigma(1)$ 时成立,且选择 $\beta$ 满足

$$\beta (x) \geqslant \frac {\varrho (x)}{\sigma (1) - \kappa_ {0}} + \beta_ {0}, \quad \beta_ {0} > 0$$

则 $s_i\dot{s}_i\leqslant -g_0\beta_0[\sigma (1) - \kappa_0 ]|s_i|,\quad |s_i|\geqslant \varepsilon$

(c) 对于该滑模控制,验证定理 14.1 和定理 14.2。

14.12 将不等式(14.10)代换为

$$\frac {\Delta_ {i}}{g _ {i}} \leqslant \varrho_ {i} (x) + \sum_ {j = 1} ^ {p} \kappa_ {i j} | v _ {j} |, \quad \forall 1 \leqslant i \leqslant p$$

设K是 $p \times p$ 矩阵,其元素为 $\kappa_{ij}$ ,并假设I-K是M矩阵①。由M矩阵的性质可知下面三个条件是等价的②:

(i) I - K 是 M 矩阵。  
(ii) I - K是非奇异的,且 $(I - K)^{-1}$ 的所有元素都是非负的。  
(iii) 存在一个各元素均为正的向量 w，使 $b = (I - \mathcal{K})w$ 的元素均为正。

设 $\overline{\varrho}_{i}(x)\geqslant\varrho_{i}(x)(1\leqslant i\leqslant p)$ 及 $\sigma(x)=(I-\mathcal{K})^{-1}\left[\overline{\varrho}_{1}(x),\cdots,\overline{\varrho}_{p}(x)\right]^{\mathrm{T}}$ 。

(a) 证明当 $1 \leqslant i \leqslant p$ 时，由 $v_{i} = -\beta_{i}(x)\operatorname{sgn}(s_{i}), \beta_{i}(x) = \sigma_{i}(x) + w_{i}$ ，可得出 $s_{i}\dot{s}_{i} \leqslant -b_{i}g_{0}|s_{i}|$ 。  
(b) 设 $\sum_{j=1}^{p}\kappa_{ij}\leqslant\kappa_{0}<1$ 和 $\varrho_{i}(x)=\varrho(x),1\leqslant i\leqslant p$ 。证明 I-K 是 M 矩阵，且适当选取 $\overline{\varrho}_{i}(x)$ 和 w 可得到控制 (14.11)。

14.13 参照 14.1.3 节中的连续型滑模控制器,证明存在一个有限时间 T, 可能与 $\varepsilon$ 和初始状态有关, 以及一个正常数 k, 与 $\varepsilon$ 和初始状态无关, 使得对于所有 $t \geqslant T$ , 有 $|y(t) - r(t)| \leqslant k\varepsilon$ 。  
14.14 应用李雅普诺夫再设计,重做习题 14.5。  
14.15 应用李雅普诺夫再设计,重做习题 14.8。  
14.16 利用 14.1.1 节给出的单摆方程的数据, 对例 14.5 的李雅普诺夫再设计进行仿真, 选择李雅普诺夫再设计的参数, 得到与滑模控制设计中相同的控制水平。比较这两种控制器的性能。  
14.17 对下列各标量系统,运用非线性阻尼工具设计一个状态反馈控制器,保证状态 $x(t)$ 有界性以及一致毕竟有界性,其最终边界为 $\mu$ 。对于所有 $t \geqslant 0$ , 函数 $\delta(t)$ 是有界的,但 $|\delta(t)|$ 的上界未知。

(a) $\dot{x} = -x + x^{2}[u + \delta(t)],$

(b) $\dot{x}=x^{2}[1+\delta(t)]-xu$

14.18 考虑以标称形式(13.16)\~(13.18)表示的单输入-单输出系统,并假设式(13.16)是输入-状态稳定的。设 $\hat{\alpha}(x)$ 和 $\hat{\gamma}(x)$ 分别是函数 $\alpha(x)$ 和 $\gamma(x)$ 的标称模型,并假设建模误差满足不等式
