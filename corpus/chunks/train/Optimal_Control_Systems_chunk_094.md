# 2.5.2 Lagrange Multiplier Method

We now generalize the second method of solving the same problem of extrema of functions with conditions. Consider again the extrema of the function $f(x_{1}, x_{2})$ subject to the condition

$$g (x _ {1}, x _ {2}) = 0. \tag {2.5.24}$$

In this method, we form an augmented Lagrangian function

$$\mathcal {L} \left(x _ {1}, x _ {2}, \lambda\right) = f \left(x _ {1}, x _ {2}\right) + \lambda g \left(x _ {1}, x _ {2}\right) \tag {2.5.25}$$

where, $\lambda$ , a parameter (multiplier) yet to be determined, is the Lagrange multiplier. Let us note that using the given condition (2.5.24) in the Lagrangian (2.5.25), we have

$$\mathcal {L} (x _ {1}, x _ {2}) = f (x _ {1}, x _ {2}) \tag {2.5.26}$$

and therefore a necessary condition for extrema is that

$$d f = d \mathcal {L} = 0. \tag {2.5.27}$$

Accepting the idea that the Lagrangian (2.5.25) is a better representation of the entire problem than the equation (2.5.26) in finding the extrema, we have from the Lagrangian relation (2.5.25)

$$d \mathcal {L} = d f + \lambda d g = 0. \tag {2.5.28}$$

Using (2.5.17) and (2.5.18) in (2.5.28), and rearranging

$$\left[ \frac {\partial f}{\partial x _ {1}} + \lambda \frac {\partial g}{\partial x _ {1}} \right] d x _ {1} + \left[ \frac {\partial f}{\partial x _ {2}} + \lambda \frac {\partial g}{\partial x _ {2}} \right] d x _ {2} = 0. \tag {2.5.29}$$

Now $dx_{1}$ and $dx_{2}$ are both not independent and hence cannot immediately conclude that each of the coefficients of $dx_{1}$ and $dx_{2}$ in (2.5.29) must be zero. Let us choose $dx_{1}$ to be independent differential and then $dx_{2}$ becomes a dependent differential as per (2.5.18). Further, let us choose the multiplier $\lambda$ , which has been introduced by us and is at our disposal, to make one of the coefficients of $dx_{1}$ or $dx_{2}$ in (2.5.29) zero. For example, let $\lambda$ take on the value $\lambda^{*}$ that makes the coefficient of the dependent differential $dx_{2}$ equal zero, that is

$$\frac {\partial f}{\partial x _ {2}} + \lambda^ {*} \frac {\partial g}{\partial x _ {2}} = 0. \tag {2.5.30}$$

With (2.5.30), the equation (2.5.29) reduces to

$$\left[ \frac {\partial f}{\partial x _ {1}} + \lambda \frac {\partial g}{\partial x _ {1}} \right] d x _ {1} = 0. \tag {2.5.31}$$

Since, $dx_{1}$ is the independent differential, it can be varied arbitrarily. Hence, for (2.5.31) to be satisfied for all $dx_{1}$ , the coefficient of $dx_{1}$ must be zero. That is
