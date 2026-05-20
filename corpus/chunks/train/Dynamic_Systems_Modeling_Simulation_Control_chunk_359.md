# First-Order Response with Zero Input

To begin the analysis of a first-order system response, we consider the case with zero input, which leads to the homogeneous differential equation

$$\tau \dot {y} + y = 0 \tag {7.26}$$

The characteristic equation can be obtained by inspection

$$\tau r + 1 = 0 \tag {7.27}$$

and therefore the single characteristic root is $r = - 1 / \tau$ . The homogeneous solution is an exponential function

$$y _ {H} (t) = c e ^ {r t} = c e ^ {- t / \tau} \tag {7.28}$$

For the case with zero input, there is no particular solution $y _ { P } ( t )$ , so the homogeneous solution $y _ { H } ( t )$ is the total or complete solution. Furthermore, the constant c is determined by applying the initial condition at time $t = 0 , \mathrm { { s o } } y ( 0 ) = c e ^ { 0 } = c = y _ { 0 }$ . Hence, the total response of the first-order system for the case of zero input is

$$y (t) = y _ {0} e ^ {- t / \tau} \tag {7.29}$$

which is either an exponentially decaying or divergent function, depending on the sign of the characteristic root, r. If root $r < 0$ (or, constant $\tau > 0 )$ , then the solution y(t) decays from its initial condition $y _ { 0 }$ to zero as time $t \to \infty$ and the response is bounded or stable. $\mathrm { I f } \ r > 0 .$ , then y(t) diverges to infinity as time t → ∞ and the response is unbounded or unstable. We see from Tables 7.1 and 7.2 that the constant ?? is always positive for these physical systems, and hence the free response Eq. (7.29) will be an exponential decay to zero at steady state. The parameter ?? is called the time constant for the first-order system.

Figure 7.5 presents the free or natural response of a general first-order system with zero input and initial condition $y _ { 0 } .$ . Note that when time $t = \tau$ , the free response has decayed to 36.8% of its initial value because $e ^ { - 1 } = 0 . 3 6 8$ . At time $t = 4 \tau$ , the free response has decayed to less than 2% of its initial value as $e ^ { - 4 } = 0 . 0 1 8 .$ , and therefore we can say that the first-order free response has essentially reached the zero steady-state value as shown in Fig. 7.5. Clearly, the time constant ?? determines the response time of the first-order free response.

![](image/ba6f794b4ee914cc33c355d5abbabb2def0c19e67dc46d7aef5b2d4bee4781fb.jpg)

<details>
<summary>line</summary>

| t | y₀ |
| --- | --- |
| τ | 0.368y₀ |
| 4τ | 0.018y₀ |
</details>

Figure 7.5 Free response of the first-order model $\tau \dot { y } + y = 0$ .
