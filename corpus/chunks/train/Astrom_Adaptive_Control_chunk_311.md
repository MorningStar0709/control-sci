# The Operator View of Dynamical Systems

Signals are elements of a normed space X, which we call the signal space. A system S is considered as an operator $S: X \rightarrow X$ . For simplicity we consider systems with one input and one output and the signals are real functions from R to R. Several choices of norms are considered, for example, the $L_{2}$ norm

$$\| u \| = \left(\int_ {- \infty} ^ {\infty} u ^ {2} (t) d t\right) ^ {\frac {1}{2}}$$

or the sup norm

$$\left| \left| u \right| \right| = \sup _ {0 \leq t \leq \infty} | u (t) |$$

A drawback of using $L_{2}$ is that it must be assumed a priori that all signals go to zero as $t \to \infty$ . The notion of extended space is introduced to avoid this assumption. This is introduced as follows.

Let $Y$ be the space of real-valued functions on $[0, \infty)$ . Let $x$ be an element of $Y$ . The truncation of $x$ at $T > 0$ is defined as

$$
x _ {T} (t) = \left\{ \begin{array}{l l} x (t) & 0 \leq t \leq T \\ 0 & t > T \end{array} \right.
$$
