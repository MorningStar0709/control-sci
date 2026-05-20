性质3 若 $\pmb{g}^{\kappa} = \left(\frac{\partial F}{\partial X}\right)_{\kappa}\neq 0$ ，则必有

$$\left(\boldsymbol {g} ^ {K}, \boldsymbol {P} ^ {j - 1}\right) = 0 \quad 1 \leqslant j \leqslant K \tag {7-36}$$

(7-36)说明, $F(X)$ 在 $X=X^{K}$ 处的梯度 $g^{K}$ 与以前各步的共轭梯度寻找方向都正交。

证明 重复使用

$$\boldsymbol {X} ^ {K} = \boldsymbol {X} ^ {K - 1} + \alpha^ {K - 1} \boldsymbol {P} ^ {K - 1}$$

得到

$$\boldsymbol {X} ^ {K} = \boldsymbol {X} ^ {j} + \sum_ {i = j} ^ {K - 1} \alpha^ {i} \boldsymbol {P} ^ {i} \quad 0 \leqslant j \leqslant K - 1 \tag {7-37}$$

由式(7-22)所假定的二次函数 $F(X)$ ，可得

$$\boldsymbol {g} ^ {K} = \left(\frac {\partial F}{\partial \boldsymbol {X}}\right) _ {K} = \boldsymbol {a} + \boldsymbol {Q} \boldsymbol {X} ^ {K} \tag {7-38}$$

设 $X = X^{*}$ 为极小点，则

$$\boldsymbol {g} \left(X ^ {*}\right) = \boldsymbol {a} + Q X ^ {*} = \boldsymbol {0} \tag {7-39}$$

式(7-38)减去式(7-39)，得

$$\boldsymbol {g} ^ {K} = \boldsymbol {Q} \left(\boldsymbol {X} ^ {K} - \boldsymbol {X} ^ {*}\right) \tag {7-40}$$

式 $(7-37)$ 代入式 $(7-40)$ ，得

$$
\begin{array}{l} \boldsymbol {g} ^ {K} = \boldsymbol {Q} \boldsymbol {X} ^ {j} + \sum_ {i = j} ^ {K - 1} \boldsymbol {Q} \alpha^ {i} \boldsymbol {P} ^ {i} - \boldsymbol {Q} \boldsymbol {X} ^ {*} \\ = \boldsymbol {g} ^ {j} + \sum_ {i = j} ^ {K - 1} \boldsymbol {Q} \alpha^ {i} \boldsymbol {P} ^ {i} \quad 0 \leqslant j \leqslant K - 1 \tag {7-41} \\ \end{array}
$$

上式两边对 $P^{j - 1}$ 作内积，得

$$\left(\boldsymbol {g} ^ {K}, \boldsymbol {P} ^ {j - 1}\right) = \left(\boldsymbol {g} ^ {j}, \boldsymbol {P} ^ {j - 1}\right) + \sum_ {i = j} ^ {K - 1} \boldsymbol {\alpha} ^ {i} \left(\boldsymbol {Q} \boldsymbol {P} ^ {i}, \boldsymbol {P} ^ {j - 1}\right) \tag {7-42}$$

由性质2知 $(\boldsymbol{g}^{j},\boldsymbol{P}^{j-1})=0$ ，再由 $P^{i},i=j,\cdots,k-1$ 与 $P^{j-1}$ 是Q共轭的定义可知式(7-42)右端第二项也为0，因此

$$(\pmb {g} ^ {K}, \pmb {P} ^ {j - 1}) = 0 \quad 1 \leqslant j \leqslant K$$

式 $(7-36)$ 得证。

如果取 $K = n$ ，则

$$\left(\boldsymbol {g} ^ {n}, \boldsymbol {P} ^ {j - 1}\right) = 0 \quad 1 \leqslant j \leqslant n \tag {7-43}$$

但 $P^{0}, P^{1}, \cdots, P^{n-1}$ 是线性无关的，它们构成 $R^{n}$ 中一组基， $g^{n}$ 与所有基正交，而 $R^{n}$ 中只有 n 个基，故 $g^{n} = 0$ 。这说明 $X^{n}$ 处的梯度为零，即 $X^{n}$ 为二次函数 $F(X)$ 的极小点。

由此可见，在 $\mathbf{R}^n$ 空间中，对二次函数 $F(X)$ 用式(7-25)所示的共轭梯度法寻优，迭代至多 $n$ 步就可达到极小点。如果一个算法能在有限步内求出二次函数的极小点，就称这个算法具有二阶收敛性或有限步收敛性。在实际计算时，由于舍入误差，总要多进行几步才能达到所需精度的结果，对于非二次的一般指标函数则更是如此。

性质4 若 $\pmb{g}^{\kappa} = \left(\frac{\partial F}{\partial X}\right)_{K}\neq 0$ ，则
