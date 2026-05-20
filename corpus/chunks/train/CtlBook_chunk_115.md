# 4.3 System Matrices from Equations of Motion

Let's see how EOMs turn into the State Space representation using the example system of Figure 4.1. Writing the EOM:

$$M \ddot {x} + B \dot {x} + (K _ {1} + K _ {2}) x = f (t)$$

rearranging to solve for x¨:

$$\ddot {x} = \frac {1}{M} \left[ - B \dot {x} - (K _ {1} + K _ {2}) x + f (t) \right]\ddot {x} = - \frac {B}{M} \dot {x} - \frac {K _ {1} + K _ {2}}{M} x + \frac {1}{M} f (t)$$

Converting this to a matrix equation is just rearranging according to

$$
\dot {X} = \left[ \begin{array}{c} \dot {x} \\ \ddot {x} \end{array} \right] \qquad X = \left[ \begin{array}{c} x \\ \dot {x} \end{array} \right] \qquad U = [ f (t) ]
$$

then we have

$$
\dot {X} = \left[ \begin{array}{c} \dot {x} \\ \ddot {x} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ \frac {- (K _ {1} + K _ {2})}{M} & \frac {- B}{M} \end{array} \right] \left[ \begin{array}{c} x \\ \dot {x} \end{array} \right] + \left[ \begin{array}{c} 0 \\ \frac {1}{M} \end{array} \right] [ f (t) ]
$$

The top row is sort of a trivial equation, and the second row is the rearranged equation of motion. This is the state space description for the system of Figure 4.1.
