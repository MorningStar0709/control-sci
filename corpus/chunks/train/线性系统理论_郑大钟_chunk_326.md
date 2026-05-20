$$Q _ {c} = \left(Q _ {o} ^ {T} Q _ {o}\right) ^ {- 1} Q _ {o} ^ {T} H (n, n) \tag {9.42}$$

于是，由此又可导出

$$\min \left\{\text { rank } \left(Q _ {o} ^ {T} Q _ {o}\right), \text { rank } Q _ {o}, \text { rank } H (n, n) \right\}= \operatorname{rank} H (n, n) \geqslant \operatorname{rank} Q _ {c} = n \tag {9.43}$$

从而，由(9.41)和(9.43)同时成立，即得

$$\operatorname{rank} H (n, n) = n \tag {9.44}$$

进而，根据凯莱-哈密尔顿（Cayley-Hamilton）定理，又可导出

$$\operatorname{rank} H (n + k, n + k) = \operatorname{rank} H (n, n) \tag {9.45}$$

其中 $k=1,2,\cdots$ 。于是，就证明了(9.35)。结论得证。

结论2 给定 $q \times p$ 的传递函数矩阵 $G(s)$ ，其史密斯-麦克米伦形 $M(s)$ 为

$$
M (s) = U (s) G (s) V (s) = \left[ \begin{array}{c c c} \frac {\varepsilon_ {1} (s)}{\psi_ {1} (s)} & & \\ & \ddots & 0 \\ & & \frac {\varepsilon_ {r} (s)}{\psi_ {r} (s)} \\ - & 0 & 0 \end{array} \right] \tag {9.46}
$$

其中 $U(s)$ 和 $V(s)$ 为单模阵。则 $G(s)$ 的任一状态空间实现的最小维数为

$$n _ {\min} = \sum_ {i = 1} ^ {r} \deg \psi_ {i} (s) \tag {9.47}$$

其中 $r = \operatorname{rank} G(s)$ 。

证 表 $M(s) = E(s)\Psi^{*1}(s)$ ，其中

$$
E (s) = \left[ \begin{array}{c c c} \varepsilon_ {1} (s) & & 0 \\ & \varepsilon_ {r} (s) & \\ - & 0 & 0 \end{array} \right], \Psi (s) = \left[ \begin{array}{c c c} \psi_ {1} (s) & & 0 \\ & \psi_ {r} (s) & \\ - & 0 & I \end{array} \right] \tag {9.48}
$$

则在不可简约的矩阵分式描述的讨论中已证得，当取 $N_{o}(s) = U^{-1}(s)E(s), D_{o}(s) = V(s)\Psi(s)$ 时， $N_{o}(s)D_{o}^{-1}(s)$ 为给定 $G(s)$ 的一个不可简约MFD。进而，由后面关于不可简约矩阵分式描述的最小实现的讨论中又可证得，其最小实现的维数

$$n _ {\min} = \deg \det D _ {o} (s) \tag {9.49}$$

于是考虑到

$$\det D _ {o} (s) = \beta \det \Psi (s) = \beta \prod_ {i = 1} ^ {r} \psi_ {i} (s) \tag {9.50}$$

其中 $\beta = \det V(s)$ 为常数，就即可得到

$$\deg \det D _ {o} (s) = \sum_ {i = 1} ^ {r} \deg \psi_ {i} (s) \tag {9.51}$$

从而，由(9.49)和(9.51)即可导出(9.47)。这样，就完成了证明。
