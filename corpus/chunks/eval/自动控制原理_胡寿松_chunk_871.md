# (1) $A(s) = 0$ 无重根

这时， $F(s)$ 可展开为 $\pmb{n}$ 个简单的部分分式之和，每个部分分式都以 $A(s)$ 的一个因式作为其分母，即

$$F (s) = \frac {c _ {1}}{s - s _ {1}} + \frac {c _ {2}}{s - s _ {2}} + \dots + \frac {c _ {i}}{s - s _ {i}} + \dots + \frac {c _ {n}}{s - s _ {n}} = \sum_ {i = 1} ^ {n} \frac {c _ {i}}{s - s _ {i}} \tag {A-13}$$

式中， $c_{i}$ 为待定常数，称为 $F(s)$ 在极点 $s_i$ 处的留数，可按下式计算：

$$c _ {i} = \lim _ {s \to s _ {i}} [ (s - s _ {i}) F (s) ] \tag {A-14}$$

或 $c_{i} = \frac{B(s)}{\dot{A}(s)}\Bigg|_{s = s_{i}}$ (A-15)

式中， $\dot{A}(s)$ 为 $A(s)$ 对 $s$ 求一阶导数。

根据拉氏变换的线性性质,从式(A-13)可求得原函数

$$f (t) = \mathcal {L} ^ {- 1} [ F (s) ] = \mathcal {L} ^ {- 1} \left[ \sum_ {i = 1} ^ {n} \frac {c _ {i}}{s - s _ {i}} \right] = \sum_ {i = 1} ^ {n} c _ {i} \mathrm{e} ^ {s _ {i} t} \tag {A-16}$$

上述表明,有理代数分式函数的拉氏反变换,可表示为若干指数项之和。

例A-5 求 $F(s) = \frac{s + 2}{s^2 + 4s + 3}$ 的原函数 $f(t)$ 。

解 将 $F(s)$ 的分母因式分解为

$$s ^ {2} + 4 s + 3 = (s + 1) (s + 3)$$

则 $F(s) = \frac{s + 2}{s^2 + 4s + 3} = \frac{s + 2}{(s + 1)(s + 3)} = \frac{c_1}{s + 1} + \frac{c_2}{s + 3}$

按式(A-14)计算,得

$$c _ {1} = \lim _ {s \rightarrow 1} [ (s + 1) F (s) ] = \lim _ {s \rightarrow 1} \frac {s + 2}{s + 3} = \frac {1}{2}c _ {2} = \lim _ {s \rightarrow 3} [ (s + 3) F (s) ] = \lim _ {s \rightarrow 3} \frac {s + 2}{s + 1} = \frac {1}{2}$$

因此，由式(A-16)可求得原函数

$$f (t) = \frac {1}{2} (\mathrm{e} ^ {- t} + \mathrm{e} ^ {- 3 t})$$

例A-6 求 $F(s) = \frac{s - 3}{s^2 + 2s + 2}$ 的原函数 $f(t)$ 。

解 将 $F(s)$ 的分母因式分解为

$$s ^ {2} + 2 s + 2 = (s + 1 - \mathrm{j}) (s + 1 + \mathrm{j})$$

本例 $F(s)$ 的极点为一对共轭复数，仍可用式(A-16)求原函数。因此， $F(s)$ 可写为

$$
\begin{array}{l} F (s) = \frac {s - 3}{s ^ {2} + 2 s + 2} = \frac {s - 3}{(s + 1 - j) (s + 1 + j)} \\ = \frac {c _ {1}}{s + 1 - j} + \frac {c _ {2}}{s + 1 + j} \\ \end{array}
$$

式中 $c_{1} = \lim_{s\to -1 + j}[ (s + 1 - j)F(s)] = \lim_{s\to -1 + j}\frac{s - 3}{s + 1 + j} = \frac{-4 + j}{2j}$

$$c _ {2} = \lim _ {s \rightarrow 1 - j} [ (s + 1 + j) F (s) ] = \lim _ {s \rightarrow 1 - j} \frac {s - 3}{s + 1 - j} = - \frac {- 4 - j}{2 j}$$

所以，原函数

$$f (t) = c _ {1} \mathrm{e} ^ {(- 1 + j) t} + c _ {2} \mathrm{e} ^ {(- 1 - j) t} = \mathrm{e} ^ {- t} (\cos t - 4 \sin t)$$

如果函数 $F(s)$ 的分母是 $s$ 的二次多项式，可将分母配成二项平方和的形式，并作为一个整体来求原函数。本例的 $F(s)$ 可写为

$$F (s) = \frac {s - 3}{s ^ {2} + 2 s + 2} = \frac {s - 3}{(s + 1) ^ {2} + 1} = \frac {s + 1}{(s + 1) ^ {2} + 1} - \frac {4}{(s + 1) ^ {2} + 1}$$

应用位移定理并查拉氏变换对照表 A-3, 原函数求得为

$$f (t) = \mathscr {L} ^ {- 1} \left[ \frac {s + 1}{(s + 1) ^ {2} + 1} - \frac {4}{(s + 1) ^ {2} + 1} \right] = e ^ {- t} (\cos t - 4 \sin t)$$
