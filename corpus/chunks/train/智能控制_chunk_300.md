# 2. 鲁棒自适应控制律

为了消除逼近误差 $\omega$ 造成的影响使 $\dot{V}(t)\leqslant0$ 恒成立，保证系统绝对稳定，在控制律中采用了鲁棒项。设计鲁棒自适应控制律为

$$\boldsymbol {\tau} = \boldsymbol {D} (\boldsymbol {q}) \ddot {\boldsymbol {q}} _ {\mathrm{r}} + \boldsymbol {C} (\boldsymbol {q}, \dot {\boldsymbol {q}}) \boldsymbol {q} _ {\mathrm{r}} + \boldsymbol {G} (\boldsymbol {q}) + \boldsymbol {F} (\boldsymbol {q}, \dot {\boldsymbol {q}}, \ddot {\boldsymbol {q}} | \boldsymbol {\Theta}) - \boldsymbol {K} _ {\mathrm{D}} s - W \operatorname{sgn} (s) \tag {5.76}$$

式中， $W=\mathrm{diag}[w_{M_{1}},\cdots,w_{M_{n}}],w_{M_{i}}\geqslant|w_{i}|,i=1,2,\cdots,n$ 。

同理,将控制律式(5.76)代入 $\dot{V}(t)$ ,得

$$\dot {V} (t) = - \mathbf {s} ^ {\mathrm{T}} \mathbf {K} _ {\mathrm{D}} \mathbf {s} \leqslant 0$$

由于当且仅当 s=0 时， $\dot{V}=0$ ，即当 $\dot{V}\equiv0$ 时， $s\equiv0$ ，根据 LaSalle 不变性原理 $^{[35]}$ ，闭环系统为渐近稳定，即当 $t\to\infty$ 时， $s\to0$ ，系统的收敛速度取决于 $K_{D}$ 。

由于 $V \geqslant 0, \dot{V} \leqslant 0$ ，则当 $t \to \infty$ 时， $V$ 有界，从而 $\tilde{\pmb{\theta}}$ 有界。

假设机器人关节个数为 $n$ 个，如果采用基于MIMO的模糊系统 $\widehat{F} (\pmb {q},\dot{\pmb{q}},\ddot{\pmb{q}}\mid \Theta)$ 来逼近 $F(q,\dot{q},$ $\ddot{q})$ ，则对每个关节构造模糊系统来说，输入变量个数为3个。如果针对 $n$ 个关节机器人力臂，对每个输入变量设计 $k$ 个隶属函数，则规则总数为 $k^{3n}$ 。

例如，机器人关节个数为2，每个关节输入变量个数为3，每个输入变量设计5个隶属函数，则规则总数为 $5^{3\times2}=5^{6}=15625$ ，如此多的模糊规则会导致计算量过大。为了减少模糊规则的个数，应针对 $F(\boldsymbol{q},\dot{\boldsymbol{q}},\ddot{\boldsymbol{q}},t)$ 的具体表达形式分别进行设计。
