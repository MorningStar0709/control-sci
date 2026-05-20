# 6.2.4 Cooperative Game

In the cooperative game, the two players share a common objective, which can be considered to be the overall plant objective

$$V (x _ {1} (0), x _ {2} (0), \mathbf {u} _ {1}, \mathbf {u} _ {2}) = \rho_ {1} V _ {1} (x _ {1} (0), \mathbf {u} _ {1}, \mathbf {u} _ {2}) + \rho_ {2} V _ {2} (x _ {2} (0), \mathbf {u} _ {2}, \mathbf {u} _ {1})$$

in which the parameters $\rho _ { 1 } , \rho _ { 2 }$ are used to specify the relative weights of the two subsystems in the overall plant objective. In the cooperative problem, each player keeps track of how his input affects the other player’s output as well as his own output. We can implement this cooperative game in several ways. The implementation leading to the simplest notation is to combine $x _ { 1 }$ and $x _ { 2 }$ into a single model

$$
\left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right] ^ {+} = \left[ \begin{array}{c c} A _ {1} & 0 \\ 0 & A _ {2} \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{l} \overline {{B}} _ {1 1} \\ \overline {{B}} _ {2 1} \end{array} \right] u _ {1} + \left[ \begin{array}{l} \overline {{B}} _ {1 2} \\ \overline {{B}} _ {2 2} \end{array} \right] u _ {2}
$$

and then express player $\mathrm { o n e ^ { \prime } s }$ stage cost as

$$
\ell_ {1} (x _ {1}, x _ {2}, u _ {1}) = \frac {1}{2} \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] ^ {\prime} \left[ \begin{array}{c c} \rho_ {1} Q _ {1} & 0 \\ 0 & \rho_ {2} Q _ {2} \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] + \frac {1}{2} u _ {1} ^ {\prime} (\rho_ {1} R _ {1}) u _ {1} + \text { const. }

V _ {1 f} (x _ {1}, x _ {2}) = \frac {1}{2} \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] ^ {\prime} \left[ \begin{array}{c c} \rho_ {1} P _ {1 f} & 0 \\ 0 & \rho_ {2} P _ {2 f} \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right]
$$

Notice that $u _ { 2 }$ does not appear because the contribution of $u _ { 2 }$ to the stage cost cannot be affected by player one, and can therefore be neglected. The cost function is then expressed as

$$V (x _ {1} (0), x _ {2} (0), \mathbf {u} _ {1}, \mathbf {u} _ {2}) = \sum_ {k = 0} ^ {N - 1} \ell_ {1} (x _ {1} (k), x _ {2} (k), u _ {1} (k)) + V _ {1 f} (x _ {1} (N), x _ {2} (N))$$

Player one’s optimal control problem is
