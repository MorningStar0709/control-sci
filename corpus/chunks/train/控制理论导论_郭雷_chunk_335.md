$$
\begin{array}{l} \int_ {C} E \left(I _ {[ x \in A ]} | z\right) E \left(I _ {[ y \in B ]} | z\right) \mathrm{d} P = \int_ {C} E \left\{I _ {[ y \in B ]} E \left(I _ {[ x \in A ]} | z\right) | z \right\} \mathrm{d} P \\ = \int_ {C \cap [ y \in B ]} E (I _ {[ x \in A ]} | ^ {z}) \mathrm{d} P. \\ \end{array}
$$

由于 $E(I_{[x \in A]}|z)$ 对 $(z, y)$ 可测，据条件期望的唯一性知 $E(I_{[x \in A]}|zy) = E(I_{[x \in A]}|z)$ . 对 $x$ 用形如 $I_{[x \in A]}$ 的示性函数的线性组合逼近，取极限后知 $E(x|z, y) = E(x|z)$ .

正态随机向量的特征函数已由式 (4.1.13) 给出，设 $x, y$ 为两个实随机向量， $E \| x\|^2 < \infty$ 。记

$$R _ {x} ^ {y} \stackrel {\text { def }} {=} E [ (x - E (x | y)) (x - E (x | y)) ^ {\mathrm{T}} | y ].$$

如果给定 $y$ ，条件特征函数为

$$E (\mathrm{e} ^ {\mathrm{i} \lambda^ {\mathrm{T}} x} | y) = \mathrm{e} ^ {\mathrm{i} \lambda^ {\mathrm{T}} E (x | y) - \frac {1}{2} \lambda^ {\mathrm{T}} R _ {x} ^ {y} \lambda}, \tag {4.4.23}$$

那么称 $x$ 为在 $y$ 条件下的正态向量，也就是说，当 $y$ 等于某确定性向量 $\eta$ 时，在 $y$ 条件下， $x$ 的条件分布为正态，期望为 $E(x|y)|_{y=\eta}$ ，协方差阵为 $R_x^y|_{y=\eta}$ .

设 $x, y, z$ 为三个随机向量，用 $f_x(\lambda), f_y(\mu)$ 和 $f_w(\gamma)$ 分别表示 $x, y$ 和 $w \stackrel{\mathrm{def}}{=} \begin{bmatrix} x \\ y \end{bmatrix}$ 的特征函数。据定理4.2.1， $x$ 和 $y$ 独立的充分必要条件是 $f_w(\gamma) = f_x(\lambda)f_y(\mu)$ 。今用 $f_{x}^{z}(\lambda), f_{y}^{2}(\mu)$ 和 $f_{w}^{z}(\gamma)$ 表示在 $z$ 条件下， $x, y$ 和 $w$ 的条件特征函数。和无条件情形类似地证明，在 $z$ 条件， $x$ 和 $y$ 独立等价于

$$f _ {x} ^ {z} (\gamma) = f _ {z} ^ {z} (\lambda) f _ {y} ^ {z} (\mu). \tag {4.4.24}$$

引理 4.4.4 i) 设 $w = \begin{bmatrix} x \\ y \end{bmatrix}$ 为正态，那么 x 和 y 独立等价于 x 和 y 不相关。设在 z 条件下，w 为条件正态，那么在 z 条件 x 和 y 条件独立等价于

$$R _ {x y} ^ {z} \stackrel {\text { def }} {=} E [ (x - E (x | z)) (y - E (y | z)) ^ {\mathrm{T}} | z ] = 0;$$

ii) 设 $w$ 正态, $A$ 和 $b$ 为相应维数的阵和向量, 那么 $Aw + b$ 仍为正态. 设在 $z$ 条件下, $w$ 为条件正态, 而 $A(z)$ 和 $b(z)$ 均为对 $z$ 可测, 那么在 $z$ 条件下, $A(z)w + b(z)$ 仍为条件正态.

证明 i) 设 $x$ 和 $y$ 独立，那么

$$R _ {x y} \stackrel {\text { def }} {=} E [ (x - E x) (y - E y) ^ {\mathrm{T}} = E (x - E x) E (y - E y) ^ {\mathrm{T}} = 0.$$

设 $x$ 和 $y$ 不相关，那么

$$
R _ {w} = \left[ \begin{array}{c c} R _ {x} & 0 \\ 0 & R _ {y} \end{array} \right].
$$

设

$$\gamma = [ \lambda^ {\mathrm{T}} \quad \mu^ {\mathrm{T}} ] ^ {\mathrm{T}}.$$

计算 $w$ 的特征函数
