证明 用反证法。若不线性独立，则必存在不全为零的常数 $C_1, C_2, \cdots, C_{n-1}$ 使

$$\sum_ {i = 0} ^ {n - 1} C _ {i} \boldsymbol {P} ^ {i} = \mathbf {0} \tag {7-30}$$

上式左端各项对 $QP^{j}$ 取内积后有

$$\sum_ {i = 0} ^ {n - 1} C _ {i} \left(\boldsymbol {P} ^ {i}, \boldsymbol {Q} \boldsymbol {P} ^ {j}\right) = C _ {j} \left(\boldsymbol {P} ^ {j}, \boldsymbol {Q} \boldsymbol {P} ^ {j}\right) = \mathbf {0} \tag {7-31}$$

因为 Q 正定, 上式对每一个 $P^{j}$ 成立, 所以必须有 $C_{j}=0, j=0,1,2,\cdots,n-1$ 。与假设矛盾, 这说明 $P^{0}, P^{1}, \cdots, P^{n-1}$ 是线性独立的, 它们构成了 $R^{n}$ 空间中的一组基向量。

按照这个性质, 函数 $F(X)$ 的极小点 $X = X^{*}$ 可用这组基来表示, 即

$$\boldsymbol {X} ^ {*} = \sum_ {i = 0} ^ {n - 1} C _ {i} \boldsymbol {P} ^ {i} \tag {7-32}$$

其中， $C_{i}, i=0,1,\cdots,n-1$ 可这样来求：作内积

$$\left(\boldsymbol {Q} \boldsymbol {X} ^ {*}, \boldsymbol {P} ^ {K}\right) = \left(\sum_ {i = 0} ^ {n - 1} C _ {i} \boldsymbol {Q} \boldsymbol {P} ^ {i}, \boldsymbol {P} ^ {K}\right) = C _ {K} \left(\boldsymbol {Q} \boldsymbol {P} ^ {K}, \boldsymbol {P} ^ {K}\right)$$

从而

$$C _ {K} = \frac {\left(\boldsymbol {Q} \boldsymbol {X} ^ {*} , \boldsymbol {P} ^ {K}\right)}{\left(\boldsymbol {Q} \boldsymbol {P} ^ {K} , \boldsymbol {P} ^ {K}\right)} K = 0, 1, 2, \dots , n - 1 \tag {7-33}$$

性质2 如果 $\pmb{g}^{\kappa} = \left(\frac{\partial F}{\partial X}\right)_{K}\neq 0$ ，则有

$$\left(\boldsymbol {P} ^ {K}, \boldsymbol {g} ^ {K + 1}\right) = 0 \tag {7-34}$$

式中， $\left(\frac{\partial F}{\partial X}\right)_K = \left(\frac{\partial F}{\partial X}\right)_{X = X^K}$ 。(7-34)说明，在 $X = X^{K + 1}$ 处函数 $F(X)$ 的梯度 $\pmb{g}^{K + 1}$ 与前一步的寻找方向 $\pmb{P}^K$ 必正交。

证明 若不然, 不妨先设 $(P^K, g^{K+1}) > 0$ 。再设 $F(X^K + \alpha^K P^K) = \min_{\alpha > 0} F(X^K + \alpha P^K)$ , 即 $\alpha^K$ 是最优步长。在 $\alpha^K$ 附近选一个 $\alpha_0^K < \alpha^K$ , 将 $F(X)$ 在 $X = X^{K+1} = X^K + \alpha^K P^K$ 处展开, 保留一阶项后, 有

$$F \left(\boldsymbol {X} ^ {K} + \alpha^ {K} \boldsymbol {P} ^ {K}\right) - F \left(\boldsymbol {X} ^ {K} + \alpha_ {0} ^ {K} \boldsymbol {P} ^ {K}\right) = \left(\frac {\partial F}{\partial \boldsymbol {X}}\right) _ {K + 1} ^ {T} \left(\alpha^ {K} - \alpha_ {0} ^ {K}\right) \boldsymbol {P} ^ {K}= \left(\alpha^ {K} - \alpha_ {0} ^ {K}\right) \left(\boldsymbol {g} ^ {K + 1}\right) ^ {\mathrm{T}} \boldsymbol {P} ^ {K} = \left(\alpha^ {K} - \alpha_ {0} ^ {K}\right) \left(\boldsymbol {g} ^ {K + 1}, \boldsymbol {P} ^ {K}\right) > 0 \tag {7-35}$$

这与 $F(X^{K} + \alpha^{K}P^{K})$ 为极小相矛盾。若设 $(P^{K}, g^{K+1}) < 0$ 则可取 $\alpha_{0}^{K} > \alpha^{K}$ ，同样得出矛盾，于是必有式(7-34)成立。
