# EXAMPLE 11.9 Obtaining integral action automatically

Consider the simple direct moving-average self-tuning controller described in Chapter 4, which is based on least-squares estimation and minimum-variance control. The estimation is based on the model

$$y (t + d) = R ^ {*} (q ^ {- 1}) u (t) + S ^ {*} (q ^ {- 1}) y (t)$$

and the regulator is

$$u (t) = - \frac {S ^ {*}}{R ^ {*}} y (t)$$

The conditions for a stationary solution are that

$$
\begin{array}{l} \hat {r} _ {y} (\tau) = \lim _ {N \rightarrow \infty} \frac {1}{N} \sum_ {k = 1} ^ {N} y (k + \tau) y (k) = 0 \quad \tau = d, \dots , d + l \\ \hat {r} _ {y u} (\tau) = \lim _ {N \rightarrow \infty} \frac {1}{N} \sum_ {k = 1} ^ {N} y (k + \tau) u (k) = 0 \quad \tau = d, \dots , d + k \\ \end{array}
$$

where k and l are the degrees of the $R^{*}$ and $S^{*}$ polynomials, respectively. These conditions are not satisfied unless the mean value of y is zero. When there is an offset, the parameter estimates will get values such that $R^{*}(1) = 0$ , that is, there is an integrator in the controller. However, the convergence to the integrator may be slow.

A second way to explicitly eliminate steady-state errors is to base an adaptive controller on estimation of parameters in the model

$$A (q) y (t) = B (q) u (t) + v$$

where v is a constant that is estimated. The control design should also be modified by introducing a feedforward from the estimated disturbance. This approach has the drawback that an extra parameter has to be estimated. Furthermore, it is necessary to have different forgetting factors on the bias estimate and the other estimates; otherwise, the convergence to a new level will be very slow. Finally, if the bias is estimated in this way, it is not possible to use the self-tuner as a tuner, since there will be no reset when the estimation is switched off. This is a simple example that shows the drawbacks of mixing the functions of the feedback loop and the adaptation loop. A much better way is to design a controller with integral action, for example, by using the methods discussed in Section 3.6. A data filter of band-pass character should also be used so that the disturbance v does not influence estimation too much. We will also show how a similar approach can be used for a direct self-tuner.
