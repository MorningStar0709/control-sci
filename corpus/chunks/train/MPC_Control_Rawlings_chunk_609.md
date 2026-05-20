# 5.4.2 State Estimator

The state estimator is defined as in (5.11) in Section 5.3.2. The state estimate $\hat { x }$ satisfies the difference equation

$$\hat {x} ^ {+} = A \hat {x} + B u + \delta \quad \delta := L (y - C \hat {x})$$

and the state estimation error $\tilde { x }$ satisfies

$$\tilde {x} ^ {+} = A _ {L} \tilde {x} + \tilde {w} \quad \tilde {w} := w - L v$$
