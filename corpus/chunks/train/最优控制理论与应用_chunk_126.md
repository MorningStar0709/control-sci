$$\left(\boldsymbol {g} ^ {K}, \boldsymbol {g} ^ {K - 1}\right) = 0 \quad K = 1, 2, \dots \tag {7-44}$$

证明 由性质3和式(7-26)知

$$
\begin{array}{l} 0 = \left(\boldsymbol {g} ^ {K}, \boldsymbol {P} ^ {K - 1}\right) = \left(\boldsymbol {g} ^ {K}, - \boldsymbol {g} ^ {K - 1} + \beta^ {K - 1} \boldsymbol {P} ^ {K - 2}\right) \\ = - \left(\boldsymbol {g} ^ {K}, \boldsymbol {g} ^ {K - 1}\right) + \beta^ {K - 1} \left(\boldsymbol {g} ^ {K}, \boldsymbol {P} ^ {K - 2}\right) \\ = - \left(\boldsymbol {g} ^ {K}, \boldsymbol {g} ^ {K - 1}\right) = 0 \\ \end{array}
$$

式(7-44)得证。

下面根据这四个性质来推出 $\beta^K$ 的一个简单的计算公式。在式(7-41)中令 $j = K - 1$ ，可导出

$$
\begin{array}{l} \left(\boldsymbol {P} ^ {K}, \boldsymbol {g} ^ {K}\right) = \left(\boldsymbol {P} ^ {K}, \boldsymbol {g} ^ {K - 1} + \alpha^ {K - 1} \boldsymbol {Q} \boldsymbol {P} ^ {K - 1}\right) \\ = \left(\boldsymbol {P} ^ {K}, \boldsymbol {g} ^ {K - 1}\right) + \alpha^ {K - 1} \left(\boldsymbol {P} ^ {K}, \boldsymbol {Q} \boldsymbol {P} ^ {K - 1}\right) = \left(\boldsymbol {P} ^ {K}, \boldsymbol {g} ^ {K - 1}\right) \\ = \left(- \mathbf {g} ^ {K} + \boldsymbol {\beta} ^ {K} \mathbf {P} ^ {K - 1}, \mathbf {g} ^ {K - 1}\right) \\ = - \left(\boldsymbol {g} ^ {K}, \boldsymbol {g} ^ {K - 1}\right) + \boldsymbol {\beta} ^ {K} \left(\boldsymbol {P} ^ {K - 1}, \boldsymbol {g} ^ {K - 1}\right) \\ \end{array}
$$

由性质4知 $(\pmb{g}^{K},\pmb{g}^{K - 1}) = 0$ ，因此得

$$\beta^ {K} = \frac {\left(\boldsymbol {P} ^ {K} , \boldsymbol {g} ^ {K}\right)}{\left(\boldsymbol {P} ^ {K - 1} , \boldsymbol {g} ^ {K - 1}\right)} \tag {7-45}$$

再利用式(7-26)，可得

$$
\begin{array}{l} \beta^ {K} = \frac {\left(- \mathbf {g} ^ {K} + \boldsymbol {\beta} ^ {K} \mathbf {P} ^ {K - 1} , \mathbf {g} ^ {K}\right)}{\left(- \mathbf {g} ^ {K - 1} + \boldsymbol {\beta} ^ {K - 1} \mathbf {P} ^ {K - 2} , \mathbf {g} ^ {K - 1}\right)} \\ = \frac {- \left(\boldsymbol {g} ^ {K} , \boldsymbol {g} ^ {K}\right) + \beta^ {K} \left(\boldsymbol {P} ^ {K - 1} , \boldsymbol {g} ^ {K}\right)}{- \left(\boldsymbol {g} ^ {K - 1} , \boldsymbol {g} ^ {K - 1}\right) + \beta^ {K - 1} \left(\boldsymbol {P} ^ {K - 2} , \boldsymbol {g} ^ {K - 1}\right)} \\ \end{array}
$$

由性质3,就可得出

$$\beta^ {K} = \frac {\left(\mathbf {g} ^ {K} , \mathbf {g} ^ {K}\right)}{\left(\mathbf {g} ^ {K - 1} , \mathbf {g} ^ {K - 1}\right)} = \frac {\left\| \mathbf {g} ^ {K} \right\| ^ {2}}{\left\| \mathbf {g} ^ {K - 1} \right\| ^ {2}} \tag {7-46}$$

用式(7-46)计算 $\beta^K$ ，只用到 $F(X)$ 在 $X^K$ 和 $X^{K - 1}$ 两处的梯度，因此非常方便。式(7-46)对二次函数是精确的，对非二次函数，它只是一个近似公式。

将共轭梯度法求 $F(X)$ 的极小解的算式归纳如下：

(1) 算梯度 $g^{K}=\left(\frac{\partial F}{\partial X}\right)_{K}$   
(2) 算共轭系数 $\beta^{K}=\frac{\left\|\boldsymbol{g}^{K}\right\|^{2}}{\left\|\boldsymbol{g}^{K-1}\right\|^{2}},\quad\beta^{0}=0$   
(3) 算共轭梯度 $P^{K} = -g^{K} + \beta^{K}P^{K-1}, P^{0} = -g^{0}$   
(4) 递推逼近极值点解 $X^{K+1}=X^{K}+\alpha^{K}P^{K}$

$\alpha^K$ 用一维寻优决定。
