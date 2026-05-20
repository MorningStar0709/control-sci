# Extensions of the Loss Function

An approach that is similar to constrained minimization is to extend the loss function to prevent the shortsightedness of the cautious controller. One obvious way is to try to solve the two-step minimization problem. The derivation in Section 7.4 shows that it is not possible to get an analytic solution when N = 2 in Eq. (7.8).

Another approach is to extend the loss function with a function of $P(t+2)$ , which will reward good parameter estimates. The following loss function can be used:

$$\min _ {u (t)} E \left\{\left(y (t + 1) - u _ {c} (t + 1)\right) ^ {2} + \rho f (P (t + 2)) \mid \mathcal {Y} _ {t} \right\} \tag {7.19}$$

where $\rho$ is a fixed parameter. Since the crucial parameter is $b_{0}$ , we can use

$$f (P (t + 2)) = p _ {b _ {0}} (t + 2)$$

or

$$f (P (t + 2)) = R _ {2} \frac {p _ {b _ {0}} (t + 2)}{p _ {b _ {0}} (t + 1)} \tag {7.20}$$

This leads to a loss function with two local minima; it is necessary to make a numerical search for the global minimum. It is possible to utilize the structure of the problem and make a serial expansion up to second order of the loss function. The expansion gives a simple noniterative suboptimal dual controller in which the increase in computations compared with a self-tuning or cautious regulator is very moderate.

Two similar approaches are to modify the loss functions to

$$\min _ {u (t)} E \left\{(y (t + 1) - u _ {c} (t + 1)) ^ {2} - \rho \frac {\det P (t + 1)}{\det P (t + 2)} \mid \mathcal {Y} _ {t} \right\} \tag {7.21}$$

and

$$\min _ {u (t)} E \left\{\left(y (t + 1) - u _ {c} (t + 1)\right) ^ {2} - \rho \varepsilon^ {2} (t + 1) \mid \mathcal {Y} _ {t} \right\} \tag {7.22}$$

respectively. The innovation $\varepsilon(t + 1)$ is defined as

$$\varepsilon (t + 1) = y (t + 1) - \varphi^ {T} (t) \hat {x} (t + 1)$$

Both these loss functions lead to quadratic criteria that make it possible to derive simple analytic expressions for the control signal.
