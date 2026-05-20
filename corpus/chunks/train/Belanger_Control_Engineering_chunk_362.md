# 6.17 Heat exchanger

a. Modify the design of Problem 6.13 by changing from proportional to PI control. Keep the same stability margins (approximately).   
b. Obtain, for both the proportional and PI designs, the response $\Delta T_{c3}$ to unit step changes in the set point to $\Delta T_{c3}$ and in the disturbance $\Delta T_{c0}$ .

6.18 Flow control The flow control example of Problem 2.10 (Chapter 2) has a model without dynamics. An integral control $\Delta u = (1 / \tau s)(F_d - F)$ is to be used.

a. Using the results of Problem 2.16 (Chapter 2), calculate the range spanned by the small-signal gain $\Delta F / \Delta u$ as $P_{1}^{*}$ ranges from 2 to 5 kpa and $P_{2}^{*}$ lies between 0.5 and 1 kpa.   
b. Calculate $\tau$ so that the crossover frequency of the linearized loop gain is at least 60 rad/s for all conditions in part (a). What is the maximum crossover frequency?

6.19 Flow control The dynamics of the valve stem are actually not instantaneous, but are modeled as $u/u_{d} = \omega_{0}^{2}/(s^{2} + \sqrt{2}\omega_{0}s + \omega_{0}^{2})$ . The fact that these dynamics were not taken into account in Problem 6.18 raises the question of stability of the design. For the value of $\tau$ obtained in Problem 6.18, what condition must $\omega_{0}$ satisfy in order that the small-signal closed-loop system be stable for all small-signal gains in the range obtained from Problem 6.18(a)? (Note: Stability of all possible small-signal models is necessary to the stability of a nonlinear system but is not sufficient.)

6.20 Flow control It is often practical in process control to design flow control loops as a first step in the design process. Figure 6.38 shows a structure, known as cascade control in the process industries, for the level-control problem of Example 2.4 (Chapter 2). The level $\ell$ appears as an input to the flow, because $F_{\mathrm{out}} = cu\sqrt{\ell}$ . The flow loop is the inner loop, and the level loop is the outer loop.
