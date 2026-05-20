# $\mathcal { H } _ { 2 }$ Performance

Assume, for example, that the disturbance $\tilde { d }$ can be approximately modeled as an impulse with random input direction; that is,

$$\tilde {d} (t) = \eta \delta (t)$$

and

$$E (\eta \eta^ {*}) = I$$

where E denotes the expectation. We may choose to minimize the expected energy of the error e due to the disturbance $\tilde { d } \colon$

$$E \left\{\| e \| _ {2} ^ {2} \right\} = E \left\{\int_ {0} ^ {\infty} \| e \| ^ {2} d t \right\} = \| W _ {e} S _ {o} W _ {d} \| _ {2} ^ {2}$$

In general, a controller minimizing only the above criterion can lead to a very large control signal u that could cause saturation of the actuators as well as many other undesirable problems. Hence, for a realistic controller design, it is necessary to include the control signal u in the cost function. Thus, our design criterion would usually be something like this:

$$
E \left\{\| e \| _ {2} ^ {2} + \rho^ {2} \| \tilde {u} \| _ {2} ^ {2} \right\} = \left\| \left[ \begin{array}{c} W _ {e} S _ {o} W _ {d} \\ \rho W _ {u} K S _ {o} W _ {d} \end{array} \right] \right\| _ {2} ^ {2}
$$

with some appropriate choice of weighting matrix $W _ { u }$ and scalar $\rho .$ The parameter $\rho$ clearly defines the tradeoff we discussed earlier between good disturbance rejection at the output and control effort (or disturbance and sensor noise rejection at the actuators). Note that $\rho$ can be set to $\rho = 1$ by an appropriate choice of $W _ { u }$ . This problem can be viewed as minimizing the energy consumed by the system in order to reject the disturbance d.
