Equations (3.25), (3.27), and (3.28) give the closed-loop system

$$y (k) = \frac {0 . 5 K (q + 1)}{(q - 1) (q - 1 + T _ {d} K) + 0 . 5 K (q + 1)} u _ {c} (k) \tag {3.29}$$

The system is of second order, and there are two free parameters, K and $T_{d}$ , that can be used to select the closed-loop poles. The closed-loop system is stable if K > 0, $T_{d} > 0.5$ , and $T_{d}K < 2$ . The root locus with respect to K of the characteristic equation of (3.29) is shown in Fig. 3.17 when $T_{d} = 1.5$ .

Let the reference signal be a step. Figure 3.18 shows the continuous-time output for four different values of K. The behavior of the closed-loop system varies from an oscillatory to a well-damped response. When K = 1, the poles are in the origin and the output is equal to the reference value after two samples. This is called deadbeat control and is discussed further in Chapters 4 and 5. When K > 1, the output and the control signal oscillate because of the discrete-time pole on the negative real axis. The poles are inside the unit circle if K < 4/3.

To determine the closed-loop response, it is important to understand the connection between the discrete-time poles and the response of the system. This is discussed in Sec. 2.8. From Fig. 2.8 it can be seen that K = 0.75 corresponds to a damping of $\zeta = 0.4$ . The distance to the origin is a measure of the speed of the system.

The behavior of the double integrator with some simple controllers has been discussed; the results can be generalized to more complex systems. Also, the importance of analysis and simulation has been illustrated.

![](image/7a97c34fd2bbb1c02f5795abf52517782b1aa23c29743adbcb782e3af9a7d70b.jpg)

<details>
<summary>scatter</summary>

| Point Type | Real axis | Imaginary axis |
| --- | --- | --- |
| Circle | 0.5 | 0.0 |
| Star | 1.0 | 0.0 |
</details>

Figure 3.17 The root locus of the characteristic equation of the system in (3.29) with respect to the parameter K when $T_{d} = 1.5$ .
