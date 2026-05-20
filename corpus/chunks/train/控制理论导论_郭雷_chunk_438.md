$$K = - B _ {2} ^ {\mathrm{T}} Y ^ {- 1} = - B _ {2} ^ {\mathrm{T}} \left(\sum_ {i = 1} ^ {m} y _ {i} Y _ {i}\right) ^ {- 1}. \tag {6.3.14}$$

实际上，上述凸可行问题是否有解还可以通过凸集上凸函数的优化问题(即凸规划问题)来判断并求解。为了说明这一点，我们来考察如下定义的标量函数：

$$f (y) = - \lambda_ {\min} \{M (y) \} = - \lambda_ {\min} \{- F (Y) \}. \tag {6.3.15}$$

显然， $f(y) < 0$ 当且仅当 $M(y) > 0$ ，即 $F(Y) < 0$ 而且，对于给定的标量 $\gamma, f(y) \leqslant \gamma$ 等价于

$$M (y) + \gamma I \geqslant 0.$$

所以根据引理6.3.1, 由上述LMI约束条件给出的如下集合 $\varepsilon$ 是凸集

$$\mathcal {E} = \{(y, \gamma) \mid f (y) \leqslant \gamma \}.$$

因此函数 $f(y)$ 是定义在凸集上的凸函数 (详细可参见文献 [2]). 这样我们有如下推论成立:

推论6.3.2 设定理6.3.1的假设成立．广义受控对象(6.3.1)所对应的 $H_{\infty}$ 设计问题有静态反馈解的充分必要条件是如下定义的凸规划问题有解：

$$\gamma_ {*} = \min _ {y \in \mathcal {M}} f (y) < 0, \tag {6.3.16}$$

若 $y = [y_{1} y_{2} \cdots t_{m}]$ 是上述凸规划问题的一个解，那么 $H_{\infty}$ 静态反馈控制器为

$$K = - B _ {2} ^ {\mathrm{T}} Y ^ {- 1} = - B _ {2} ^ {\mathrm{T}} \left(\sum_ {i = 1} ^ {m} y _ {i} Y _ {i}\right) ^ {- 1}. \tag {6.3.17}$$
