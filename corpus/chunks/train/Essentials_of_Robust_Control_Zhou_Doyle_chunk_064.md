where $U _ { r } = [ u _ { 1 } , \ldots , u _ { r } ] , V _ { r } = [ v _ { 1 } , \ldots , v _ { r } ]$ , and $\Sigma _ { r } = \operatorname { d i a g } \left( \sigma _ { 1 } , \ldots , \sigma _ { r } \right)$ ;

5. $\| A \| _ { F } ^ { 2 } = \sigma _ { 1 } ^ { 2 } + \sigma _ { 2 } ^ { 2 } + \cdot \cdot \cdot + \sigma _ { r } ^ { 2 } ,$

6. $\| A \| = \sigma _ { 1 }$ ;

7. $\sigma _ { i } ( U _ { 0 } A V _ { 0 } ) = \sigma _ { i } ( A ) , i = 1 , \ldots , p$ for any appropriately dimensioned unitary matrices U0 and $V _ { 0 } ;$

8. Let $k < r = \mathrm { r a n k } ( A )$ and $\begin{array} { r } { A _ { k } : = \sum _ { i = 1 } ^ { k } \sigma _ { i } u _ { i } v _ { i } ^ { * } } \end{array}$

$$\min _ {\operatorname{rank} (B) \leq k} \| A - B \| = \| A - A _ {k} \| = \sigma_ {k + 1}.$$

Proof. We shall only give a proof for part 8. It is easy to see that rank $\left( A _ { k } \right) \leq k$ and $\| A - A _ { k } \| = \sigma _ { k + 1 }$ . Hence, we only need show that min $\| A - B \| \geq \sigma _ { k + 1 }$ . Let B rank(B)≤k be any matrix such that rank $( B ) \leq k .$ . Then

$$
\begin{array}{l} \| A - B \| = \| U \Sigma V ^ {*} - B \| = \| \Sigma - U ^ {*} B V \| \\ \geq \left\| \left[ \begin{array}{c c} I _ {k + 1} & 0 \end{array} \right] (\Sigma - U ^ {*} B V) \left[ \begin{array}{c} I _ {k + 1} \\ 0 \end{array} \right] \right\| = \left\| \Sigma_ {k + 1} - \hat {B} \right\|, \\ \end{array}
$$

where $\begin{array} { r } { \hat { B } = \left[ \begin{array} { l l } { I _ { k + 1 } } & { 0 } \end{array} \right] U ^ { * } B V \left[ \begin{array} { c } { I _ { k + 1 } } \\ { 0 } \end{array} \right] \in \mathbb { F } ^ { ( k + 1 ) \times ( k + 1 ) } } \end{array}$ and $\operatorname { r a n k } ( { \hat { B } } ) \leq k$ . Let $x \in \mathbb { F } ^ { k + 1 }$ be such that $\hat { B } x = 0$ and $\| { \boldsymbol x } \| = 1$ . Then

$$\| A - B \| \geq \left\| \Sigma_ {k + 1} - \hat {B} \right\| \geq \left\| (\Sigma_ {k + 1} - \hat {B}) x \right\| = \| \Sigma_ {k + 1} x \| \geq \sigma_ {k + 1}.$$

Since B is arbitrary, the conclusion follows.

![](image/4ac07dd606e27d00b60592dfbd2a0a5e8dcac64a29b33b9301904c30fc3112e9.jpg)

Illustrative MATLAB Commands:

$$\gg [ \mathbf {U}, \boldsymbol {\Sigma}, \mathbf {V} ] = \operatorname{svd} (\mathbf {A}) \% A = U \Sigma V ^ {*}$$

Related MATLAB Commands: cond, condest
