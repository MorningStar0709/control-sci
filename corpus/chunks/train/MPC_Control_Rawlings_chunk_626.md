# 5.5.3 Stability Analysis

We give here an informal discussion of the stability properties of the controller because offset-free MPC of constrained uncertain systems remains an area of current research. The controller described above is motivated by the following consideration: nominal MPC is able to handle “slow” uncertainties such as the drift of a target point if the value function $V _ { N } ^ { 0 } ( \cdot )$ is Lipschitz continuous.“Fast” uncertainties, however, are better handled by the tube controller that generates, using MPC, a suitable central trajectory that uses a “fast” ancillary controller to steer trajectories of the uncertain system toward the central trajectory. As shown above, the controller ensures that $x ( i ) \in \{ z ( i ) \} \oplus \mathbb { T }$ for all i; its success therefore depends on the ability of the controlled nominal system $z ^ { + } = A z + B _ { d } \hat { d } + B \bar { \kappa } _ { N } ( z , \hat { d } , \bar { r } ) , \nu = \bar { \kappa } _ { N } ( z , \hat { d } , \bar { r } )$ , to track the target $\bar { z } ( \hat { d } , \bar { r } )$ , which varies as $\hat { d }$ evolves.

Assuming that the standard stability assumptions are satisfied for the nominal optimal control problem $\bar { \mathbb { P } } _ { N } ( z , \hat { d } , \bar { r } )$ defined above, we have

$$V _ {N} ^ {0} (z, \hat {d}, \bar {r}) \geq c _ {1} | z - \bar {z} (\hat {d}, \bar {r}) | ^ {2}\Delta V _ {N} ^ {0} (z, \hat {d}, \bar {r}) \leq - c _ {1} | z - \bar {z} (\hat {d}, \bar {r}) | ^ {2}V _ {N} ^ {0} (z, \hat {d}, \bar {r}) \leq c _ {2} | z - \bar {z} (\hat {d}, \bar {r}) | ^ {2}$$

for all $z \in \mathcal { Z } _ { N } ( \hat { d } , \bar { r } )$ where, since $( \hat { d } , \bar { r } )$ is constant,

$$\Delta V _ {N} ^ {0} (z, \hat {d}, \bar {r}) := V _ {N} ^ {0} (A z + B _ {d} \hat {d} + B \bar {\kappa} _ {N} (z, \hat {d}, \bar {r}), \hat {d}, \bar {r}) - V _ {N} ^ {0} (z, \hat {d}, \bar {r})$$

and, for each $( \hat { d } , \bar { r } ) , \mathcal { Z } _ { N } ( \hat { d } , \bar { r } ) = \{ z \mid \mathcal { V } _ { N } ( z , \hat { d } , \bar { r } ) \neq \emptyset \}$ is the domain of $V _ { N } ^ { 0 } ( \cdot , \hat { d } , \bar { r } )$ .
