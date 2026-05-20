# 例 A.9 部分分式展开法：复根各不相同

求函数 $f(t)$ ，其拉普拉斯变换为

$$F (s) = \frac {1}{s (s ^ {2} + s + 1)}$$

解答。将 $F(s)$ 写为

$$F (s) = \frac {C _ {1}}{s} + \frac {C _ {2} s + C _ {3}}{s ^ {2} + s + 1}$$

用消去法我们求得

$$C _ {1} = s F (s) \mid_ {s = 0} = 1$$

令 $C_{1}=1$ 并且将分子通过部分分式展开得

$$(s ^ {2} + s + 1) + (C _ {2} s + C _ {3}) s = 1$$

求解 $C_2$ 和 $C_3$ 后，我们得到 $C_2 = -1$ 和 $C_3 = -1$ 为了使它更适合使用拉普拉斯变换表，我们重写上式如下：

$$F (s) = \frac {1}{s} - \frac {s + \frac {1}{2} + \frac {1}{2}}{\left(s + \frac {1}{2}\right) ^ {2} + \frac {3}{4}}$$

从表中我们得到

$$f (t) = \left(1 - \mathrm{e} ^ {- t / 2} \cos \left(\sqrt {\frac {3}{4}} t\right) - \frac {1}{\sqrt {3}} \mathrm{e} ^ {- t / 2} \sin \left(\sqrt {\frac {3}{4}} t\right)\right) 1 (t) = \left(1 - \frac {2}{\sqrt {3}} \mathrm{e} ^ {- t / 2} \cos \left(\frac {\sqrt {3}}{2} t - \frac {\pi}{6}\right)\right) 1 (t)$$

或者，可将 $F(s)$ 写成

$$F (s) = \frac {C _ {1}}{s} + \frac {C _ {2}}{s - p _ {1}} + \frac {C _ {2} ^ {*}}{s - p _ {1} ^ {*}} \tag {A.24}$$

其中： $p_{1}=-\frac{1}{2}+j\frac{\sqrt{3}}{2};C_{1}=1$ 。此时

$$C _ {2} = (s - p _ {1}) F (s) \mid_ {s = p _ {1}} = - \frac {1}{2} + \mathrm{j} \frac {1}{2 \sqrt {3}}C _ {3} ^ {*} = - \frac {1}{2} - \mathrm{j} \frac {1}{2 \sqrt {3}}$$

和

$$
\begin{array}{l} f (t) = (1 + 2 \mid C _ {2} \mid \mathrm{e} ^ {\alpha t} \cos [ \beta t + \arg (C _ {2}) ] 1 (t) = \left(1 + \frac {2}{\sqrt {3}} \mathrm{e} ^ {- t / 2} \cos \left[ \frac {\sqrt {3}}{2} t + \frac {5 \pi}{6} \right]\right) 1 (t) \\ = \left(1 - \frac {2}{\sqrt {3}} \mathrm{e} ^ {- t / 2} \cos \left[ \frac {\sqrt {3}}{2} t - \frac {5 \pi}{6} \right]\right) 1 (t) \\ \end{array}
$$

以下部分分式展开式可用 Matlab 计算：

$$
\begin{array}{l} \text { num } = 1; \quad \% \text { form   numerator } \\ \text { den } = \text { conv } ([ 1 0 ], [ 1 1 1 ]); \quad \% \text { form   denominator } \\ [ r, p, k ] = \text { residue(num,den)} \quad \% \text { compute residues } \\ \end{array}
$$

经过计算得

$$
\begin{array}{l} \boldsymbol {r} = \left[ - 0. 5 0 0 0 + 0. 2 8 8 7 \mathrm{j} - 0. 5 0 0 0 - 0. 2 8 8 7 \mathrm{j} 1. 0 0 0 0 \right] ^ {\mathrm{T}}; \\ \boldsymbol {p} = \left[ - 0. 5 0 0 0 + 0. 8 6 6 0 \mathrm{j} - 0. 5 0 0 0 - 0. 8 6 6 0 \mathrm{j} 0 \right] ^ {\mathrm{T}}; k = [ ] \\ \end{array}
$$

此结果与手算结果一致。应该注意的是，若使用拉普拉斯变换表，则第一种方法更好，第二种方法更适合检测 Matlab 结果。

在 Matlab 中使用如下命令也可以得到相同的结果：

$$
\begin{array}{l} \text {syms s t} \\ \text {ilaplace(1 / (s^ {*} (s ^ {\wedge} 2 + s + 1))}). \end{array}
$$

重极点 对于 $F(s)$ 有重极点的情况，部分分式展开的计算过程需要调整。如果 $p_{1}$ 是三重极点，可将部分分式写成：
