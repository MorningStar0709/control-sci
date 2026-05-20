# 3.1 Introduction

example those policies for which each control law $\mu _ { i } ( \cdot )$ is continuous. Then, $\phi ( i ; \boldsymbol { x } , \pmb { \mu } , \mathbf { w } )$ denotes the solution at time $i \in \{ 0 , 1 , 2 , 3 \}$ of the following difference equation

$$x (i + 1) = x (i) + \mu_ {i} (x (i)) + w (i) \quad x (0) = x$$

An open-loop control sequence $\mathbf { u } = \{ u ( 0 ) , u ( 1 ) , u ( 2 ) \}$ is then merely a degenerate policy $\pmb { \mu } = \{ \mu _ { 0 } ( \cdot ) , \mu _ { 1 } ( \cdot ) , \mu _ { 2 } ( \cdot ) \}$ } where each control law $\mu _ { i } ( \cdot )$ satisfies

$$\mu_ {i} (x) = u (i)$$

for all $x \in \mathbb { R }$ and all $i \in \{ 0 , 1 , 2 \}$ . The cost $V _ { 3 } ( \cdot )$ may now be defined

$$V _ {3} (x, \boldsymbol {\mu}, \mathbf {w}) := (1 / 2) \sum_ {i = 0} ^ {2} [ (x (i) ^ {2} + u (i) ^ {2}) ] + (1 / 2) x (3) ^ {2}$$

where, now, $x ( i ) = \phi ( i ; x , \pmb { \mu } , \mathbf { w } )$ and $u ( i ) = \mu _ { i } ( x ( i ) )$ . Since the disturbance is unpredictable, the value of w is not known at time 0, so the optimal control problem must “eliminate” it in some meaningful way so that the solution $\pmb { \mu } ^ { 0 } ( x )$ does not depend on w. To eliminate w, the optimal control problem $\mathbb { P } _ { 3 } ^ { * } \left( x \right)$ is defined by

$$\mathbb {P} _ {3} ^ {*} (x): \qquad V _ {3} ^ {0} (x) := \inf _ {\boldsymbol {\mu} \in \mathcal {M}} J _ {3} (x, \boldsymbol {\mu})$$

in which the cost $J _ { 3 } ( \cdot )$ is defined in such a way that it does not depend on w; inf is used rather than min in this definition since the minimum may not exist. The most popular choice for $J _ { 3 } ( \cdot )$ in the MPC literature is

$$J _ {3} (x, \boldsymbol {\mu}) := \max _ {\mathbf {w} \in \mathcal {W}} V _ {3} (x, \boldsymbol {\mu}, \mathbf {w})$$

in which the disturbance w is assumed to lie in W a bounded class of admissible disturbance sequences. Alternatively, if the disturbance sequence is random, the cost $J _ { 3 } ( \cdot )$ may be chosen to be

$$J _ {3} (x, \boldsymbol {\mu}) := \mathcal {E} V _ {3} (x, \boldsymbol {\mu}, \mathbf {w})$$

in which E denotes “expectation” or average, over random disturbance sequences. For our purpose here, we adopt the simple cost

$$J _ {3} (x, \boldsymbol {\mu}) := V _ {3} (x, \boldsymbol {\mu}, \mathbf {0})$$
