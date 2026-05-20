# $\mathcal { H } _ { \infty }$ Performance

Although the $\mathcal { H } _ { 2 }$ norm (or $\mathcal { L } _ { 2 }$ norm) may be a meaningful performance measure and although LQG theory can give efficient design compromises under certain disturbance and plant assumptions, the $\mathcal { H } _ { 2 }$ norm suffers a major deficiency. This deficiency is due to the fact that the tradeoff between disturbance error reduction and sensor noise error reduction is not the only constraint on feedback design. The problem is that these performance tradeoffs are often overshadowed by a second limitation on high loop gains — namely, the requirement for tolerance to uncertainties. Though a controller may be designed using FDLTI models, the design must be implemented and operated with a real physical plant. The properties of physical systems (in particular, the ways in which they deviate from finite-dimensional linear models) put strict limitations on the frequency range over which the loop gains may be large.

A solution to this problem would be to put explicit constraints on the loop gain in the cost function. For instance, one may chose to minimize

$$\sup _ {\left\| \tilde {d} \right\| _ {2} \leq 1} \| e \| _ {2} = \| W _ {e} S _ {o} W _ {d} \| _ {\infty}$$

subject to some restrictions on the control energy or control bandwidth:

$$\sup _ {\left\| \tilde {d} \right\| _ {2} \leq 1} \| \tilde {u} \| _ {2} = \| W _ {u} K S _ {o} W _ {d} \| _ {\infty}$$

$\mathrm { O r } ,$ more frequently, one may introduce a parameter $\rho$ and a mixed criterion

$$
\sup _ {\left\| \tilde {d} \right\| _ {2} \leq 1} \left\{\left\| e \right\| _ {2} ^ {2} + \rho^ {2} \left\| \tilde {u} \right\| _ {2} ^ {2} \right\} = \left\| \left[ \begin{array}{c} W _ {e} S _ {o} W _ {d} \\ \rho W _ {u} K S _ {o} W _ {d} \end{array} \right] \right\| _ {\infty} ^ {2}
$$

Alternatively, if the system robust stability margin is the major concern, the weighted complementary sensitivity has to be limited. Thus the whole cost function may be

$$
\left\| \left[ \begin{array}{c} W _ {e} S _ {o} W _ {d} \\ \rho W _ {1} T _ {o} W _ {2} \end{array} \right] \right\| _ {\infty}
$$

where $W _ { 1 }$ and $W _ { 2 }$ are the frequency-dependent uncertainty scaling matrices. These design problems are usually called $\mathcal { H } _ { \infty }$ mixed-sensitivity problems. For a scalar system, an $\mathcal { H } _ { \infty }$ norm minimization problem can also be viewed as minimizing the maximum magnitude of the system’s steady-state response with respect to the worst-case sinusoidal inputs.
