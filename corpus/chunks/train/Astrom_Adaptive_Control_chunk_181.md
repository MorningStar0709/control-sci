# Feedforward Control

A nice feature of the direct self-tuner is that it is easy to include feedforward. Let v be a disturbance that can be measured. By estimating parameters in the model

$$y (t) = \frac {1}{A _ {o} A _ {m}} (R u (t) + S y (t) - U v (t)) \tag {3.31}$$

and using the control law

$$R u (t) = T u _ {c} (t) - S y (t) - U v (t)$$

we obtain a self-tuning controller that combines feedback and feedforward. The term $Tu_{c}$ in the control law can also be viewed as a feedforward term.

In Algorithm 3.3, polynomials R and S are estimated and the polynomial T is computed. This means that the different terms of the control law are treated differently. It is possible to obtain an algorithm in which all coefficients of the control law are estimated by treating $Tu_{c}$ as a feedforward term that is adapted. To do this, we first notice that the desired response is given by

$$y _ {m} (t) = \frac {B _ {m}}{A _ {m}} u _ {c} (t) = \frac {T}{A _ {o} A _ {m}} u _ {c} (t)$$

It follows from Eq. (3.27) that error $e(t) = y(t) - y_m(t)$ is given by

$$
\begin{array}{l} e (t) = \frac {1}{A _ {o} A _ {m}} \left(R u (t) + S y (t) - T u _ {c} (t)\right) \\ = R ^ {*} u _ {f} \left(t - d _ {0}\right) + S ^ {*} y _ {f} \left(t - d _ {0}\right) - T ^ {*} u _ {c f} \left(t - d _ {0}\right) \tag {3.32} \\ \end{array}
$$

where $u_{f}$ , $y_{f}$ , and $u_{cf}$ are the filtered signals defined by Eqs. (3.28) and

$$u _ {c f} (t) = \frac {1}{A _ {o} ^ {*} (q ^ {- 1}) A _ {m} ^ {*} (q ^ {- 1})} u _ {c} (t)$$

Furthermore, $\deg T = \deg R = \deg S = \deg (A_o A_m) - d_0$ and $\deg A_m - \deg B_m = d_0$ . An algorithm that is analogous to Algorithm 3.3, in which the parameters of the feedforward polynomial $T$ are also estimated is now easily obtained by estimating the parameters in Eq. (3.32).
