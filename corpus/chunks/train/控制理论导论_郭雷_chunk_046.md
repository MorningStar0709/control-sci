$$\boldsymbol {z} ^ {\mathrm{T}} \boldsymbol {A} ^ {k} + \alpha_ {k - 1} \boldsymbol {z} ^ {\mathrm{T}} \boldsymbol {A} ^ {k - 1} + \dots + \alpha_ {1} \boldsymbol {z} ^ {\mathrm{T}} \boldsymbol {A} + \alpha_ {0} \boldsymbol {z} ^ {\mathrm{T}} = 0.$$

这说明

$$f (s) = s ^ {k} + \alpha_ {k - 1} s ^ {k - 1} + \dots + \alpha_ {1} s + \alpha_ {0}$$

是 $z^{\mathrm{T}}$ 相对 $\pmb{A}$ 的最小多项式. 令 $s_0$ 是 $f(s)$ 的一个零点, 显然 $s_0$ 是 $\pmb{A}$ 的一个特征值, 这是因为 $f(s)$ 是 $\pmb{A}$ 的特征多项式的一个因子. 于是重新写 $f(s)$ 为

$$f (s) = \left(s ^ {k - 1} + \beta_ {k - 2} s ^ {k - 2} + \dots + \beta_ {1} s + \beta_ {0}\right) \left(s - s _ {0}\right),$$

这里 $\beta_{0},\beta_{1},\cdots,\beta_{k-2}$ 是 k-1 个复常数。于是有

$$\boldsymbol {z} ^ {\mathrm{T}} f (A) = \boldsymbol {z} ^ {\mathrm{T}} (\boldsymbol {A} ^ {k - 1} + \beta_ {k - 2} \boldsymbol {A} ^ {k - 2} + \dots + \beta_ {1} \boldsymbol {A} + \beta_ {0} \boldsymbol {I} _ {n}) (\boldsymbol {A} - \lambda_ {0} \boldsymbol {I} _ {n}) = 0.$$

令

$$\boldsymbol {\psi} ^ {\mathrm{T}} = \boldsymbol {z} ^ {\mathrm{T}} (\boldsymbol {A} ^ {k - 1} + \beta_ {k - 2} \boldsymbol {A} ^ {k - 2} + \dots + \beta_ {1} \boldsymbol {A} + \beta_ {0} \boldsymbol {I} _ {n}). \tag {1.3.11}$$

显然 $\psi^{\mathrm{T}}\neq 0$ ，这是因为 $z^{\mathrm{T}}$ 相对 $\pmb{A}$ 的最小多项式为 $k$ 次的．这样， $\psi^{\mathrm{T}}$ 是 $\pmb{A}$ 的相应于特征值 $s_0$ 的特征向量．但是，从式(1.3.10)和式(1.3.11)得出， $\psi^{\mathrm{T}}B = 0,$ 所以必有

$$\operatorname{rank} [ \boldsymbol {A} - \lambda_ {0} \boldsymbol {I} _ {n}, \quad \boldsymbol {B} ] < n.$$

而这与假设 (1.3.8) 矛盾，这个矛盾表明系统 $(A, B)$ 是能控的。

推论 1.3.3 定常线性系统 (A, B) 能控的充要条件是它没有输入解耦零点.

从定理1.3.3还可以发现，定常线性系统 $(A,B)$ 能控的充要条件是

$$s \in \sigma (A), z \in \mathbb {R} ^ {n}, z ^ {\mathrm{T}} B = 0, \text {且} z ^ {\mathrm{T}} (A - s I _ {n}) = 0 \Longrightarrow z = 0.$$

即系统 $(A, B)$ 能控的充要条件是，对 $A^{\mathrm{T}}$ 的每个特征向量 $z$ ，总有 $z^{\mathrm{T}}B \neq 0$ .

按照系统的能控性，可以对定常线性系统的系统矩阵 $\pmb{A}$ 的特征值（或系统的极点）进行分类。当 $s_0 \in \sigma(A)$ ，并且满足

$$\operatorname{rank} [ \boldsymbol {A} - s _ {0} \boldsymbol {I} _ {n}, \boldsymbol {B} ] < n$$

时，系统 $(A, B)$ 不能控，这样的 $s_0$ 叫做系统 $(A, B)$ 的一个不能控振型。系统的不能控振型是它的极点，又是它的输入解耦零点。

关于定常系统的能控性，除了上述的代数判据以外，还有几何判据。有兴趣的读者可以参考文献 [15].

下面讨论线性系统理论中的另一重要概念，即能观测性.
