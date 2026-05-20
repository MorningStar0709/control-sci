# 5.2.1 Fixed-Final State and Open-Loop Optimal Control

Let us now discuss the boundary condition and the associated control configurations. For the given or fixed-initial condition (5.2.2) and the fixed-final state as

$$\mathbf {x} (k = k _ {f}) = \mathbf {x} (k _ {f}), \tag {5.2.23}$$

the terminal cost term in the performance index (5.2.3) makes no sense and hence we can set $\mathbf{F}(k_{f}) = 0$ . Also, in view of the fixed-final state condition (5.2.23), the variation $\delta\mathbf{x}(k_{f}) = 0$ and hence the boundary condition (5.2.9) does not exist for this case. Thus, the state and costate system (5.2.22) along with the initial condition (5.2.2) and the fixed-final condition (5.2.23) constitute a two-point boundary value problem (TPBVP). The solution of this TPBVP, gives $\mathbf{x}^{*}(k)$ and $\boldsymbol{\lambda}^{*}(k)$ or $\boldsymbol{\lambda}^{*}(k + 1)$ which along with the control relation (5.2.20) leads us to the so-called open-loop optimal control. The entire procedure is now summarized in Table 5.1.

We now illustrate the previous procedure by considering a simple system.

Table 5.1 Procedure Summary of Discrete-Time Optimal Control System: Fixed-End Points Condition
