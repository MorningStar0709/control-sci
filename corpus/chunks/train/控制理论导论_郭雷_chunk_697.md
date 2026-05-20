则容易看出方程 (9.4.47) 中的 $R_{k}$ 收敛于某一 $\tilde{R}$ (当 $k \to \infty$ ), 其中对 LMS 情形, $\tilde{R} = I$ ; 对 FFLS 情形, $\tilde{R} = S^{-1}$ ; 而对 KF 情形 $\tilde{R}$ 满足 $\tilde{RS}\tilde{R} = Q / R$ . 将 $\tilde{R}$ 的值代入方程 (9.4.47) 知 $\Pi_{k} \xrightarrow[k \to \infty]{\longrightarrow} \Pi$ , 其中 $\Pi$ 满足 (忽略 $\mu^{2}\Pi$ 项):

LMS 情形

$$S \Pi + \Pi S = \mu R _ {w} S + \frac {\gamma^ {2}}{\mu} Q _ {\Delta},$$

FFLS 情形

$$\Pi = \frac {1}{2} \left[ \mu R _ {w} S ^ {- 1} + \frac {\gamma^ {2}}{\mu} Q _ {\Delta} \right],$$

KF 情形

$$(\bar {R} S) \Pi + \Pi (R S) ^ {\mathbf {T}} = \mu R _ {w} Q / R + \frac {\gamma^ {2}}{\mu} Q _ {\Delta}.$$

从上述表达式中容易看出， $\mu$ 的“最好”的选择是噪声灵敏性与跟踪能力之间的折中 (trade-off). 特别地，对 FFLS 情形，对 $\operatorname{tr}(\Pi)$ 求关于 $\mu$ 的最小值，可得

$$\mu = \gamma \sqrt {\frac {\operatorname{tr} Q _ {\Delta}}{R _ {w} \operatorname{tr} (S ^ {- 1})}}.$$

此式可以用来指导遗忘因子 $(1 - \mu)$ 的合理选取.
