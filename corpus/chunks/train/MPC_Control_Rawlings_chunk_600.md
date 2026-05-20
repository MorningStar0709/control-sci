# 5.3.3 Controlling xˆ

Since $\tilde { { \boldsymbol { x } } } ( i ) \in \mathbb { \Sigma }$ for all i, we seek a method for controlling the observer state $\hat { x } ( i )$ in such a way that $x ( i ) = \hat { x } ( i ) + \widetilde { x } ( i )$ satisfies the state constraint $x ( i ) \in \mathbb { X }$ for all i. The state constraint $x ( i ) \in \mathbb { X }$ will be satisfied if we control the estimator state to satisfy $\hat { x } ( i ) \in \mathbb { X } \ominus \mathbb { Z }$ for all i. The estimator state satisfies (5.14) which can be written in the form

$$\hat {x} ^ {+} = A \hat {x} + B u + \delta \tag {5.15}$$

where the disturbance δ is defined by

$$\delta := L (y - \hat {y}) = L (C \tilde {x} + v)$$

and, therefore, always lies in the C-set ∆ defined by

$$\mathbb {A} := L (C \mathbb {Z} \oplus \mathbb {N})$$

The problem of controlling xˆ is, therefore, the same as that of controlling an uncertain system with known state. This problem was extensively discussed in Chapter 3. We can therefore use the approach of Chapter 3 here with $\hat { x }$ replacing x, δ replacing w, $\mathbb { X } \ominus \mathbb { Z }$ replacing X and $\mathbb { \Delta }$ replacing W.

To control (5.15) we use, as in Chapter 3, a combination of open-loop and feedback control, i.e., we choose the control u as follows

$$u = v + K e \quad e := \hat {x} - z \tag {5.16}$$

where z is the state of a nominal (deterministic) system that we shall shortly specify; v is the feedforward component of the control u, and Ke is the feedback component. The matrix K is chosen to satisfy $\rho ( A _ { K } ) \ < \ 1$ where $A _ { K } : = A + B K$ . The feedforward component v of the control u generates, as we show subsequently, a trajectory $\{ z ( i ) \}$ , which is the center of the tube in which the state estimator trajectory $\{ \hat { x } ( i ) \}$ lies. The feedback component Ke attempts to steer the trajectory $\{ \hat { x } ( i ) \}$ of the state estimate toward the center of the tube and thereby controls the cross section of the tube. The controller is $d y -$ namic since it incorporates the nominal dynamic system.

With this control, xˆ satisfies the following difference equation

$$\hat {x} ^ {+} = A \hat {x} + B v + B K e + \delta \quad \delta \in \mathbb {A} \tag {5.17}$$

The nominal (deterministic) system describing the evolution of $z$ is obtained by neglecting the disturbances BKe and $\delta$ in (5.17) yielding

$$z ^ {+} = A z + B v$$

The deviation $e = { \hat { x } } - z$ between the state $\hat { x }$ of the estimator and the state $z$ of the nominal system satisfies
