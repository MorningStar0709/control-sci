# Concluding Comments on Optimal Regulator Systems

1. Given any initial state $\mathbf { x } \big ( t _ { 0 } \big )$ , the optimal regulator problem is to find an allowable control vector ${ \bf \delta u } ( t )$ that transfers the state to the desired region of the state space and for which the performance index is minimized. For the existence of an optimal control vector u(t), the system must be completely state controllable.

2. The system that minimizes (or maximizes, as the case may be) the selected performance index is, by definition, optimal. Although the controller may have nothing to do with “optimality” in many practical applications, the important point is that the design based on the quadratic performance index yields a stable control system.

3. The characteristic of an optimal control law based on a quadratic performance index is that it is a linear function of the state variables, which implies that we need to feed back all state variables. This requires that all such variables be available for feedback. If not all state variables are available for feedback, then we need to employ a state observer to estimate unmeasurable state variables and use the estimated values to generate optimal control signals.

Note that the closed-loop poles of the system designed by the use of the quadratic optimal regulator approach can be found from

$$\left| s \mathbf {I} - \mathbf {A} + \mathbf {B K} \right| = 0$$

Since these closed-loop poles correspond to the desired closed-loop poles in the pole-placement approach, the transfer functions of the observer controllers can be obtained from either Equation (10–74) if the observer is of full-order type or Equation (10–108) if the observer is of minimum-order type.

4. When the optimal control system is designed in the time domain, it is desirable to investigate the frequency-response characteristics to compensate for noise effects. The system frequency-response characteristics must be such that the system attenuates highly in the frequency range where noise and resonance of components are expected. (To compensate for noise effects, we must in some cases either modify the optimal configuration and accept suboptimal performance or modify the performance index.)

5. If the upper limit of integration in the performance index J given by Equation (10–114) is finite, then it can be shown that the optimal control vector is still a linear function of the state variables, but with time-varying coefficients. (Therefore, the determination of the optimal control vector involves that of optimal timevarying matrices.)
