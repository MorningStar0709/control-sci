考虑到 $b_{k}(x) > 0, \forall x \in [c,d]$ , 有 $z(x) = w(x) = \psi(x) = \varphi(x) = 0, \forall x \in [c,d]$ . 由于 $\psi = \mathrm{i}\omega \varphi$ , 故 $\varphi$ 和 $w$ 满足

$$
\left\{ \begin{array}{l} (K (\varphi - w ^ {\prime})) ^ {\prime} - \omega^ {2} \rho w = 0, \\ (E I \varphi^ {\prime}) ^ {\prime} - K (\varphi - w ^ {\prime}) + \omega^ {2} I _ {\rho} \varphi = 0, \\ w (x) = \varphi (x) = 0, \quad \forall x \in [ c, d ], \\ \varphi (0) = 0, \quad \varphi^ {\prime} (0) = 0, \quad \varphi^ {\prime} (\ell) = w ^ {\prime} (\ell), \quad \varphi^ {\prime} (\ell) = 0. \end{array} \right.
$$

于是根据常微分方程理论， $\varphi (x) = w(x) = 0,\forall x\in [0,\ell ]$ ，这与 $[\varphi ,\psi ]\neq 0$ 相矛盾.

现在假定存在 $Y_{n} = [w_{n},z_{n},\varphi_{n},\psi_{n}]\in \mathcal{D}(\mathcal{A})$ 和 $\{\omega_n\} \subset \mathbb{R}$ ，使得式(10.4.26）成立．记 $\tilde{Y}_n = [\tilde{w}_n,\tilde{z}_n,\tilde{\varphi}_n,\tilde{\psi}_n]^{\mathrm{T}} = \mathrm{i}\omega_nY_n - AY_n$ ，即

$$
\left\{ \begin{array}{l} \tilde {w} _ {n} = \mathrm{i} \omega_ {n} w _ {n} - z _ {n}, \\ \tilde {z} _ {n} = \mathrm{i} \omega_ {n} z _ {n} + \rho^ {- 1} (K (\varphi_ {n} - w _ {n} ^ {\prime})) ^ {\prime} + b _ {1} z _ {n}, \\ \tilde {\varphi} _ {n} = \mathrm{i} \omega_ {n} \varphi_ {n} - \psi_ {n}, \\ \tilde {\psi} _ {n} = \mathrm{i} \omega_ {n} \psi_ {n} - I _ {\rho} ^ {- 1} (E I \varphi_ {n} ^ {\prime}) ^ {\prime} + I _ {\rho} ^ {- 1} K (\varphi_ {n} - w _ {n} ^ {\prime}) + b _ {2} \psi_ {n}. \end{array} \right. \tag {10.4.29}
$$

从 $\lim_{n\to \infty}\operatorname {Re}\langle \tilde{Y}_n,Y_n\rangle = 0$ 可知

$$\lim _ {n \rightarrow \infty} \int_ {0} ^ {\ell} (\rho b _ {1} | z _ {n} | ^ {2} + I _ {\rho} b _ {2} | \psi_ {n} | ^ {2}) \mathrm{d} x = 0. \tag {10.4.30}$$

从方程 (10.4.29) 可知存在常数 $C > 0$ 使得

$$\left\| \omega_ {n} w _ {n} \right\| _ {L ^ {2}} \leqslant C, \quad \left\| \omega_ {n} \varphi_ {n} \right\| _ {L ^ {2}} \leqslant C, \quad \forall n \geqslant 1,$$

这里及下面 $C$ 均表示正常数而不特别说明 (每次出现时可能取不同值). 于是

$$\lim _ {n \rightarrow \infty} \| w _ {n} \| _ {L ^ {2}} = 0, \quad \lim _ {n \rightarrow \infty} \| \varphi_ {n} \| _ {L ^ {2}} = 0. \tag {10.4.31}$$

注意 $w_{n}$ 和 $\varphi_{n}$ 满足方程
