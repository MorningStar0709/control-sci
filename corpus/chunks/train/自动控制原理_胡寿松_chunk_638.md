$$
\begin{array}{l} \boldsymbol {B} _ {n - 1} = \boldsymbol {I} \\ \boldsymbol {B} _ {n - 2} - \boldsymbol {B} _ {n - 1} \boldsymbol {A} = a _ {n - 1} \boldsymbol {I} \\ \vdots \tag {9-99} \\ \boldsymbol {B} _ {0} - \boldsymbol {B} _ {1} \boldsymbol {A} = a _ {i} \boldsymbol {I} \\ - \boldsymbol {B} _ {0} \boldsymbol {A} = a _ {0} \boldsymbol {I} \\ \end{array}
$$

将式(9-99)两端按顺序右乘 $A^{n},A^{n-1},\cdots,A,A^{0}$ 得

$$\boldsymbol {B} _ {n - 1} \boldsymbol {A} ^ {n} = \boldsymbol {A} ^ {n}\boldsymbol {B} _ {n - 2} \boldsymbol {A} ^ {n - 1} - \boldsymbol {B} _ {n - 1} \boldsymbol {A} ^ {n} = a _ {n - 1} \boldsymbol {A} ^ {n - 1}$$

(9-100)

$$\boldsymbol {B} _ {0} \boldsymbol {A} - \boldsymbol {B} _ {1} \boldsymbol {A} ^ {2} = a _ {1} \boldsymbol {A}- \boldsymbol {B} _ {0} \boldsymbol {A} = a _ {0} \boldsymbol {I}$$

将式(9-100)中各式相加,可得

$$f (\mathbf {A}) = \mathbf {A} ^ {n} + a _ {n - 1} \mathbf {A} ^ {n - 1} + \dots + a _ {1} \mathbf {A} + a _ {0} \mathbf {I} = \mathbf {0}$$

推论1 矩阵 $\mathbf{A}$ 的 $k(k\geqslant n)$ 次幂可表示为 $\mathbf{A}$ 的 $n - 1$ 阶多项式

$$\mathbf {A} ^ {k} = \sum_ {m = 0} ^ {n - 1} \alpha_ {m} \mathbf {A} ^ {m}, \quad k \geqslant n \tag {9-101}$$

证明 由于 $A^n = -a_{n-1}A^{n-1} - a_{n-2}A^{n-2} - \cdots - a_1A - a_0I$

则 $A^{n+1}=AA^{n}=-a_{n-1}A^{n}-a_{n-2}A^{n-1}-\cdots-a_{1}A^{2}-a_{0}A$

$$= - a _ {n - 1} \left(- a _ {n - 1} \mathbf {A} ^ {n - 1} - \dots - a _ {1} \mathbf {A} - a _ {0} \mathbf {I}\right) - a _ {n - 2} \mathbf {A} ^ {n - 1}- \dots - a _ {1} A ^ {2} - a _ {0} A= \left(a _ {n - 1} ^ {2} - a _ {n - 2}\right) A ^ {n - 1} + \left(a _ {n - 1} a _ {n - 2} - a _ {n - 3}\right) A ^ {n - 2} + \dots+ \left(a _ {n - 1} a _ {2} - a _ {1}\right) \mathbf {A} ^ {2} + \left(a _ {n - 1} a _ {1} - a _ {0}\right) \mathbf {A} + a _ {n - 1} a _ {0} \mathbf {I}$$

故上述推论成立。式(9-101)中的 $\alpha_{m}$ 与A阵的元素有关。此推论可用以简化矩阵幂的计算。

推论2 矩阵指数 $\mathbf{e}^{A t}$ 可表示为 $\pmb{A}$ 的 $n - 1$ 阶多项式

$$\mathrm{e} ^ {\boldsymbol {A} t} = \sum_ {m = 0} ^ {n - 1} \alpha_ {m} (t) \boldsymbol {A} ^ {m} \tag {9-102}$$

证明 由于
