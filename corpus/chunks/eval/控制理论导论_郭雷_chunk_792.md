$$
\begin{array}{l} \left\langle Y _ {1}, Y _ {2} \right\rangle = \int_ {0} ^ {\ell} K \left(\varphi_ {1} - w _ {1} ^ {\prime}\right) \left(\bar {\varphi} _ {2} - \bar {w} _ {2} ^ {\prime}\right) d x + \int_ {0} ^ {\ell} E I \varphi_ {1} ^ {\prime} \bar {\varphi} _ {2} ^ {\prime} d x \\ + \int_ {0} ^ {\ell} \rho z _ {1} \overline {{z}} _ {2} \mathrm{d} x + \int_ {0} ^ {\ell} I _ {\rho} \psi_ {1} \overline {{\psi}} _ {2} \mathrm{d} x. \\ \end{array}
$$

在 $\mathcal{H}$ 中定义线性算子 $A = A_{1} + B$

$$
\mathcal {A} _ {1} \left[ \begin{array}{c} w \\ z \\ \varphi \\ \psi \end{array} \right] = \left[ \begin{array}{c} z \\ - \rho^ {- 1} (K (\varphi - w ^ {\prime})) ^ {\prime} \\ \psi \\ I _ {\rho} ^ {- 1} (E I \varphi^ {\prime}) ^ {\prime} - I _ {\rho} ^ {- 1} K (\varphi - w ^ {\prime}) \end{array} \right], \quad \forall \left[ \begin{array}{c} w \\ z \\ \varphi \\ \psi \end{array} \right] \in \mathcal {D} (\mathcal {A}),
\mathcal {D} (\mathcal {A} _ {1}) = \left\{\left[ w, z, \varphi , \psi \right] ^ {\mathrm{T}} \mid w, \varphi \in V _ {0} ^ {2}, z, \psi \in V _ {0} ^ {1}, \varphi (\ell) = w ^ {\prime} (\ell), \varphi^ {\prime} (\ell) = 0 \right\},\boldsymbol {B} [ \boldsymbol {w}, z, \varphi , \psi ] ^ {\mathrm{T}} = [ 0, - b _ {1} z, 0, b _ {2} \psi ] ^ {\mathrm{T}}, \quad \forall [ \boldsymbol {w}, z, \varphi , \psi ] ^ {\mathrm{T}} \in \mathcal {H}.
$$

于是方程 (10.4.27) 可以写成 $\mathcal{H}$ 中线性发展方程

$$\dot {Y} (t) = \mathcal {A} Y (t).$$

可以证明 (留作练习), $\mathcal{A}_{1}^{*} = -\mathcal{A}_{1}$ , $\mathcal{A}_{1}$ 有紧豫解式, $\mathcal{B} \in \mathcal{L}(\mathcal{H})$ , $\mathcal{A}$ 生成 $\mathcal{H}$ 中 $C_{0}$ 压缩半群, 从而方程 (10.4.27) 是适定的. 系统 (10.4.27) 的能量是

$$E (t) = \frac {1}{2} \int_ {0} ^ {\ell} \left(K | \varphi - w ^ {\prime} | ^ {2} + E I | \varphi^ {\prime} | ^ {2} + \rho | z | ^ {2} + I _ {\rho} | \psi | ^ {2}\right) d x.$$

下面我们证明 $\mathbb{R} \subset \rho(\mathcal{A})$ , 并且 (10.4.25) 成立, 从而系统 (10.4.27) 指数稳定.

事实上，如果 $\mathbf{i}\mathbb{R} \subset \rho(\mathcal{A})$ 不成立，则存在 $\omega \in \mathbb{R}$ 使得 $\mathrm{i}\omega \in \sigma_p(\mathcal{A})$ ，从而存在非零元 $[\varphi, \psi]^{\mathrm{T}} \in \mathcal{D}(\mathcal{A})$ ，使得 $\mathcal{A}[\varphi, \psi]^{\mathrm{T}} = \mathrm{i}\omega[\varphi, \psi]^{\mathrm{T}}$ 。于是

$$\operatorname{Re} \langle \mathcal {A} Y, Y \rangle = - \int_ {0} ^ {\ell} (\rho b _ {1} | z | ^ {2} + I _ {\rho} b _ {2} | \psi | ^ {2}) \mathrm{d} x = 0.$$

由此从假设 (10.4.28) 可得

$$b _ {1} (x) z (x) = 0, \quad b _ {1} (x) \psi (x) = 0, \quad \forall x \in [ 0, \ell ].$$
