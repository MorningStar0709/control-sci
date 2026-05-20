$$\mathcal {A} (\phi) (X _ {1}, \dots , X _ {r}) = \frac {1}{r !} \sum_ {\sigma \in S _ {r}} \operatorname{sign} (\sigma) (X _ {\sigma (1)}, \dots , X _ {\sigma (r)}),$$

这里对 $k$ 阶对称群 $S_{k}$ 求和.

命题3.10.2 设 $V$ 为 $n$ 维向量空间，则 $\Omega(V)$ 的维数是

$$\dim (\varOmega (V)) = 2 ^ {n}. \tag {3.10.4}$$

证明 注意 $\phi \in T^{k}(V)$ 由

$$\phi (e _ {i _ {1}}, \dots , e _ {i _ {k}}), \quad 1 \leqslant i _ {1} < i _ {2} < \dots < i _ {k} \leqslant n$$

唯一决定，换言之

$$\left\{\mathcal {A} \left(d ^ {i _ {1}} \otimes \dots \otimes d ^ {i _ {k}}\right) \mid 1 \leqslant i _ {1} < i _ {2} < \dots < i _ {k} \leqslant n \right\}$$

是 $\mathcal{T}^k (V)$ 的一个基. 因此 $\dim (\Omega^k (V)) = \left(\frac{k}{n}\right)$ . 于是结论显见.

反对称张量的楔积在张量分析中是很重要的.

定义3.10.5 设 $\phi \in \Omega^r(V)$ 及 $\psi \in \Omega^s(V)$ . $\phi$ 与 $\psi$ 的楔积 $\phi \wedge \psi$ 定义为

$$\phi \wedge \psi = \frac {(r + s) !}{r ! s !} (\mathcal {A}) (\phi \otimes \psi) \in \otimes^ {\nabla + f} (\mathcal {V}). \tag {3.10.5}$$

下面的性质对楔积十分重要，证明留作练习.

命题 3.10.3 (1) (双线性性)

$$\phi \wedge (\psi_ {1} + \psi_ {2}) = \phi \wedge \psi_ {1} + \phi \wedge \psi_ {2} A \#; \tag {3.10.6}$$

(2) (结合律)

$$\phi \wedge (\psi \wedge \eta) = (\phi \wedge \psi) \wedge \eta A \#; \tag {3.10.7}$$

(3) 如果 $\phi \in \Omega^r(V)$ 且 $\psi \in \Omega^s(V)$ , 那么

$$\phi \wedge \psi = (- 1) ^ {r s} \psi \wedge \phi A \#; \tag {3.10.8}$$

(4) 设 $\phi_{i} \in \Omega^{r_{i}}(V), i = 1, \cdots, k$ . 那么

$$\phi_ {1} \wedge \dots \wedge \phi_ {r} = \frac {\left(r _ {1} + \cdots + r _ {k}\right) !}{r _ {1} ! r _ {2} ! \cdots r _ {k} !} \mathcal {A} \left(\phi_ {1} \otimes \dots \otimes \phi_ {k}\right). \tag {3.10.9}$$

下面定义流形上的张量场.

定义 3.10.6 在一个 $C^{k}$ 流形 M 上的一个 $C^{k}$ 张量场 $\phi(x) \in T_{s}^{r}(M)$ 是一个规则，它对每一点 $x_{0} \in M$ 指定一个 $\phi(x_{0}) \in T_{s}^{r}(T_{x_{0}}(M))$ ，使得对任意 $C^{k}$ 向量场 $X_{1}(x), \cdots, X_{r}(x)$ 和余向量场 $\omega_{1}(x), \cdots, \omega_{s}(x)$ ，映射

$$\phi (X _ {1} (x), \dots , X _ {r} (x), \omega_ {1} (x), \dots , \omega_ {s} (x))$$

是一个 $C^k$ 函数.

类似于张量，对张量场我们也可同样定义对称，反对称等。两个张量场的张量积及楔积也是定义好的。

局部地说，在一个 n 维流形 M 的一个坐标卡 $(U, x)$ 上将 $T_{x}(M)$ 的自然基底选为 $\frac{\partial}{\partial x_{i}}, i = 1, \cdots, n,$ 而它的对偶基为 $dx_{i}, i = 1, \cdots, n.$

反对称张量场在理论上十分重要. $\Omega^k (M)$ 的一个自然基底为

$$\left\{\mathrm{d} x _ {i _ {1}} \wedge \dots \wedge \mathrm{d} x _ {i _ {k}} \mid 1 \leqslant i _ {1} < \dots < i _ {k} \leqslant n \right\}.$$

一个张量场 $\omega \in \Omega^k (M)$ 称为一个 $k$ -形式. 显然 $\dim (\Omega^n (M)) = 1$ . 一个 $n$ -形式可用来给流形定向.
