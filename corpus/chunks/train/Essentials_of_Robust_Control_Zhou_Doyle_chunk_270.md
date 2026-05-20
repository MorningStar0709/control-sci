Let $A \in \mathbb { C } ^ { n \times n } , B \in \mathbb { C } ^ { n \times m } , C \in \mathbb { C } ^ { m \times n }$ , and $D \in \mathbb { C } ^ { m \times m }$ be given, and interpret them as the state-space model of a discrete time system

$$x _ {k + 1} = A x _ {k} + B u _ {k}y _ {k} \quad = C x _ {k} + D u _ {k}.$$

Let $M \in \mathbb { C } ^ { ( n + m ) \times ( n + m ) }$ be the block state-space matrix of the system

$$
M = \left[ \begin{array}{c c} A & B \\ C & D \end{array} \right].
$$

Applying the theorem with these data gives that the following are equivalent:

• The spectral radius of A satisfies $\rho \left( A \right) < 1$ , and

$$
\max_{\substack{\delta_{1}\in \mathbb{C}\\ |\delta_{1}|\leq 1}}\overline{\sigma}\left(D + C\delta_{1}\left(I - A\delta_{1}\right)^{-1}B\right) <   1. \tag{10.17}
$$

• The maximum singular value of D satisfies $\overline { { \sigma } } ( D ) < 1$ , and

$$
\max _ {\substack {\Delta_ {2} \in \mathbb {C} ^ {m \times m} \\ \overline {\sigma} (\Delta_ {2}) \leq 1}} \rho (A + B \Delta_ {2} (I - D \Delta_ {2}) ^ {- 1} C) <   1. \tag{10.18}
$$

• The structured singular value of M satisfies

$$\mu_ {\Delta} (M) < 1. \tag {10.19}$$

The first condition is recognized by two things: The system is stable, and the $| | \cdot | | _ { \infty }$ norm on the transfer function from u to y is less than 1 (by replacing $\delta _ { 1 }$ with $\textstyle { \frac { 1 } { z } } \int$ :

$$
\| G\|_{\infty}:= \max_{\substack{z\in \mathbb{C}\\ |z|\geq 1}}\overline{\sigma}\left(D + C\left(zI - A\right)^{-1}B\right) = \max_{\substack{\delta_{1}\in \mathbb{C}\\ |\delta_{1}|\leq 1}}\overline{\sigma}\left(D + C\delta_{1}\left(I - A\delta_{1}\right)^{-1}B\right).
$$

The second condition implies that $\left( I - D \Delta _ { 2 } \right) ^ { - 1 }$ is well defined for all $\overline { { \sigma } } ( \Delta _ { 2 } ) \leq 1$ and that a robust stability result holds for the uncertain difference equation

$$x _ {k + 1} = \left(A + B \Delta_ {2} (I - D \Delta_ {2}) ^ {- 1} C\right) x _ {k}$$

where $\Delta _ { 2 }$ is any element in $\mathbb { C } ^ { m \times m }$ with $\overline { { \sigma } } ( \Delta _ { 2 } ) \leq 1$ , but otherwise unknown.
