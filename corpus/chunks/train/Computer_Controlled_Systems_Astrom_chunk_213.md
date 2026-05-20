3.16 Determine the values of K > 0 for which the system

$$y (k) = K \frac {4 q ^ {- 1} + q ^ {- 2}}{1 + q ^ {- 1} + 0 . 1 6 q ^ {- 2}} u (k)$$

is stable under simple feedback.

3.17 Determine a coordinate transformation $z = Tx$ that transfers the system

$$
\begin{array}{l} x (k + 1) = \left( \begin{array}{l l} 1 & 2 \\ 1 & 2 \end{array} \right) x (k) + \left( \begin{array}{l} 3 \\ 4 \end{array} \right) u (k) \\ y (k) = \left( \begin{array}{l l} 5 & 6 \end{array} \right) x (k) \\ \end{array}
$$

to controllable canonical form and to observable canonical form.

3.18 Assume that the continuous-time system (CT)

$$
\begin{array}{l} \frac {d x}{d t} = A x + B u \\ y = C x \\ \end{array}
$$

is sampled and gives the discrete-time system (DT)

$$x (k h + h) = \Phi x (k h) + \Gamma u (k h)y (k h) = C x (k h)$$

Consider the following statements:

(a) CT stable $\Rightarrow$ DT stable   
(b) CT unstable $\Rightarrow$ DT unstable   
(c) CT stable inverse $\Rightarrow$ DT stable inverse   
(d) CT unstable inverse $\Rightarrow$ DT unstable inverse   
(e) CT controllable $\Rightarrow$ DT controllable   
(f) CT observable $\Rightarrow$ DT observable   
(g) CT pole excess $r \Rightarrow DT$ pole excess r

Which statements are true for the following cases:

(i) All sampling intervals $h > 0$ .   
(ii) All $h > 0$ except for isolated values.   
(iii) Neither (i) nor (ii).

3.19 Consider the system

$$
x (k + 1) = \left( \begin{array}{c c c} 0 & - 3 & 2 \\ 3 & - 1 2 & 7 \\ 6 & - 2 1 & 1 2 \end{array} \right) x (k) + \left( \begin{array}{l} 0 \\ 1 \\ 2 \end{array} \right) u (k)
$$

Determine whether

(a) the system is reachable.   
(b) the system is controllable.

3.20 Given the system

$$(q ^ {2} + 0. 4 q) y (k) = u (k)$$

(a) For which values of K in the proportional controller

$$u (k) = K \left(u _ {c} (k) - y (k)\right)$$

is the closed-loop system stable?

(b) Determine the stationary error $u_{c} - y$ when $u_{c}$ is a step and when K = 0.5 in the controller in (a).

3.21 Assume that the system

$$y (k) - 1. 2 y (k - 1) + 0. 5 y (k - 2) = 0. 4 u (k - 1) + 0. 8 u (k - 2)$$

is controlled by

$$u (k) = - K y (k)$$

(a) Determine for which values of $K$ the closed-loop system is stable.   
(b) Assume that there is a computational delay in the controller, that is,

$$u (k) = - K y (k - 1)$$

For which values of K is the closed-loop system now stable?
