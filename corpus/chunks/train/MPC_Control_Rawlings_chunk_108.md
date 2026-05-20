1. The output target is modified in (1.46a) to account for the effect of the disturbance on the measured output $( y _ { \mathrm { s p } }  y _ { \mathrm { s p } } - C _ { d } \hat { d } _ { s } )$ .   
2. The output constraint in (1.46d) is similarly modified $( f \to f -$ $F C _ { d } \hat { d } _ { s } )$ .   
3. The system steady-state relation in (1.46b) is modified to account for the effect of the disturbance on the state evolution $( 0  B _ { d } \hat { d } _ { s } )$ .   
4. The controlled variable target in (1.46b) is modified to account for the effect of the disturbance on the controlled variable $( r _ { \mathrm { s p } } $ $r _ { \mathrm { s p } } - H C _ { d } \hat { d } _ { s } )$ .

Given the steady-state target, the same dynamic regulation problem as presented in the tracking section, Section 1.5, is used for the regulator. In other words, the regulator is based on the deterministic system (A, B) in which the current state is $\hat { x } ( k ) - x _ { s }$ and the goal is to take the system to the origin.

The following lemma summarizes the offset-free control property of the combined control system.

Lemma 1.10 (Offset-free control). Consider a system controlled by the MPC algorithm as shown in Figure 1.5. The target problem (1.46) is assumed feasible. Augment the system model with a number of integrating disturbances equal to the number of measurements $( n _ { d } = p )$ ; choose any $B _ { d } \in \mathbb { R } ^ { n \times p } , C _ { d } \in \mathbb { R } ^ { p \times p }$ such that

$$
\operatorname{rank} \left[ \begin{array}{c c} I - A & - B _ {d} \\ C & C _ {d} \end{array} \right] = n + p
$$

If the plant output $y ( k )$ goes to steady state $y _ { s }$ , the closed-loop system is stable, and constraints are not active at steady state, then there is zero offset in the controlled variables, that is

$$H y _ {s} = r _ {\mathrm{sp}}$$

The proof of this lemma is given in Pannocchia and Rawlings (2003). It may seem surprising that the number of integrating disturbances must be equal to the number of measurements used for feedback rather than the number of controlled variables to guarantee offset-free control. To gain insight into the reason, consider the disturbance part (bottom half) of the Kalman filter equations shown in Figure 1.5

$$
\hat {d} ^ {+} = \hat {d} + L _ {d} \left(y - \left[ \begin{array}{c c} C & C _ {d} \end{array} \right] \left[ \begin{array}{c} \hat {x} \\ \hat {d} \end{array} \right]\right)
$$

Because of the integrator, the disturbance estimate cannot converge until
