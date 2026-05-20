# 2.2.3 拉普拉斯逆变换

本节将介绍拉普拉斯的逆变换(Inverse Laplace Transform)，它是反向使用拉普拉斯变换，将 $F(s)$ 变回时域函数 $f(t)$ ，即

$$f (t) = \mathcal {L} ^ {- 1} [ F (s) ] \tag {2.2.16}$$

请看下面的例子。

例 2.2.6 已知 $F(s)=\frac{-s+5}{s^{2}+5s+4}$ ，求 $f(t)$ 。

解：

$$F (s) = \frac {- s + 5}{s ^ {2} + 5 s + 4} = \frac {- s + 5}{(s + 4) (s + 1)} = \frac {A}{s + 4} + \frac {B}{s + 1} \tag {2.2.17}$$

此时可以用分式分解法求解 A 和 B。根据式(2.2.17)可得

$$A (s + 1) + B (s + 4) = - s + 5 \tag {2.2.18}$$

令 $s = -1$ ，可得

$$B (- 1 + 4) = 1 + 5\Rightarrow B = 2 \tag {2.2.19}$$

令 $s = -4$ ，可得

$$- 3 A = 9\Rightarrow A = - 3 \tag {2.2.20}$$

所以

$$F (s) = \frac {- 3}{s + 4} + \frac {2}{s + 1} \tag {2.2.21}$$

根据例2.2.1： $\mathcal{L}^{-1}\left[\frac{1}{s + a}\right] = \mathrm{e}^{-at}$ ，可得

$$f (t) = \mathcal {L} ^ {- 1} [ F (s) ] = \mathcal {L} ^ {- 1} \left[ \frac {- 3}{s + 4} + \frac {2}{s + 1} \right] = - 3 \mathrm{e} ^ {- 4 t} + 2 \mathrm{e} ^ {- t} \tag {2.2.22}$$

在式(2.2.21)中, 如果令 $F(s)$ 的分母部分等于 0 , 即 $\left\{ \begin{array}{l} s + 4 = 0 \\ s + 1 = 0 \end{array} \right.$ , 可以得到 $s$ 的两个解: $\left\{ \begin{array}{l} s_1 = -4 \\ s_2 = -1 \end{array} \right.$ 。再去对比式(2.2.22)可以发现, $s_1$ 与 $s_2$ 出现在了时间函数 $f(t)$ 的指数部分。因为它们两个都是负值, 所以决定了 $f(t)$ 随着时间 $t$ 的增加而不断地减小, 最终变为 0 。而一旦 $s_1$ 或者 $s_2$ 里面有一个为正值, $f(t)$ 则会随着时间的增加而趋于无穷大。

例 2.2.7 已知 $F(s)=\frac{4s+8}{s^{2}+2s+5}$ ，求 $f(t)$ 。

解：

$$
\begin{array}{l} F (s) = \frac {4 s + 8}{s ^ {2} + 2 s + 5} = \frac {4 s + 8}{(s + 1 + 2 j) (s + 1 - 2 j)} \\ = \frac {A}{(s + 1 + 2 j)} + \frac {B}{(s + 1 - 2 j)} \tag {2.2.23} \\ \end{array}
$$

利用分式分解法可得

$$
\left\{ \begin{array}{l} A = j + 2 \\ B = - j + 2 \end{array} \right. \tag {2.2.24}
$$

可以得到

$$
\begin{array}{l} f (t) = \mathcal {L} ^ {- 1} [ F (s) ] = (\mathrm{j} + 2) \mathrm{e} ^ {(- 1 - 2 \mathrm{j}) t} + (- \mathrm{j} + 2) \mathrm{e} ^ {(- 1 + 2 \mathrm{j}) t} \\ = \mathrm{e} ^ {- t} \left(\mathrm{je} ^ {- 2 \mathrm{j} t} + 2 \mathrm{e} ^ {- 2 \mathrm{j} t} - \mathrm{je} ^ {2 \mathrm{j} t} + 2 \mathrm{e} ^ {2 \mathrm{j} t}\right) \\ = \mathrm{e} ^ {- t} (\mathrm{j} (\mathrm{e} ^ {- 2 \mathrm{j} t} - \mathrm{e} ^ {2 \mathrm{j} t}) + 2 (\mathrm{e} ^ {- 2 \mathrm{j} t} + \mathrm{e} ^ {2 \mathrm{j} t})) \\ = \mathrm{e} ^ {- t} (2 \sin 2 t + 4 \cos 2 t) \tag {2.2.25} \\ \end{array}
$$

在例 2.2.7 中, $F(s)$ 分母部分为零时, 得到: $s_1 = -1 - 2j$ 和 $s_2 = -1 + 2j$ 出现在了 $f(t)$ 的指数部分。因为它们是复数, 根据欧拉公式, 复数将引入正弦 (余弦) 函数, 带来了振动。这说明, 当一个函数 $f(t)$ 经过拉普拉斯变换之后, 如果 $F(s)$ 分母部分的根存在虚部, 那么 $f(t)$ 就会存在振动。例 2.2.6 和例 2.2.7 说明, 通过分析 $F(s)$ 的根可以了解原函数 $f(t)$ 的时间表现。
