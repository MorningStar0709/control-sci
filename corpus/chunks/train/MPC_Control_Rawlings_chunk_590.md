# 5.1 Introduction

In Chapter 2 we show how model predictive control (MPC) may be employed to control a deterministic system, that is, a system in which there are no uncertainties and the state is known. In Chapter 3 we show how to control an uncertain system in which uncertainties are present but the state is known. Here we address the problem of MPC of an uncertain system in which the state is not fully known. We assume that there are outputs available that may be used to estimate the state as shown in Chapter 4. These outputs are used by the model predictive controller to generate control actions; hence the name output MPC.

Output feedback control is, in general, more complex than state feedback control since knowledge of the state provides considerable information. If the state is known, optimal control is, in general, a timevarying function of the current state even if the system is uncertain as, for example, when it is subject to an additive disturbance. In this case, the state must include the state of the disturbance.

Generally, however, the state is not known; instead, a noisy measurement $y ( t )$ of the state is available at each time t. Since the state x is not known, it is replaced by a hyperstate p that summarizes all prior information (previous inputs and outputs and the prior distribution of the initial state) and that has the “state” property: future values of p can be determined from the current value of p and current and future inputs and outputs. Usually $p ( t )$ is the conditional density of $x ( t )$ given the prior density $p ( 0 )$ of $x ( 0 )$ and the current available “information” $I ( t ) : = \{ \mathcal { y } ( 0 ) , \mathcal { y } ( 1 ) , \ldots , \mathcal { y } ( t - 1 ) , u ( 0 ) , u ( 1 ) , \ldots , u ( t - 1 ) \}$ . If the current hyperstate is known, future hyperstates have to be predicted since future noisy measurements of the state are not known. So the hyperstate satisfies an uncertain difference equation of the form

$$p ^ {+} = \phi (p, u, \psi) \tag {5.1}$$

where $\{ \psi ( t ) \}$ is a sequence of random variables; the problem of controlling a system with unknown state x is transformed into the problem of controlling an uncertain system with known state $p$ . For example, if the underlying system is described by

$$x ^ {+} = A x + B u + wy = C x + v$$
