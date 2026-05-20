从而 $\mathcal{N}(G(t_f)^*) = \{0\} \Longleftrightarrow W(t_f) > 0$ ，这证明了 (1). 另一方面，对于自伴算子 $W(t_f), \mathcal{R}(W(t_f)) = H \Longleftrightarrow W(t_f)$ 是正定的，由此 (2) 成立. 证毕.

现在我们通过秩条件来给出能控性的另一个判据.

定理10.2.6 设 $X$ 和 $U$ 是两个自反Banach空间，并令

$$U _ {\infty} = \left\{u \in U \mid B u \in \bigcap_ {n \geqslant 1} \mathcal {D} (A ^ {n}) \right\}.$$

如果

$$\overline {{{{\operatorname{span}}}}} \left\{A ^ {n} B U _ {\infty} \mid n \geqslant 0 \right\} = X, \tag {10.2.12}$$

则 $(A, B)$ 在任意有穷时间区间 $[0, t_f]$ 上近似能控.

证明留作练习.

下面我们列举一些有关能控性和能观测性的例子.

例10.2.1 设 $A$ 是Hilbert空间 $H$ 上具有紧豫解式的正定自伴算子. 设 $\sigma(A) = \{\lambda_n \mid n \geqslant 1\}$ , 假定每个 $\lambda_n$ 是单的, 从而 $A$ 的相应的规范本征元列 $\{\varphi_n \mid n \geqslant 1\}$ 构成 $H$ 的规范正交基. 现在我们考虑如下二阶发展方程:

$$\frac {\mathrm{d} ^ {2} y}{\mathrm{d} t ^ {2}} + A y = u (t). \tag {10.2.13}$$

定义乘积 Hilbert 空间 $\mathcal{H} = D\left(A^{\frac{1}{2}}\right) \times H$ ，其中内积定义为

$$\left(\left[ y _ {1}, z _ {1} \right] ^ {\mathrm{T}}, \left[ y _ {2}, z _ {2} \right] ^ {\mathrm{T}}\right) _ {\mathcal {H}} = (A ^ {\frac {1}{2}} y _ {1}, A ^ {\frac {1}{2}} y _ {2}) _ {H} + (z _ {1}, z _ {2}) _ {H},$$

并且在 $\mathcal{H}$ 中定义线性算子

$$
\mathcal {A} \left[ \begin{array}{l} \varphi \\ \psi \end{array} \right] = \left[ \begin{array}{c c} 0 & I \\ - A & 0 \end{array} \right] \left[ \begin{array}{l} \varphi \\ \psi \end{array} \right], \quad \forall \left[ \begin{array}{l} \varphi \\ \psi \end{array} \right] \in \mathcal {D} (\mathcal {A}) = \mathcal {D} (A) \times D \left(A ^ {\frac {1}{2}}\right).
$$

于是式 (10.2.13) 可以写成如下的等价形式:

$$\frac {\mathrm{d} w}{\mathrm{d} t} = \mathcal {A} w + \mathcal {B} u (t),$$

其中 $\mathcal{B} = [0,I]^{\mathrm{T}}$ 从例5.3.11，由 $\mathcal{A}$ 生成的 $C_0$ 半群是

$$
T (t) w = \left[ \begin{array}{l} \sum_ {n = 1} ^ {\infty} \left[ (y, \varphi_ {n}) _ {H} \cos \sqrt {\lambda_ {n}} t + \frac {1}{\sqrt {\lambda_ {n}}} (z, \varphi_ {n}) _ {H} \sin \sqrt {\lambda_ {n}} t \right] \varphi_ {n} \\ \sum_ {n = 1} ^ {\infty} \left[ - \sqrt {\lambda_ {n}} (y, \varphi_ {n}) _ {H} \sin \sqrt {\lambda_ {n}} t + (z, \varphi_ {n}) _ {H} \cos \sqrt {\lambda_ {n}} t \right] \varphi_ {n} \end{array} \right],
$$

其中 $w = [y, z]^{\mathrm{T}} \in \mathcal{H}$ . 由于 $\mathcal{A}^{*} = -\mathcal{A}$ , 故 $T(t)$ 可以延拓成一酉群, 并且 $T^{*}(t) = T(-t)$ . 注意到 $\mathcal{B}^{*} - [0, I]$ , 我们有
