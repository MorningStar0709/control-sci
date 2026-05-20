把 $M$ 看作实数时，上式是 $M$ 作自变量的分段线性函数；自变量的定义域表明，随着 $M$ 与 $z$ 的增大，段数由1向上增加。一般情况下，这种函数在分段点 $j_{z}$ 处可能向上跳跃而产生不连续。下面来证明上述分段线性函数一定是连续的。考察 $r \to r - 1 \to \dots \to r - j_{u} + 1 \to s$ 的路，其重为 $t(r - j_{u} + 1, s)$ ，长为 $j_{u}$ ；而 $r \to r - 1 \to \dots \to r - j_{u} \to s$ 的路，重为 $t(r - j_{u}, s) = t(r - j_{u} + 1, s)\widehat{t}(u)$ ，长为 $j_{u} + 1$ 。易知：这二个路重值都在线性函数 $t(r - j_{u}, s)\widehat{t}(u)^{M - 1 - j_{u}}$ 上，对应自变量 $M = j_{u}, j_{u + 1}$ 。另一方面， $M = j_{u}$ 时，对应的最重路重为 $\sum_{w=1}^{u-1} t(r - j_{w}, s)\widehat{t}_{w}^{M - 1 - j_{w}}$ ，它 $\geqslant t(r - j_{u} + 1, s) = t(r - j_{u}, s)\widehat{t}(u)^{-1}$ ，所以在 $j_{u}$ 处上述分段线性函数不可能向上跳跃，必是连续的。易知定义域式 $j_{z} < M \leqslant j_{z+1}$ 现在可以取消掉， $f_{1}$ 中可把 $z$ 改为 $P$ 。

现在再来进行第二步，先研究从 $r$ 经过 $>s$ 的点再到 $s$ 的路。类似地可知，最重为

$$f _ {2} \stackrel {\mathrm{def}} {=} \sum_ {v = 1} ^ {Q} t (r, s + j _ {v} ^ {\prime}) \tilde {t} _ {v} ^ {M - 1 - j _ {v} ^ {\prime}}.$$

其次研究从 $r$ 经过 $< r$ 的点，再经过 $>s$ 的点，最后到 $s$ 的路。设路上的编号最小的点为 $r - j_u$ ，编号最大的点为 $s \mid j_v$ 。若 $\widehat{t}(u) \geqslant \widetilde{t}_v$ ，类似地只需看不含回路的路。设路上小于 $s$ 的编号最小的点为 $p$ ，则由于无回路，必有 $p$ 到 $s + j_v$ 的弧。现把 $p \to s + j_v \to s + j_v - 1 \to \cdots \to s$ 的路段换成 $p \to s$ 的弧，再在 $\widehat{t}(u)$ 上多绕圈而使总路长不变。易知新路更重（或重不变），这就归结为从 $r$ 经过 $< s$ 的点到 $s$ 的路。若 $\widehat{t}(u) < \widetilde{t}_v$ ，类似地设路上大于 $s$ 的编号最小的点为 $p$ ，把 $r \to r - 1 \to \cdots \to r - j_u \to \cdots \to p$ 的路段换成 $r \to p$ 的板，再在 $\widetilde{t}(v)$ 上多绕圈而使总路长不变，于是归结为从 $r$ 经过 $>s$ 的点到 $s$ 的路。综上所述，长为 $M$ 的最重路的重为 $f_1 \oplus f_2$ 。

最后设 $r > s$ . 当 $M < r - s$ 时, $r \to s$ 无长的为 $M$ 的路, $a_{r,s}(M) = -\infty$ ; 当 $M \geqslant r - s$ 时, 类似于 $r \leqslant s$ 的情况, 但 $j_1 = j_1' \stackrel{\mathrm{def}}{=} r - s - 1$ , 可证: 长为 $M$ 的最重路的重为 $f_1 \oplus f_2$ . 由定理 11.8.5 与引理 11.8.1 可得本定理的其他结论.

由定理11.8.6易得以下定理：

定理11.8.7 不用 $D$ 上运算，而用普通运算描写，系统(11.8.8)的批生产周期 $\lambda(M)$ 为

$$\lambda (M) = \max _ {1 \leqslant j \leqslant p} \left\{\alpha_ {j} M + \beta_ {j} \right\}, \tag {11.8.10}$$

因而目标函数为

$$f (M) = \left(W _ {2} M + W _ {1}\right) / \max _ {1 \leqslant j \leqslant p} \left\{\alpha_ {j} M + \beta_ {j} \right\}. \tag {11.8.11}$$

显然，式(11.8.10)形式的函数是连续分段线性增凸函数.

为求目标函数 $f(M)$ 的最大值，只需求 $1 / f(M)$ 的最小值。由式(11.8.11)，可把 $1 / f(M)$ 记为

$$g (M) = \max _ {1 \leqslant j \leqslant p} \left\{\alpha_ {j} M + \beta_ {j} \right\} / \left(W _ {2} M + W _ {1}\right). \tag {11.8.12}$$

定理11.8.8 上式所示 $g(M)$ 在

$$M = (\beta_ {j _ {0}} - \beta_ {j _ {0} + 1}) / (\alpha_ {j _ {0} + 1} - \alpha_ {j _ {0}})$$

处取到最小值，这里 $\alpha_{j}$ 已被重新标定下标，满足
