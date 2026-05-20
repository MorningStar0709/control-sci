$$
\begin{array}{l} \Phi_ {2 i} (x (t)) = \sum_ {j = 1} ^ {n} \sum_ {k = 1} ^ {n} \left(- b _ {j} (x (t)) \frac {\partial f _ {k} (x (t))}{\partial x _ {j}} \cdot \frac {\partial f _ {i} (x (t))}{\partial x _ {k}} + f _ {j} (x (t)) \frac {\partial f _ {i} (x (t))}{\partial x _ {k}} \cdot \frac {\partial b _ {k} (x (t))}{\partial x _ {j}} \right. \\ + f _ {k} (x (t)) \frac {\partial b _ {j} (x (t))}{\partial x _ {k}} \cdot \frac {\partial f _ {k} (x (t))}{\partial x _ {j}} + b _ {j} (x (t)) b _ {k} (x (t)) \frac {\partial^ {2} f _ {i} (x (t))}{\partial x _ {k} \partial x _ {j}} \\ \left. - b _ {k} (x (t)) \frac {\partial f _ {j} (x (t))}{\partial x _ {k}} \cdot \frac {\partial b _ {i} (x (t))}{\partial x _ {j}} - f _ {j} (x (t)) b _ {k} (x (t)) \frac {\partial^ {2} b _ {i} (x (t))}{\partial x _ {k} \partial x _ {j}}\right), \\ \Psi_ {2 i} (x (t)) = \sum_ {j = 1} ^ {n} \sum_ {k = 1} ^ {n} \left(f _ {j} (x (t)) \frac {\partial f _ {k} (x (t))}{\partial x _ {j}} \cdot \frac {\partial b _ {i} (x (t))}{\partial x _ {k}} - b _ {j} (x (t)) \frac {\partial b _ {k} (x (t))}{\partial x _ {j}} \cdot \frac {\partial b _ {i} (x (t))}{\partial x _ {k}} \right. \\ + b _ {k} (x (t)) \frac {\partial b _ {j} (x (t))}{\partial x _ {k}} \cdot \frac {\partial f _ {i} (x (t))}{\partial x _ {j}} + b _ {j} (x (t)) b _ {k} (x (t)) \frac {\partial^ {2} f _ {i} (x (t))}{\partial x _ {k} \partial x _ {j}} \\ \left. - b _ {k} (x (t)) \frac {\partial f _ {j} (x (t))}{\partial x _ {k}} \cdot \frac {\partial b _ {i} (x (t))}{\partial x _ {j}} - f _ {j} (x (t)) b _ {k} (x (t)) \frac {\partial^ {2} b _ {i} (x (t))}{\partial x _ {k} \partial x _ {j}}\right). \\ \end{array}
$$

若 $\sum_{i=1}^{n} \psi_i(t) \Psi_{2i}(x(t)) \neq 0, \forall t \in [t_1, t_2]$ , 则从式 (7.2.50) 能解得 $u(t)$ 为

$$u (t) = - \frac {\sum_ {i = 1} ^ {n} \psi_ {i} (t) \Phi_ {2 i} (x (t))}{\sum_ {i = 1} ^ {n} \psi_ {i} (t) \Psi_ {2 i} (x (t))}; \tag {7.2.51}$$

而若 $\sum_{i=1}^{n} \psi_i(t) \Psi_{2i}(x(t)) = 0, \forall t \in [t_1, t_2]$ , 则从式 (7.2.50) 能得到

$$\sum_ {i = 1} ^ {n} \psi_ {i} (t) \Phi_ {2 i} (x (t)) = 0, \quad \forall t \in [ t _ {1}, t _ {2} ].$$

对上式两端求导，整理后又能得到

$$
\begin{array}{l} \frac {\mathrm{d}}{\mathrm{d} t} \left[ \sum_ {i = 1} ^ {n} \psi_ {i} (t) \Phi_ {2 i} (x (t)) \right] \\ = \sum_ {i = 1} ^ {n} \psi_ {i} (t) \Phi_ {3 i} (x (t)) + u (t) \sum_ {i = 1} ^ {n} \psi_ {i} (t) \Psi_ {3 i} (x (t)) = 0. \tag {7.2.52} \\ \end{array}
$$

其中 $\Phi_{3i}(x(t)),\Psi_{3i}(x(t))$ 的表示式这里不再赘述.

若 $\sum_{i=1}^{n} \psi_i(t) \Psi_{3i}(x(t)) \neq 0, \forall t \in [t_1, t_2]$ , 则从式 (7.2.52) 又可解得 $u(t)$ 为
