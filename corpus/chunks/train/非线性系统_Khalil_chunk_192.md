我们不能应用引理6.1, 因为对于任意 $s, \det [G(s) + G^{\mathrm{T}}(-s)] \equiv 0$ 。然而, 通过验证定义6.4的条件可知 $G(s)$ 是严格正实的。注意, 当 $\varepsilon < 1$ 时, $G(s - \varepsilon)$ 各元素的极点都满足 $\operatorname{Re}[s] < 0$ , 且

$$
G (j \omega - \varepsilon) + G ^ {\mathrm{T}} (- j \omega - \varepsilon) = \frac {2 (1 - \varepsilon)}{\omega^ {2} + (1 - \varepsilon) ^ {2}} \left[ \begin{array}{l l} 1 & 1 \\ 1 & 1 \end{array} \right]
$$

对于所有 $\omega \in R$ 都是半正定的。同样， $2 \times 2$ 传递函数矩阵

$$
G (s) = \frac {1}{s + 1} \left[ \begin{array}{c c} s + 1 & 1 \\ - 1 & 2 s + 1 \end{array} \right]
$$

是严格正实的,但此时 $\det\left[G(s)+G^{\mathrm{T}}(-s)\right]$ 不恒为零。应用引理6.1也可得出相同的结论,因为 $G(\infty)+G^{\mathrm{T}}(\infty)$ 是正定的,且

$$
G (j \omega) + G ^ {\mathrm{T}} (- j \omega) = \frac {2}{\omega^ {2} + 1} \left[ \begin{array}{c c} \omega^ {2} + 1 & - j \omega \\ j \omega & 2 \omega^ {2} + 1 \end{array} \right]
$$

对于所有 $\omega \in R$ 是正定的。最后，对 $2\times 2$ 传递函数矩阵

$$
G (s) = \left[ \begin{array}{l l} \frac {s + 2}{s + 1} & \frac {1}{s + 2} \\ \frac {- 1}{s + 2} & \frac {2}{s + 1} \end{array} \right]
$$

有 $G(\infty) + G^{\mathrm{T}}(\infty) = \left[ \begin{array}{ll}2 & 0\\ 0 & 0 \end{array} \right]$

可以验证,对于所有 $\omega \in R$

$$
G (j \omega) + G ^ {\mathrm{T}} (- j \omega) = \left[ \begin{array}{l l} \frac {2 (2 + \omega^ {2})}{1 + \omega^ {2}} & \frac {- 2 j \omega}{4 + \omega^ {2}} \\ \frac {2 j \omega}{4 + \omega^ {2}} & \frac {4}{1 + \omega^ {2}} \end{array} \right]
$$

是正定的。取 $M^{\mathrm{T}} = [0\quad 1]$ ，可以验证

$$\lim _ {\omega \rightarrow \infty} \omega^ {2} M ^ {\mathrm{T}} [ G (j \omega) + G ^ {\mathrm{T}} (- j \omega) ] M = 4$$

因而，由引理6.1可知 $G(s)$ 是严格正实的。

正实传递函数的无源性性质可用下面两个引理给予证明,它们分别是正实引理和Kalman-Yakubovich-Popov引理。这两个引理给出了正实传递函数和严格正实传递函数的代数特性。

引理6.2（正实引理）设 $G(s) = C(sI - A)^{-1}B + D$ 是 $p \times p$ 传递函数矩阵，其中 $(A, B)$ 是可控制的， $(A, C)$ 是可观测的。当且仅当存在矩阵 $P = P^{\mathrm{T}} > 0, L$ 和 $W$ 满足

$$P A + A ^ {\mathrm{T}} P = - L ^ {\mathrm{T}} L \tag {6.11}P B = C ^ {\mathrm{T}} - L ^ {\mathrm{T}} W \tag {6.12}W ^ {\mathrm{T}} W = D + D ^ {\mathrm{T}} \tag {6.13}$$

时， $G(s)$ 是正实的。

证明:参见附录 C.12。

引理6.3（Kalman-Yakubovich-Popov引理）设 $G(s) = C(sI - A)^{-1}B + D$ 是 $p\times p$ 传递函数矩阵，其中 $(A,B)$ 是可控制的， $(A,C)$ 是可观测的。当且仅当存在矩阵 $P = P^{\mathrm{T}} > 0,L,W$ 和

正常数 $\varepsilon$ ，满足 $PA + A^{T}P = -L^{T}L - \varepsilon P$ (6.14)

$$P B = C ^ {\mathrm{T}} - L ^ {\mathrm{T}} W \tag {6.15}W ^ {\mathrm{T}} W = D + D ^ {\mathrm{T}} \tag {6.16}$$

时， $G(s)$ 是严格正实的。
