# 6.3 正实传递函数

定义6.4 设有一个 $p \times p$ 正则有理传递函数矩阵 $G(s)$ , 如果

- $G(s)$ 所有元素的极点都满足 $\operatorname{Re}[s] \leqslant 0$ ,   
- 对于所有实数 $\omega, j\omega$ 不是 $G(s)$ 的任一元素的极点，矩阵 $G(j\omega) + G^{\mathrm{T}}(-j\omega)$ 是半正定的，  
- $G(s)$ 任一元素的任一纯虚数极点 $j\omega$ 是单阶的，且留数矩阵 $\lim_{s\to j\omega}(s - j\omega)G(s)$ 是半正定埃尔米特(Hermit)矩阵。

则 $G(s)$ 是正实的。如果对于某个 $\varepsilon > 0, G(s - \varepsilon)$ 是正实的，则传递函数 $G(s)$ 称为严格正实的 $^{①}$ 。

当 $p = 1$ 时, 定义6.4的第二个条件简化为 $\operatorname{Re}[G(j\omega)] \geqslant 0, \forall \omega \in R$ , 当 $G(j\omega)$ 的奈奎斯特曲线位于右半闭复平面时, 该式成立。只有当传递函数的相对阶为0或1时②, 这一条件方可满足。

下一引理给出严格正实传递函数的等效特征。

引理6.1 设 $G(s)$ 是一个 $p \times p$ 的正则有理传递函数矩阵，并假设 $\operatorname{det}[G(s) + G^{\mathrm{T}}(-s)]$ 不恒为零③，如果 $G(s)$ 是严格正实的，则当且仅当

- $G(s)$ 是赫尔维茨矩阵, 即 $G(s)$ 的所有元素极点的实部都为负.  
- 对于所有 $\omega \in R, G(j\omega) + G^{\mathrm{T}}(-j\omega)$ 是正定的.  
- $G(\infty) + G^{\mathrm{T}}(\infty)$ 或者是正定的,或者是半正定的,且 $\lim_{\omega \to \infty}\omega^{2}(p - q)\det [G(j\omega) + G^{\mathrm{T}}(-j\omega)] > 0$ ,其中 $q = \operatorname {rank}[G(\infty) + G^{\mathrm{T}}(\infty)]$ 。

证明:参见附录 C.11。

如果 $G(\infty) + G^{\mathrm{T}}(\infty) = 0$ ，可取 $M = I$ 。在标量情况下 $(p = 1)$ ，引理的频域条件简化为对于所有 $\omega \in R, \operatorname{Re}[G(j\omega)] > 0$ ，并且 $G(\infty) > 0$ 或 $G(\infty) = 0$ ，以及 $\lim_{\omega \to \infty} \omega^2 \operatorname{Re}[G(j\omega)] > 0$ 。

例6.4 传递函数 $G(s) = 1 / s$ 是正实的,因为它没有满足 $\operatorname{Re}[s] > 0$ 的极点,仅在 $s = 0$ 有一个单极点,其留数为1,且

$$\mathrm{Re} [ G (j \omega) ] = \mathrm{Re} \left[ \frac {1}{j \omega} \right] = 0, \forall \omega \neq 0$$

但该传递函数不是严格正实的,因为对于任意 $\varepsilon > 0, 1/(s - \varepsilon)$ 有满足 Re[s] > 0 的极点。当 a > 0 时,传递函数 $G(s) = 1/(s + a)$ 是正实的,因为没有 Re[s] ≥ 0 的极点,且

$$\operatorname{Re} [ G (j \omega) ] = \frac {a}{\omega^ {2} + a ^ {2}} > 0, \forall \omega \in R$$

由于对于每个 $a > 0$ 都如此，可看出对于每个 $\varepsilon \in (0, a)$ ，传递函数 $G(s - \varepsilon) = 1 / (s + a - \varepsilon)$ 是正实的。所以， $G(s) = 1 / (s + a)$ 是严格正实的。注意到

$$\lim _ {\omega \rightarrow \infty} \omega^ {2} \mathrm{Re} [ G (j \omega) ] = \lim _ {\omega \rightarrow \infty} \frac {\omega^ {2} a}{\omega^ {2} + a ^ {2}} = a > 0$$

由引理6.1可得出相同的结论。传递函数

$$G (s) = \frac {1}{s ^ {2} + s + 1}$$

不是正实的,因为其相对阶是2。通过计算

$$\mathrm{Re} [ G (j \omega) ] = \frac {1 - \omega^ {2}}{(1 - \omega^ {2}) ^ {2} + \omega^ {2}} < 0, \forall | \omega | > 1$$

也可以看出这一点。考虑 $2 \times 2$ 传递函数矩阵

$$
G (s) = \frac {1}{s + 1} \left[ \begin{array}{l l} 1 & 1 \\ 1 & 1 \end{array} \right]
$$
