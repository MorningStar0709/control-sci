从式 (7.2.46) 和式 (7.2.47) 可知，对于任意正整数 $l$ ，有

$$
\left\{ \begin{array}{l l} \frac {\mathrm{d} ^ {l} \beta (t)}{\mathrm{d} t ^ {l}} = \frac {\mathrm{d} ^ {l}}{\mathrm{d} t ^ {l}} \sum_ {i = 1} ^ {n} \psi_ {i} (t) b _ {i} (x (t)) = 0, \\ \frac {\mathrm{d} ^ {l} \alpha (t)}{\mathrm{d} t ^ {l}} = \frac {\mathrm{d} ^ {l}}{\mathrm{d} t ^ {l}} \sum_ {i = 1} ^ {n} \psi_ {i} (t) f _ {i} (x (t)) = 0, \end{array} \right. \quad \forall t \in [ t _ {1}, t _ {2} ]. \tag {7.2.48}
$$

取 $l = 1$ ，则由 $\frac{\mathrm{d}\beta(t)}{\mathrm{d}t} = 0$ 整理后并联立式(7.2.46)和式(7.2.47)，得到

$$
\left\{ \begin{array}{l l} \sum_ {i = 1} ^ {n} \psi_ {i} (t) f _ {i} (x (t)) = 1, \\ \sum_ {i = 1} ^ {n} \psi_ {i} (t) b _ {i} (x (t)) = 0, & \forall t \in [ t _ {1}, t _ {2} ], \\ \sum_ {i = 1} ^ {n} \psi_ {i} (t) \Phi_ {1 i} (x (t)) = 0, \end{array} \right. \tag {7.2.49}
$$

其中 $\Phi_{1i}(x(t)) \stackrel{\mathrm{def}}{=} -\sum_{k=1}^{n}\left(b_k(x(t))\frac{\partial f_i(x(t))}{\partial x_k} - f_k(x(t))\frac{\partial b_i(x(t))}{\partial x_k}\right)$ .

对方程 (7.2.49) 中第三式求导，经整理后不难得到

$$\frac {\mathrm{d}}{\mathrm{d} t} \left[ \sum_ {i = 1} ^ {n} \psi_ {i} (t) \Phi_ {1 i} (x (t)) \right] = \sum_ {i = 1} ^ {n} \psi_ {i} (t) \Phi_ {2 i} (x (t)) + u (t) \sum_ {i = 1} ^ {n} \psi_ {i} (t) \Psi_ {2 i} (x (t)) = 0, \tag {7.2.50}$$

其中
