Design by Pole Placement. In the conventional approach to the design of a singleinput, single-output control system, we design a controller (compensator) such that the dominant closed-loop poles have a desired damping ratio $\zeta$ and a desired undamped natural frequency $\omega _ { n }$ . In this approach, the order of the system may be raised by 1 or 2 unless pole–zero cancellation takes place. Note that in this approach we assume the effects on the responses of nondominant closed-loop poles to be negligible.

Different from specifying only dominant closed-loop poles (the conventional design approach), the present pole-placement approach specifies all closed-loop poles. (There is a cost associated with placing all closed-loop poles, however, because placing all closedloop poles requires successful measurements of all state variables or else requires the inclusion of a state observer in the system.) There is also a requirement on the part of the system for the closed-loop poles to be placed at arbitrarily chosen locations.The requirement is that the system be completely state controllable. We shall prove this fact in this section.

Consider a control system

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} u \tag {10-1}y = \mathbf {C x} + D u$$

where x = state vector (n-vector)

y = output signal (scalar)

u = control signal (scalar)

A = n \* n constant matrix

B = n \* 1 constant matrix

C = 1 \* n constant matrix

D = constant (scalar)

We shall choose the control signal to be

$$u = - \mathbf {K} \mathbf {x} \tag {10-2}$$

This means that the control signal u is determined by an instantaneous state. Such a scheme is called state feedback. The 1\*n matrix K is called the state feedback gain matrix. We assume that all state variables are available for feedback. In the following analysis we assume that u is unconstrained. A block diagram for this system is shown in Figure 10–1.

This closed-loop system has no input. Its objective is to maintain the zero output. Because of the disturbances that may be present, the output will deviate from zero.The nonzero output will be returned to the zero reference input because of the state feedback scheme of the system. Such a system where the reference input is always zero is called a regulator system. (Note that if the reference input to the system is always a nonzero constant, the system is also called a regulator system.)

Substituting Equation (10–2) into Equation (10–1) gives
