Then the change in the control pressure $p _ { c }$ will be instantaneous.The restriction R will momentarily prevent the feedback bellows from sensing the pressure change $p _ { c }$ .Thus the feedback bellows will not respond momentarily, and the pneumatic actuating valve will feel the full effect of the movement of the flapper.As time goes on,the feedback bellows will expand. The change in the nozzle–flapper distance x and the change in the control pressure $p _ { c }$ can be plotted against time t, as shown in Figure 4–14(b). At steady state, the feedback bellows acts like an ordinary feedback mechanism.The curve $p _ { c }$ versus t clearly shows that this controller is of the proportional-plus-derivative type.

A block diagram corresponding to this pneumatic controller is shown in Figure 4–14(c). In the block diagram, K is a constant, A is the area of the bellows, and $k _ { s }$ is the equivalent spring constant of the bellows.The transfer function between $p _ { c }$ and e can be obtained from the block diagram as follows:

$$\frac {P _ {c} (s)}{E (s)} = \frac {\frac {b}{a + b} K}{1 + \frac {K a}{a + b} \frac {A}{k _ {s}} \frac {1}{R C s + 1}}$$

In such a controller the loop gain $\left| K a A / [ ( a + b ) k _ { s } ( R C s + 1 ) ] \right|$ is made much greater than unity. Thus the transfer function $P _ { c } ( s ) / E ( s )$ can be simplified to give

$$\frac {P _ {c} (s)}{E (s)} = K _ {p} \left(1 + T _ {d} s\right)$$

where

$$K _ {p} = \frac {b k _ {s}}{a A}, \quad T _ {d} = R C$$

Thus, delayed negative feedback, or the transfer function $1 / ( R C s + 1 )$ in the feedback path, modifies the proportional controller to a proportional-plus-derivative controller.

Note that if the feedback valve is fully opened, the control action becomes proportional. If the feedback valve is fully closed, the control action becomes narrow-band proportional (on–off).

Obtaining Pneumatic Proportional-Plus-Integral Control Action. Consider the proportional controller shown in Figure 4–13(a). Considering small changes in the variables, we can show that the addition of delayed positive feedback will modify this proportional controller to a proportional-plus-integral controller, or a PI controller.
