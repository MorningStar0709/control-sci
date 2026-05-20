# A. 1.2 用部分分式展开法求拉普拉斯反变换

就像我们在第3章看到的，如果 $F(s)$ 是有理分式，那么求 $f(t)$ 的拉普拉斯变换最简单的方法就是利用部分分式展开法将 $F(s)$ 展开成在拉普拉斯变换表中能找到的简单项的和的形式。我们已经在3.1.5小节中讨论了单根的情况。在本节，将分析如何使用部分分式展开法来处理复根和重根的情况。

复极点 分母中二次因式有复数根时，分子中二次因式就成为一阶形式。如例 A.9 所示。每当函数存在一对共轭复极点，例如，

$$F (s) = \frac {C _ {1}}{s - p _ {1}} + \frac {C _ {2}}{s - p _ {1} ^ {*}}$$

时，我们可以证明

$$C _ {2} = C _ {1} ^ {*}$$

(见问题 3.1) 并且有

$$f (t) = C _ {1} \mathrm{e} ^ {p _ {1} t} + C _ {1} ^ {*} \mathrm{e} ^ {p _ {1} * t} = 2 \operatorname{Re} \left(C _ {1} \mathrm{e} ^ {p _ {1} t}\right)$$

假设 $p_1 = \alpha + j\beta$ ，我们可以重写 $f(t)$ 为简单的形式：

$$f (t) = 2 \mathrm{Re} \left\{C _ {1} \mathrm{e} ^ {p _ {1} t} \right\} = 2 \mathrm{Re} \left\{\left| C _ {1} \right| \mathrm{e} ^ {\mathrm{jarg} \left(C _ {1}\right)} \mathrm{e} ^ {(\alpha + \mathrm{j} \beta) t} \right\} = 2 \left| C _ {1} \right| \mathrm{e} ^ {\alpha t} \cos [ \beta t + \arg (C _ {1}) ] \tag {A.23}$$
