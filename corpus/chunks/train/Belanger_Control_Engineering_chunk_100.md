# DEFINITION

An LTI system is observable if the initial state $\mathbf{x}(0) = \mathbf{x}_{0}$ can be uniquely deduced from knowledge of the input $\mathbf{u}(t)$ and output $\mathbf{y}(t)$ for all t between 0 and any T > 0.

If $\mathbf{x}_0$ can be deduced, then so can $\mathbf{x}(t)$ , for $0 < t \leq T$ . To show this, we use additivity to write

$$\mathbf {x} (t) = e ^ {A t} \mathbf {x} _ {0} + \int_ {0} ^ {t} e ^ {A (t - \tau)} B \mathbf {u} (\tau) d \tau \tag {3.35}$$

Once $x_{0}$ is known, u can be inserted in Equation 3.35 to compute $\mathbf{x}(t)$ for all t between 0 and T. We conclude, then, that observability allows us to deduce from measurements the state of the system.

To study observability, it is necessary only to consider the zero-input solution. The complete output is

$$\mathbf {y} (t) = C e ^ {A t} \mathbf {x} _ {0} + \int_ {0} ^ {t} C e ^ {A (t - \tau)} B \mathbf {u} (\tau) d \tau + D \mathbf {u} (t).$$

Since $\mathbf{u}(t)$ is given, the zero-state part can be calculated and subtracted from $\mathbf{y}(t)$ , leaving only

$$\mathbf {y} _ {z i} (t) = C e ^ {A t} \mathbf {x} _ {0}$$

which is the only component that depends on $x_{0}$ . We shall dispense with the subscript zi in the remainder of this section.
