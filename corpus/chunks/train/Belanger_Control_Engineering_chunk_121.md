# DEFINITION

An LTI system is controllable if, for every $x_{1}$ and every T > 0, there exists an input function $\mathbf{u}(t), 0 < t \leq T$ , such that the system state is taken from 0 at t = 0 to $x_{1}$ at t = T.

The definition may appear restrictive due to the special choice of 0 as initial state. That is not the case: if the system satisfies the definition, the state can be taken from any initial state to any other state in arbitrary nonzero time. This follows from the fact that

$$\mathbf {x} (t _ {0} + T) = e ^ {A T} \mathbf {x} (t _ {0}) + \int_ {t _ {0}} ^ {t _ {0} + T} e ^ {A (t _ {0} + T - \tau)} B \mathbf {u} (\tau) d \tau . \tag {3.46}$$

With $\tau' = \tau - t_0$ , the integral becomes

$$\int_ {t _ {0}} ^ {t _ {0} + T} e ^ {A (t _ {0} + T - \tau)} B \mathbf {u} (\tau) d \tau = \int_ {0} ^ {T} e ^ {A (T - \tau^ {\prime})} B \mathbf {u} (t _ {0} + \tau^ {\prime}) d \tau^ {\prime}.$$

If we let $\mathbf{v}(\tau') = \mathbf{u}(t_0 + \tau')$ , the integral is just the zero-state response at t = T to an input $\mathbf{v}(t')$ , $0 < t' \leq T$ . If the system is controllable, $\mathbf{u}(t')$ can be chosen to give the integral any desired value; this implies that $\mathbf{x}(t_0 + T)$ in Equation 3.46 can also have any desired value.

What this means is that, to study controllability, we need only focus on the zero-state response; recall that only the zero-input response was necessary in the study of observability.
