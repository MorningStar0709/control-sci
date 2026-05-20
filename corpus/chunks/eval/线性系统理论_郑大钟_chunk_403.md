结论1 给定开环系统的传递函数矩阵 $G_{\bullet}(s) = N(s)D^{-1}(s)$ ，其中 $D(s)$ 为列既约。再给定

(1) 一组期望的两两相异的闭环特征值

$$\lambda_ {1} ^ {*}, \lambda_ {2} ^ {*}, \dots , \lambda_ {n} ^ {*} \tag {11.110}$$

它们可以是实数或以共轭对形式出现的复数，且

$$n = \sum_ {i = 1} ^ {p} k _ {i}, k _ {i} = \delta_ {c i} D (s)$$

p 为 $D(s)$ 的维数。

(2) 一组满足如下的限制条件的期望特征向量 $\{f_{i}, i=1,2,\cdots,n\}$ :

① $f_{i}$ 属于 $\Psi(\lambda_{i}^{*})$ 的值域空间，即可以表为 $f_{i} = \Psi(\lambda_{i}^{*})p_{i}, p_{i}$ 为非零常数向量， $\Psi(s)$ 是 $D(s)$ 的低次矩阵。

② $\{f_{i}, i=1,2,\cdots,n\}$ 为线性无关。

③ 对应于共轭复数 $\lambda_{i}^{*}$ 和 $\lambda_{i+1}^{*}$ ，向量 $f_{i}$ 和 $f_{i+1}$ 也是共轭的。

则当取输入变换阵H和状态反馈阵K分别为

$$H = D _ {h c} \tag {11.111}K = - D _ {h c} ^ {- 1} \left[ g _ {1}, \dots , g _ {n} \right] \left[ f _ {1}, \dots , f _ {n} \right] ^ {- 1} = D _ {h c} ^ {- 1} \bar {K} \tag {11.112}$$

时,所导出的状态反馈系统的传递函数矩阵

$$G _ {H} (s, K) = N (s) D _ {K H} ^ {- 1} (s), D _ {K H} (s) = S (s) + \left(D _ {k c} ^ {- 1} D _ {l c} + K\right) \Psi (s)$$

的控制器形实现 $(A_{c}-B_{c}HK,B_{c}H,C_{c})$ 具有所期望的特征值 $\{\lambda_{i}^{*},i=1,2,\cdots,n\}$ 和特征向量 $\{f_{i}, i=1,2,\cdots,n\}$ 。其中， $S(s)$ 为 $D(s)$ 的列次阵， $D_{hc}$ 和 $D_{lc}$ 分别为 $D(s)$ 的列次系数阵和低次系数阵，且

$$\boldsymbol {g} _ {i} = D \left(\lambda_ {i} ^ {*}\right) \boldsymbol {p} _ {i}, i = 1, 2, \dots , n \tag {11.113}$$

证 由 $\bar{K} = -[g_1, \cdots, g_n] [f_1, \cdots, f_n]^{-1}$ 可导出

$$\bar {K} \left[ f _ {1}, \dots , f _ {n} \right] = - \left[ g _ {1}, \dots , g _ {n} \right] \tag {11.114}$$

由此，并考虑到(11.113)，进而有

$$\bar {K} f _ {i} = - \mathbf {g} _ {i} = - D \left(\lambda_ {i} ^ {*}\right) \mathbf {p} _ {i}, i = 1, 2, \dots , n \tag {11.115}$$

再知 $f_{i} = \Psi (\lambda_{i}^{*})p_{i}$ ，故将此代入上式，又可得到

$$\bar {K} \Psi \left(\lambda_ {i} ^ {*}\right) p _ {i} + D \left(\lambda_ {i} ^ {*}\right) p _ {i} = \left[ D \left(\lambda_ {i} ^ {*}\right) + \bar {K} \Psi \left(\lambda_ {i} ^ {*}\right) \right] p _ {i} = 0i = 1, 2, \dots , n \tag {11.116}$$

此外，可导出

$$
\begin{array}{l} D _ {K H} (s) = S (s) + \left(D _ {h c} ^ {- 1} D _ {l c} + K\right) \Psi (s) \\ = D _ {h c} ^ {- 1} \left[ D _ {h c} S (s) + D _ {l c} \Psi (s) + \bar {K} \Psi (s) \right] \\ = D _ {k c} ^ {- 1} [ D (s) + \bar {K} \Psi (s) ] \tag {11.117} \\ \end{array}
$$

这样，由(11.117)和(11.116)就可得到

$$D _ {K H} \left(\lambda_ {i} ^ {*}\right) p _ {i} = 0, i = 1, 2, \dots , n \tag {11.118}$$

但已知 $\pmb{p}_i$ 为非零常数向量，所以上式成立意味着 $D_{KH}(\lambda_i^*)$ 为奇异，也即成立

$$\det D _ {K H} \left(\lambda_ {i} ^ {*}\right) = 0, i = 1, 2, \dots , n \tag {11.119}$$
