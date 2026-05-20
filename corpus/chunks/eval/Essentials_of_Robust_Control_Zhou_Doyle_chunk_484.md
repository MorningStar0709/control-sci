for some d $\in \mathcal { D } _ { \mathrm { c o n v e x } }$ if and only if there exists a $d = ( d _ { 0 } , d _ { 1 } , \dots , d _ { l - 1 } ) \in \pi _ { \ell } { \cal D } _ { \mathrm { c o n v e x } }$ such that

$$\overline {{\sigma}} \left[ (T _ {\hat {y}} - T _ {D} T _ {d}) (T _ {\hat {u}} ^ {*} T _ {\hat {u}}) ^ {- 1 / 2} \right] \leq 1$$

where

$$
T _ {D} := \left[ \begin{array}{c c c c} D _ {0} & 0 & \dots & 0 \\ D _ {1} & D _ {0} & \ddots & 0 \\ \vdots & \vdots & \ddots & 0 \\ D _ {l - 1} & D _ {l - 2} & \dots & D _ {0} \end{array} \right].
$$

Proof. Note that the system input-output equation can be written as

$$(y - P u) - D d = \Delta (W u).$$

Since $P , W , D ,$ , and $\Delta$ are causal, linear, and time invariant, we have $\pi _ { \ell } D d = \pi _ { \ell } D \pi _ { \ell } d ,$ $\pi _ { \ell } ( y - P u ) = y _ { \mathrm { e x p t } } - \pi _ { \ell } P \pi _ { \ell } u = y _ { \mathrm { e x p t } } - \pi _ { \ell } P u _ { \mathrm { e x p t } }$ and $\pi _ { \ell } W u = \pi _ { \ell } W \pi _ { \ell } u = \pi _ { \ell } W u _ { \mathrm { e x p t } }$ . Denote

$$\hat {d} = (\hat {d} _ {0}, \hat {d} _ {1}, \dots , \hat {d} _ {\ell - 1}) = \pi_ {\ell} (D d).$$

Then it is easy to show that

$$
\left[ \begin{array}{c} \hat {d} _ {0} \\ \hat {d} _ {1} \\ \vdots \\ \hat {d} _ {\ell - 1} \end{array} \right] = T _ {D} \left[ \begin{array}{c} d _ {0} \\ d _ {1} \\ \vdots \\ d _ {\ell - 1} \end{array} \right]
$$

and $T _ { \hat { d } } = T _ { D } T _ { d }$ . Now note that

$$T _ {\pi_ {\ell} (y - P u - D d)} = T _ {\pi_ {\ell} (y - P u)} - T _ {\pi_ {\ell} (D d)} = T _ {\hat {y}} - T _ {D} T _ {d}, \quad T _ {\pi_ {\ell} W u} = T _ {\hat {u}}$$

and $\pi _ { \ell } \Delta W u = \pi _ { \ell } \Delta \pi _ { \ell } ( W u )$ since $\Delta$ is causal. Applying Theorem 18.1, there exists a $\Delta \in \mathcal { H } _ { \infty } , \| \Delta \| _ { \infty } \leq 1$ such that

$$\pi_ {\ell} \left[ (y - P u) - D d \right] = \pi_ {\ell} \Delta (W u) = \pi_ {\ell} \Delta \pi_ {\ell} (W u)$$

if and only if

$$(T _ {\hat {y}} - T _ {D} T _ {d}) ^ {*} (T _ {\hat {y}} - T _ {D} T _ {d}) \leq T _ {\hat {u}} ^ {*} T _ {\hat {u}}$$

which is equivalent to

$$\overline {{\sigma}} \left[ (T _ {\hat {y}} - T _ {D} T _ {d}) (T _ {\hat {u}} ^ {*} T _ {\hat {u}}) ^ {- \frac {1}{2}} \right] \leq 1.$$

Note that $T _ { \hat { u } }$ is of full column rank since $W ( \infty )$ is of full column rank and $u _ { 0 } \neq 0 ,$ which implies $\hat { u } _ { 0 } \neq 0$ . ✷

Note that

$$\inf _ {d \in \mathcal {D} _ {\mathrm{convex}}} \overline {{\sigma}} \left[ (T _ {\hat {y}} - T _ {D} T _ {d}) (T _ {\hat {u}} ^ {*} T _ {\hat {u}}) ^ {- \frac {1}{2}} \right] \leq 1$$

is a convex problem and can be checked numerically.
