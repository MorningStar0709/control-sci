The state variable $\xi_{2}$ defined by Eq. (5.92) can thus be interpreted as the difference between $x_{2}$ and the "stabilizing feedback" $-a_{1}(\xi_{1})$ .

Similarly, if $x_{3}$ was a control variable that could be chosen freely, the “control law”

$$x _ {3} = - a _ {2} \left(\xi_ {1}, \xi_ {2}\right)$$

would give the closed-loop system

$$\frac {d \xi_ {1}}{d t} = - \xi_ {1} + \xi_ {2}\frac {d \xi_ {2}}{d t} = - \xi_ {2}$$

The state variable $\xi_{3}$ can be interpreted as the difference between $x_{3}$ and the “stabilizing feedback” $-a_{2}(\xi_{1},\xi_{2})$ .

The procedure was originally derived by applying this reasoning recursively, and the name "backstepping" derives from this.

In the example the system was transformed to a triangular form given by Eq. (5.93). There are many other possibilities. $\square$
