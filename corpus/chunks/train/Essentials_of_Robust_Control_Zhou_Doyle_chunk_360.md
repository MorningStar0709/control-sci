$$
A _ {c} + B _ {c} B _ {c} ^ {*} P / \gamma^ {2} = \left[ \begin{array}{c c} A + B _ {1} B _ {1} ^ {*} Y _ {\infty} ^ {- 1} & B _ {2} F _ {\infty} - B _ {1} B _ {1} ^ {*} Y _ {\infty} ^ {- 1} Z _ {\infty} ^ {- 1} \\ 0 & A + B _ {1} B _ {1} ^ {*} X _ {\infty} / \gamma^ {2} + B _ {2} F _ {\infty} \end{array} \right]
$$

has no eigenvalues on the imaginary axis since $A + B _ { 1 } B _ { 1 } ^ { * } X _ { \infty } / \gamma ^ { 2 } + B _ { 2 } F _ { \infty }$ is stable and $A + B _ { 1 } B _ { 1 } ^ { * } Y _ { \infty } ^ { - 1 }$ is antistable. Thus, by Corollary 12.3, $\| T _ { z w } \| _ { \infty } < \gamma$ . ✷

Remark 14.1 It is appropriate to point out that the conditions stated in Lemma 14.3 are, in fact, necessary and sufficient; see Gahinet and Apkarian [1994] and Gahinet [1996] for a linear matrix inequality (LMI) approach to the $\mathcal { H } _ { \infty }$ problem. But the necessity should be suitably interpreted. For example, if one finds an $X _ { 1 } ~ > ~ 0$ and a $Y _ { 1 } > 0$ satisfying conditions (i) and (ii) but not condition (iii), this does not imply that there is no admissible $\mathcal { H } _ { \infty }$ controller since there might be other $X _ { 1 } > 0$ and $Y _ { 1 } > 0$ that satisfy all three conditions. For example, consider $\gamma = 1$ and

$$
G (s) = \left[ \begin{array}{c c c} - 1 & \left[ \begin{array}{c c} 1 & 0 \end{array} \right] & 1 \\ \hline \left[ \begin{array}{c} 1 \\ 0 \end{array} \right] & 0 & \left[ \begin{array}{c} 0 \\ 1 \end{array} \right] \\ 1 & \left[ \begin{array}{c c} 0 & 1 \end{array} \right] & 0 \end{array} \right].
$$

It is easy to check that $X _ { 1 } = Y _ { 1 } = 0 . 5$ satisfy (i) and (ii) but not (iii). Nevertheless, we shall show in the next section that $\gamma _ { \mathrm { o p t } } = 0 . 7 3 2 1$ and thus a suboptimal controller exists for $\gamma = 1$ . In fact, we can check that $1 < X _ { 1 } < 2 , 1 < Y _ { 1 } < 2$ also satisfy (i), (ii) and (iii). ✸

Example 14.1 Consider the feedback system shown in Figure 6.3 with

$$P = \frac {5 0 (s + 1 . 4)}{(s + 1) (s + 2)}, \quad W _ {e} = \frac {2}{s + 0 . 2}, \quad W _ {u} = \frac {s + 1}{s + 1 0}.$$

We shall design a controller so that the $\mathcal { H } _ { \infty }$ norm from $w = \left[ \begin{array} { c } { { d } } \\ { { d _ { i } } } \end{array} \right] \mathrm { t o } z = \left[ \begin{array} { c } { { e } } \\ { { \tilde { u } } } \end{array} \right]$ is minimized. Note that
