# State Space Systems

We will now show how Lyapunov's theory can be used to derive stable MRASs for general linear systems. The idea is the same as used previously. It can be described as follows:

1. Find a controller structure.   
2. Derive the error equation.   
3. Find a Lyapunov function and use it to derive a parameter updating law such that the error will go to zero.

Consider a linear system described by

$$\frac {d x}{d t} = A x + B u \tag {5.29}$$

Assume that it is desired to find a control law so that the response to command

![](image/db7c85039013973bb0e7238608fe0ade8081667e5c085cece5dc0fb06ac36ca7.jpg)  
Figure 5.13 Controller parameters $\theta_{1}$ and $\theta_{2}$ for the system in Example 5.7 when $\gamma = 0.2, 1$ , and 5. The dotted lines are the parameters obtained with the MIT rule. Compare Fig. 5.6.

signals is given by

$$\frac {d x _ {m}}{d t} = A _ {m} x _ {m} + B _ {m} u _ {c} \tag {5.30}$$

A general linear control law for the system given by Eq. (5.29) is

$$u = M u _ {c} - L x \tag {5.31}$$

The closed-loop system then becomes

$$\frac {d x}{d t} = (A - B L) x + B M u _ {\mathrm{c}} = A _ {c} (\theta) x + B _ {c} (\theta) u _ {c} \tag {5.32}$$

The control law can be parameterized in different ways. All parameters in the matrices L and M may be chosen freely. There may also be constraints among the parameters. The general case can be captured by assuming that the closed-loop system is described by Eq. (5.32), where matrices $A_{c}$ and $B_{c}$ depend on a parameter $\theta$ .

Compatibility conditions It is not always possible to find parameters $\theta$ such that Eq. (5.32) is equivalent to Eq. (5.30). A sufficient condition is that there exists a parameter value $\theta^{0}$ such that

$$
\begin{array}{l} \boldsymbol {A} _ {c} \left(\theta^ {0}\right) = A _ {m} \\ \boldsymbol {B} _ {c} \left(\theta^ {0}\right) = \boldsymbol {B} _ {m} \end{array} \tag {5.33}
B _ {c} (\theta^ {0}) = B _ {m}
$$

This condition for perfect model-following is fairly stringent. When all parameters in the control law can be chosen freely, it implies that

$$A - A _ {m} = B LB _ {m} = B M$$

This means that the columns of matrices $A - A_{m}$ and $B_{m}$ are linear combinations of the columns of matrix B. If these conditions are satisfied and the columns of B and $B_{m}$ are linearly independent, then the matrices L and M are given by
