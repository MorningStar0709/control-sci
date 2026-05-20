# C. 22 证明定理 13.2

系统

$$\dot {x} = f (x) + g (x) u$$

是可反馈线性化的,当且仅当存在一个足够光滑的函数 $h(x)$ ,使系统

$$\dot {x} = f (x) + g (x) u, \quad y = h (x)$$

在 $D_0 \subset D$ 上具有相对阶 $n$ , 即 $h(x)$ 满足

$$L _ {g} L _ {f} ^ {i} h (x) = 0, \quad 0 \leqslant i \leqslant n - 2 \quad \text {和} \quad L _ {g} L _ {f} ^ {n - 1} h (x) \neq 0, \forall x \in D _ {0} \tag {C.93}$$

这样,为了证明该定理而需要证明,存在满足式(C.93)的 $h(x)$ 相当于条件1和条件2。

必要性: 假设存在 $h(x)$ 满足式(C.93)。引理 C.9 说明秩 G=n，则 D 是非奇异的，且维数为 n-1。根据式(C.92)，当 k=0, $\rho=n$ 时，有

$$L _ {g} h (x) = L _ {a d _ {f} g} h (x) = \dots = L _ {a d _ {f} ^ {n - 2} g} h (x) = 0$$

上式可写为 $dh(x)[g(x),ad_{f}g(x),\cdots,ad_{f}^{n-2}g(x)]=0$

该方程表明D是完全可积的,且根据 Frobenius 定理可知D是对合的。

充分性:假设满足条件1和条件2,则D是非奇异的,且维数为n-1。根据Frobenius定理,存在 $h(x)$ 满足 $L_{g}h(x)=L_{ad_{f}g}h(x)=\cdots=L_{ad_{f}^{n-2}g}h(x)=0$

利用雅可比恒等式(见习题13.8),可以验证

$$L _ {g} h (x) = L _ {g} L _ {f} h (x) = \dots = L _ {g} L _ {f} ^ {n - 2} h (x) = 0$$

而且 $dh(x)\mathcal{G}(x)=dh(x)[g(x),ad_{f}g(x),\cdots,ad_{f}^{n-1}g(x)]=[0,\cdots,0,L_{ad_{f}^{n-1}g}h(x)]$

由于秩 $\mathcal{G} = n$ 且 $dh(x) \neq 0$ , 则 $L_{adj^{n-1}}gh(x) \neq 0$ 一定成立。利用雅可比恒等式可以验证 $L_g L_f^{n-1}h(x) \neq 0$ , 由此完成了该定理的证明。
