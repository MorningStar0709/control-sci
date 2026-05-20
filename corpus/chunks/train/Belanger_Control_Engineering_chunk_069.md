d. Write Newton's second law for $\ddot{z}$ , $\ddot{y}$ , and $\ddot{\theta}$ in terms of the incremental forces $\Delta F_{L1}$ , $\Delta F_{L2}$ , $\Delta F_{G1}$ , and $\Delta F_{G2}$ ; the wind force $F_W$ ; and the guideway elevation $z_G$ . (The moment of inertia about the center of gravity is $J = 2500\mathrm{kgm}^2$ .)   
e. The control inputs are defined to be currents squared; i.e., $u = i^2$ . Linearize the magnetic forces about the respective equilibrium values of $u$ and $S$ to obtain linear expressions in $\Delta u$ and $\Delta S$ for each $\Delta F$ .   
f. Obtain a linear expression for each $\Delta S$ in terms of $z_G, \Delta z, \Delta y$ , and $\theta$ . Do this by calculating $\Delta S$ from individual changes in $\Delta z, \Delta y$ , and $\theta$ ( $\theta$ small), and summing the contributions. Insert the results in the Newton's law equations, and derive the state equations (six state variables).

M

2.21 It is possible to linearize about a trajectory rather than a point. Consider the system

$$\dot {\mathbf {x}} = \mathbf {f} (\mathbf {x}, \mathbf {u})\mathbf {y} = \mathbf {h} (\mathbf {x}, \mathbf {u}).$$

Let $\mathbf{x}^{*}(t),\mathbf{u}^{*}(t)$ , and $\mathbf{y}^{*}(t)$ , the nominal state trajectory, input, and output functions, satisfy the system equations. Define

$$\Delta \mathbf {x} (t) = \mathbf {x} (t) - \mathbf {x} ^ {*} (t), \quad \Delta \mathbf {u} (t) = \mathbf {u} (t) - \mathbf {u} ^ {*} (t), \quad \Delta \mathbf {y} (t) = \mathbf {y} (t) - \mathbf {y} ^ {*} (t).$$

a. Derive, under the assumption of small $\Delta x$ , $\Delta u$ , and $\Delta y$ , the equations satisfied by these quantities. Show that this incremental system is time-varying, in general.

b. Given the nonlinear system

$$
\begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = - x _ {1} - x _ {2} ^ {3} + x _ {2} u \\ y = x _ {1} \\ \end{array}
$$

compute the trajectory $x^{*}(t), 0 \leq t \leq 5$ , for $x_{1}(0) = 1, x_{2}(0) = 0$ , and $u(t) = t$ . Also compute, as functions of time, the elements of the matrices of the linearized system for $0 \leq t \leq 5$ .
