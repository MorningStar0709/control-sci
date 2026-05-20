# EXAMPLE 9.2 Tank system

Consider a tank in which the cross section $A$ varies with height $h$ . The model is

$$V = \int_ {0} ^ {h} A (\tau) d \tau\frac {d V}{d t} = A (h) \frac {d h}{d t} = q _ {t} - a \sqrt {2 g h}$$

where V is the volume, $q_{i}$ is the input flow, and a is the cross section of the outlet pipe. Let $q_{i}$ be the input, and let h be the output of the system. The linearized model at an operating point, $q_{in}^{0}$ and $h^{0}$ , is given by the transfer function

$$G (s) = \frac {\beta}{s + \alpha}$$

where

$$\beta = \frac {1}{A (h ^ {0})} \quad \alpha = \frac {q _ {i n} ^ {0}}{2 A (h ^ {0}) h ^ {0}} = \frac {a \sqrt {2 g h ^ {0}}}{2 A (h ^ {0}) h ^ {0}}$$

A good PI control of the tank is given by

$$u (t) = K \left(e (t) + \frac {1}{T _ {i}} \int e (\tau) d \tau\right)$$

where

$$K = \frac {2 \zeta \omega - \alpha}{\beta}$$

and

$$T _ {i} = \frac {2 \zeta \omega - \alpha}{\omega^ {2}}$$

This gives a closed-loop system with natural frequency $\omega$ and relative damping $\zeta$ . Introducing the expressions for $\alpha$ and $\beta$ gives the following gain schedule:

$$K = 2 \zeta \omega A (h ^ {0}) - \frac {q _ {i n} ^ {0}}{2 h ^ {0}}T _ {i} = \frac {2 \zeta}{\omega} - \frac {q _ {i n} ^ {0}}{2 A (h ^ {0}) h ^ {0} \omega^ {2}}$$

The numerical values are often such that $\alpha \ll 2\zeta\omega$ . The schedule can then be simplified to

$$K = 2 \zeta \omega A (h ^ {0})T _ {i} = \frac {2 \zeta}{\omega}$$

In this case it is thus sufficient to make the gain proportional to the cross section of the tank.

Example 9.2 illustrates that it can sometimes be sufficient to measure one or two variables in the process and use them as inputs to the gain schedule. Often, it is not as easy as in Example 9.2 to determine the controller parameters as a function of the measured variables. The design of the controller must then be redone for different working points of the process. Some care must also be exercised if the measured signals are noisy. They may have to be filtered properly before they are used as scheduling variables.

The next example illustrates that gains, delays, and time constants are often inversely proportional to the production rate of the process. This fact can be used to make time scaling.
