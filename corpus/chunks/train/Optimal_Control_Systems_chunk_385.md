# 7.1.4 Structure of Time-Optimal Control System

We examine two natural structures, i.e., open-loop and closed-loop structures for implementation of time-optimal control system.

1. Open-Loop Structure: We repeat here again the time-optimal control system and summarize the result. For the normal time-optimal control system, where the system is described by

$$\dot {\mathbf {x}} (t) = \mathbf {A} \mathbf {x} (t) + \mathbf {B} \mathbf {u} (t) \tag {7.1.38}$$

with the constraint on the control as

$$\left| u _ {j} (t) \right| \leq 1, \quad j = 1, 2, \dots , r. \tag {7.1.39}$$

the time-optimal control is to find the control which drives the system (7.1.38) from any initial condition $\mathbf{x}(0)$ to target condition 0 in minimum time under the constraint (7.1.39). From the previous discussion, we know that the optimal control is given by

$$u _ {j} ^ {*} (t) = - s g n \{\mathbf {b} _ {j} ^ {\prime}, \lambda^ {*} (t) \} \tag {7.1.40}$$

where, the costate function $\lambda^{*}(t)$ is

$$\boldsymbol {\lambda} ^ {*} (t) = \epsilon^ {- \mathbf {A} ^ {\prime} t} \boldsymbol {\lambda} ^ {*} (0). \tag {7.1.41}$$

Let us note that the initial condition $\lambda^{*}(0)$ is not specified and hence arbitrary, and hence we have to adopt an iterative procedure. Thus, the steps involved in obtaining the optimal control are given as follows.

(a) Assume a value for the initial condition $\lambda^{*}(0)$ .   
(b) Using the initial value in (7.1.41), compute the costate $\lambda^{*}(t)$ .   
(c) Using the costate $\lambda^{*}(t)$ , evaluate the control (7.1.40).   
(d) Using the control $\mathbf{u}^{*}(t)$ , solve the system relation (7.1.38).   
(e) Monitor the solution $\mathbf{x}^{*}(t)$ and find if there is a time $t_f$ such that the system goes to zero, i.e., $\mathbf{x}(t_f) = 0$ . Then the corresponding control computed previously is the time-optimal control. If not, then change the initial value of $\lambda^{*}(0)$ and repeat the previous steps until $\mathbf{x}(t_f) = 0$ .

A schematic diagram showing the open-loop, time-optimal control structure is shown in Figure 7.5. The relay shown in the figure is an engineering realization of signum function. It gives the required control sequences +1 or -1 depending on its input. However, we note the following:

![](image/55a051152848449c364f0ae42637dc51279c7048cba514db008d680271ae9a1d.jpg)

<details>
<summary>flowchart</summary>
