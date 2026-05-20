7.21 For the system

$$
\begin{array}{l} \dot {\mathbf {x}} = \left[ \begin{array}{l l l} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right] \mathbf {x} + \left[ \begin{array}{l} 0 \\ 0 \\ 1 \end{array} \right] u \\ y = \left[ \begin{array}{l l l} 1 & 0 & 0 \end{array} \right] \mathbf {x} \\ \end{array}
$$

verify stabilizability and detectability.

\*Hint Controllability guarantees stabilizability, and observability ensures detectability.

Calculate (analytically) the state feedback gain matrix that minimizes $J = \int_0^\infty [y^2 (t) + \rho u^2 (t)]dt, \rho > 0$ .

M

7.22 Servo with flexible shaft We wish to design an LQ regulator for the dc servo of Problem 2.5 (Chapter 2), for the set point $\theta_{2} = \theta_{d}$ . The control objective is to achieve the fastest possible response consistent with constraints on the motor voltage and on the torsion force on the shaft. Specifically, the control should be such that the zero-state response to a step $\theta_{d}$ of 1 rad should not call for a motor voltage magnitude of more than $5\mathrm{V}$ , and $|\theta_{1} - \theta_{2}| = |\Delta|$ should be held below 0.03 radians.

a. Calculate the dc steady state corresponding to $\theta_{2} = \theta_{d}$ , and write the state equations for $\Delta \mathbf{x} = \mathbf{x} - \mathbf{x}^{*}$ , the incremental state variables.   
b. Define $J = \int_0^\infty [Q_{11}\Delta^2 + Q_{33}(\theta_2 - \theta_d)^2 + Rv^2]dt$ . Use as starting values $Q_{11} = 1 / (.03)^2$ , $Q_{33} = 1$ , and $R = 1 / (5)^2$ , and calculate the optimal LQ gain.   
c. Compute the closed-loop zero-state response to a unit step $\theta_{d}=1$ rad.   
d. Repeat parts (b) and (c), increasing weights on those terms of $J$ that correspond to constraints that are violated, and decreasing weights if the constraints are satisfied.

M

7.23 Drum speed control An LQ control system is to be designed to regulate the drum speed $\omega_{0}$ in Problem 2.6 (Chapter 2). To prevent undue torsion stress, the shaft torsion angles should be less than 0.02 rad in magnitude. The voltage inputs $u_{1}$ and $u_{2}$ should be held to magnitudes less than 180 V. The load torque $T_{0}$ is assumed to be zero.

The control system should maximize the speed of response of $\omega_{0}$ , from the zero state to a constant steady-state $\omega_{d}=2.0$ rad/s, while satisfying constraints. Use
