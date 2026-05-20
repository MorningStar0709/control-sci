# EXAMPLE 5.17 Stabilization by backstepping

Consider the system described by

$$\frac {d x _ {1}}{d t} = x _ {2} + f (x _ {1})\frac {d x _ {2}}{d t} = x _ {3} \tag {5.91}\frac {d x _ {3}}{d t} = u$$

Introduce $\xi_{1} = x_{1}$ . Then

$$\frac {d \xi_ {1}}{d t} = x _ {2} + f (\xi_ {1}) = - \xi_ {1} + x _ {2} + \xi_ {1} + f (\xi_ {1})$$

If we introduce the function

$$a _ {1} (\xi_ {1}) = \xi_ {1} + f (\xi_ {1})$$

and the state variable

$$\xi_ {2} = x _ {2} + a _ {1} \left(\xi_ {1}\right) \tag {5.92}$$

the differential equation for $\xi_{1}$ can be written as

$$\frac {d \xi_ {1}}{d t} = - \xi_ {1} + \xi_ {2}$$

The derivative of the variable $\xi_{2}$ is given by

$$\frac {d \xi_ {2}}{d t} = \frac {d x _ {2}}{d t} + \frac {d a _ {1}}{d \xi_ {1}} (- \xi_ {1} + \xi_ {2}) = - \xi_ {2} + x _ {3} + \xi_ {2} + \frac {d a _ {1}}{d \xi_ {1}} (- \xi_ {1} + \xi_ {2})$$

If we introduce the function

$$a _ {2} (\xi_ {1}, \xi_ {2}) = \xi_ {2} + \frac {d a _ {1}}{d \xi_ {1}} (- \xi_ {1} + \xi_ {2})$$

and the state variable

$$\xi_ {3} = x _ {3} + a _ {2} (\xi_ {1}, \xi_ {2})$$

the differential equation for $\xi_{2}$ can be written as

$$\frac {d \xi_ {2}}{d t} = - \xi_ {2} + \xi_ {3}$$

Taking derivatives of $\xi_{3}$ and using Eqs. (5.91), we find that

$$\frac {d \xi_ {3}}{d t} = u + \frac {\partial a _ {2}}{\partial \xi_ {1}} (- \xi_ {1} + \xi_ {2}) + \frac {\partial a _ {2}}{\partial \xi_ {2}} (- \xi_ {2} + \xi_ {3})$$

Introducing the function

$$a _ {3} \left(\xi_ {1}, \xi_ {2}, \xi_ {3}\right) = \xi_ {3} + \frac {\partial a _ {2}}{\partial \xi_ {1}} (- \xi_ {1} + \xi_ {2}) + \frac {\partial a _ {2}}{\partial \xi_ {2}} (- \xi_ {2} + \xi_ {3})$$

we find that the differential equation for $\xi_{3}$ can be written as

$$\frac {d \xi_ {3}}{d t} = - \xi_ {3} + a _ {3} (\xi_ {1}, \xi_ {2}, \xi_ {3}) + u$$

The feedback

$$u = - a _ {3} \left(\xi_ {1}, \xi_ {2}, \xi_ {3}\right)$$

gives the closed-loop system described by

$$
\frac {d \xi}{d t} = \left( \begin{array}{c c c} - 1 & 1 & 0 \\ 0 & - 1 & 1 \\ 0 & 0 & - 1 \end{array} \right) \xi \tag {5.93}
$$

This system is clearly stable, and its state $\xi$ goes to zero exponentially. Notice that by a slight modification of the procedure we can have any number in the diagonal of the system matrix.

The transformation was obtained recursively. Notice that if the variable $x_{2}$ was a control variable that could be chosen freely, the “control law”

$$x _ {2} = - a _ {1} (\xi_ {1})$$

would give

$$\frac {d \xi_ {1}}{d t} = - \xi_ {1}$$
