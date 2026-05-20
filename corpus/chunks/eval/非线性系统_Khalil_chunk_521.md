为此,定义 $\eta(\omega,a,\mu)=(1-\mu)\phi(\omega,a)+\mu\tilde{\phi}(\omega,a)=\phi(\omega,a)-\mu\delta\Psi(\omega,a)$

$\mu \in [0,1]$ ，使得当 $\mu = 0$ 时， $\eta = \phi$ ；当 $\mu = 1$ 时， $\eta = \tilde{\phi}$ 。可以验证

$$\left| \Psi (a) + \frac {1}{G (j \omega)} \right| \geqslant \sigma (\omega), \forall (\omega , a) \in \partial \Gamma \tag {C.53}$$

例如,如果取边界为 $a = a_{1}$ , 则参考图 7.20, 式(C.53)的左边是连接 $-\Psi(a)$ 轨线上对应于 $a = a_{1}$ 的点和 $1/G(j\omega)$ 轨线上对应于 a 点的线段的长度, 其中 $\omega_{1} \leqslant \omega \leqslant \omega_{2}$ 。通过构造, 前一点在以后一点为圆心的误差圆外(或圆上), 因此连接这两点的线段的长度一定大于(或等于)误差圆的半径 $\sigma(\omega)$ 。利用式(C.53), 有

$$
\begin{array}{l} | \eta (\omega , a, \mu) | \geqslant | \phi (\omega , a) | - \mu | \delta \Psi (\omega , a) | \\ = \left| \Psi (a) + \frac {1}{G (j \omega)} \right| - \mu | \delta \Psi (\omega , a) | \geqslant \sigma (\omega) - \mu \sigma (\omega) \\ \end{array}
$$

式中用到边界(7.41)。这样,对于所有 $0 \leqslant \mu < 1$ , 上面最后一个不等式的右边为正, 这表明当 $\mu < 1$ 时, 在 $\partial \Gamma$ 上, $\eta(\omega, a, \mu) \neq 0$ 。假设在 $\partial \Gamma$ 上 $\eta(\omega, a, 1) \neq 0$ 并不失一般性, 因为不等式说明已找到了要求的解。这样, 根据 d 的同伦不变性, 有

$$d (\tilde {\phi}, \Gamma , 0) = d (\phi , \Gamma , 0) \neq 0$$

因此，方程(C.52)在 $\bar{\Gamma}$ 上有一个解。证毕。
