Notice that the control variable u now appears explicitly on the right-hand side. In the stabilization problem the error is equal to the vector $\xi$ and the error equation is obtained by combining Eqs. (5.95), (5.100), and (5.101). Following the general MRAS approach, we now attempt to find a feedback law and a parameter adjustment rule that stabilizes the error equation. Choosing

$$2 V = \xi_ {1} ^ {2} + \xi_ {2} ^ {2} + \xi_ {3} ^ {2} + \bar {\theta} ^ {2}$$

as a possible Lyapunov function, we get, after straightforward but tedious calculations,

$$
\begin{array}{l} \frac {d V}{d t} = - \xi_ {1} ^ {2} - \xi_ {2} ^ {2} + \xi_ {2} \xi_ {3} + \xi_ {2} \frac {\partial a _ {1}}{\partial \hat {\theta}} \left(\frac {d \hat {\theta}}{d t} - b _ {2}\right) \\ + \xi_ {3} \left(u + \frac {\partial a _ {1}}{\partial \hat {\theta}} \left(\frac {d \hat {\theta}}{d t} - b _ {2}\right) + \frac {\partial a _ {2}}{\partial \hat {\theta}} \frac {d \hat {\theta}}{d t}\right) \\ + \tilde {\theta} \left(\xi_ {1} f + \xi_ {2} \frac {\partial a _ {1}}{\partial \xi_ {1}} f + \xi_ {3} \left(\frac {\partial a _ {2}}{\partial \xi_ {1}} + \frac {\partial a _ {1}}{\partial \xi_ {1}} \frac {\partial a _ {2}}{\partial \xi_ {2}}\right) f - \frac {d \hat {\theta}}{d t}\right) \\ \end{array}
$$

The term that contains $\tilde{\theta}$ can be eliminated by updating the parameters in the following way:

$$\frac {d \hat {\theta}}{d t} = \xi_ {1} f + \xi_ {2} \frac {\partial a _ {1}}{\partial \xi_ {1}} f + c (\xi_ {1}, \xi_ {2}) \xi_ {3} \tag {5.102}$$

where

$$c \left(\xi_ {1}, \xi_ {2}\right) = \left(\frac {\partial a _ {2}}{\partial \xi_ {1}} + \frac {\partial a _ {1}}{\partial \xi_ {1}} \frac {\partial a _ {2}}{\partial \xi_ {2}}\right) f$$

Furthermore, introducing

$$b _ {3} (\xi_ {1}, \xi_ {2}, \xi_ {3}) = b _ {2} + c \xi_ {3}$$

and

$$a _ {3} = \xi_ {2} + \xi_ {3} + \frac {\partial a _ {2}}{\partial \xi_ {1}} (- \xi_ {1} + \xi_ {2}) + \frac {\partial a _ {2}}{\partial \xi_ {2}} \left(- \xi_ {1} - \xi_ {2} + \xi_ {3} - \xi_ {3} ^ {2} \frac {\partial a _ {1}}{\partial \hat {\theta}} c\right) + \frac {\partial a _ {2}}{\partial \hat {\theta}} b _ {3}$$

we find that

$$\frac {d \hat {\theta}}{d t} - b _ {2} = c \xi_ {3}$$

The derivative of the Lyapunov function can then be written as

$$\frac {d V}{d t} = - \xi_ {1} ^ {2} - \xi_ {2} ^ {2} - \xi_ {3} ^ {2} + \xi_ {3} (u + a _ {3})$$

The feedback law

$$u = - a _ {3} \left(\xi_ {1}, \xi_ {2}, \xi_ {3}\right) \tag {5.103}$$

gives

$$\frac {d V}{d t} = - \xi_ {1} ^ {2} - \xi_ {2} ^ {2} - \xi_ {3} ^ {2}$$

and we find that $dV/dt$ is negative as long as $|\xi| \neq 0$ .

□
