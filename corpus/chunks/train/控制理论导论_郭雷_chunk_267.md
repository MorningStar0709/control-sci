$$
\left[ \begin{array}{c} \widetilde {\gamma} _ {i j} ^ {1} \\ \vdots \\ \widetilde {\gamma} _ {i j} ^ {n} \end{array} \right] = \left[ \begin{array}{c c c} \frac {\partial^ {2} x _ {1}}{\partial y _ {j} \partial y _ {1}} & \dots & \frac {\partial^ {2} x _ {1}}{\partial y _ {j} \partial y _ {n}} \\ \vdots & & \vdots \\ \frac {\partial^ {2} x _ {n}}{\partial y _ {j} \partial y _ {1}} & \dots & \frac {\partial^ {2} x _ {n}}{\partial y _ {j} \partial y _ {n}} \end{array} \right] \left[ \begin{array}{c} \frac {\partial x _ {1}}{\partial y _ {i}}, \dots , \frac {\partial x _ {n}}{\partial y _ {i}} \end{array} \right] ^ {\mathrm{T}}
+ \Gamma \ltimes \left[ \frac {\partial x _ {1}}{\partial y _ {i}}, \dots , \frac {\partial x _ {n}}{\partial y _ {i}} \right] ^ {T} \ltimes \left[ \frac {\partial x _ {1}}{\partial y _ {j}} \dots \frac {\partial x _ {n}}{\partial y _ {j}} \right] ^ {T}. \tag {3.11.10}
$$

证明 设

$$f = \frac {\partial}{\partial y _ {i}} = \sum_ {s = 1} ^ {n} \frac {\partial}{\partial x _ {s}} \frac {\partial x _ {s}}{\partial y _ {i}},g = \frac {\partial}{\partial y _ {j}} = \sum_ {t = 1} ^ {n} \frac {\partial}{\partial x _ {t}} \frac {\partial x _ {t}}{\partial y _ {j}}.$$

回忆 $\gamma$ 的定义，可知

$$\sum_ {k = 1} ^ {n} \widetilde {\gamma} _ {i j} ^ {k} \frac {\partial}{\partial y _ {k}} = \nabla_ {f} g.$$

应用式 (3.11.8) 到上述等式即得式 (3.11.10).

定理3.11.2 在新坐标 $y$ 下， $\tilde{\Gamma}$ 是

$$\tilde {I} = D ^ {2} x D x + \Gamma \ltimes D x (I \otimes D x). \tag {3.11.11}$$

证明 直接计算可得
