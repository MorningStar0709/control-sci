Now suppose $\begin{array} { r } { \operatorname* { s u p } _ { s \in \mathbb { C } _ { + } } \mu _ { \Delta } ( G ( s ) ) > \beta ; } \end{array}$ then by the definition of $\mu ,$ there is an $s _ { o } \in$ $\overline { { \mathbb { C } } } _ { + } \cup \{ \infty \}$ and a complex structured ∆ such that $\overline { { \sigma } } ( \Delta ) < 1 / \beta$ and det $( I - G ( s _ { o } ) \Delta ) = 0$ . This implies that there is a $0 \leq \hat { \omega } \leq \infty$ and $0 < \alpha \leq 1$ such that det $( I - G ( j \hat { \omega } ) \alpha \Delta ) =$ 0. This, in turn, implies that $\mu _ { \Delta } ( G ( j \hat { \omega } ) ) > \beta$ since $\overline { { \sigma } } ( \alpha \Delta ) < 1 / \beta$ . In other words, $\begin{array} { r } { \operatorname* { s u p } _ { s \in \mathbb { C } _ { + } } \mu _ { \Delta } ( G ( s ) ) \leq \operatorname* { s u p } _ { \omega } \mu _ { \Delta } ( G ( j \omega ) ) } \end{array}$ ). The proof is complete.

$( \Longrightarrow )$ Suppose supω R $\mu _ { \Delta } ( G ( j \omega ) ) > \beta .$ . Then there is a $0 < \omega _ { o } < \infty$ such that $\mu _ { \pmb { \Delta } } ( G ( j \omega _ { o } ) ) > \beta .$ By Remark 10.1, there is a complex $\Delta _ { c } \in \Delta$ that each full block has rank 1 and $\overline { { \sigma } } ( \Delta _ { c } ) < 1 / \beta$ such that $I - G ( j \omega _ { o } ) \Delta _ { c }$ is singular. Next, using the same construction used in the proof of the small gain theorem (Theorem 8.1), one can find a rational $\Delta ( s )$ such that $\left\| \Delta ( s ) \right\| _ { \infty } = \overline { { \sigma } } ( \Delta _ { c } ) < 1 / \beta , \Delta ( j \omega _ { o } ) = \Delta _ { c } .$ , and $\Delta ( s )$ destabilizes the system. ✷

Hence, the peak value on the $\mu$ plot of the frequency response determines the size of perturbations that the loop is robustly stable against.

Remark 10.4 The internal stability with a closed ball of uncertainties is more complicated. The following example is shown in Tits and Fan [1995]. Consider

$$
G (s) = \frac {1}{s + 1} \left[ \begin{array}{l l} 0 & - 1 \\ 1 & 0 \end{array} \right]
$$

and $\Delta = \delta ( s ) I _ { 2 }$ . Then

$$\sup _ {\omega \in \mathbb {R}} \mu_ {\boldsymbol {\Delta}} (G (j \omega)) = \sup _ {\omega \in \mathbb {R}} \frac {1}{| j \omega + 1 |} = \mu_ {\boldsymbol {\Delta}} (G (j 0)) = 1.$$

On the other hand, $\mu _ { \Delta } ( G ( s ) ) < 1$ for all $s \neq 0 , s \in \overline { { \mathbb { C } } } _ { + }$ , and the only matrices in the form of $\Gamma = \gamma I _ { 2 }$ with $| \gamma | \leq 1$ for which

$$\det (I - G (0) \Gamma) = 0$$
