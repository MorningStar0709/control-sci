# Exercise 1.1: State space form for chemical reaction model

Consider the following chemical reaction kinetics for a two-step series reaction

$$\mathrm{A} \stackrel {k _ {1}} {\longrightarrow} \mathrm{B} \quad \mathrm{B} \stackrel {k _ {2}} {\longrightarrow} \mathrm{C}$$

We wish to follow the reaction in a constant volume, well-mixed, batch reactor. As taught in the undergraduate chemical engineering curriculum, we proceed by writing material balances for the three species giving

$$\frac {d c _ {A}}{d t} = - r _ {1} \quad \frac {d c _ {B}}{d t} = r _ {1} - r _ {2} \quad \frac {d c _ {C}}{d t} = r _ {2}$$

in which $c _ { j }$ is the concentration of species j, and $r _ { 1 }$ and $r _ { 2 }$ are the rates (mol/(time·vol)) at which the two reactions occur. We then assume some rate law for the reaction kinetics, such as

$$r _ {1} = k _ {1} c _ {A} \quad r _ {2} = k _ {2} c _ {B}$$

We substitute the rate laws into the material balances and specify the starting concentrations to produce three differential equations for the three species concentrations.

(a) Write the linear state space model for the deterministic series chemical reaction model. Assume we can measure the component A concentration. What are x, y, A, B, C, and D for this model?

(b) Simulate this model with initial conditions and parameters given by

$$c _ {A 0} = 1 \quad c _ {B 0} = c _ {C 0} = 0 \quad k _ {1} = 2 \quad k _ {2} = 1$$
