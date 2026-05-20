# 4.3 Fixed-End-Point Regulator System

In this section, we discuss the fixed-end-point state regulator system, where the final state $\mathbf{x}(t_{f})$ is zero and the final time $t_{f}$ is fixed [5]. This is different from the conventional free-end-point state regulator system with the final time $t_{f}$ being free, leading to the matrix Riccati differential equation that was discussed in Chapter 3. Following the procedure similar to the free-end-point system, we will arrive at the same matrix differential Riccati equation (3.2.18). But, if we use the earlier transformation (3.2.11) to find the corresponding boundary condition for (3.2.18), we see that

$$\boldsymbol {\lambda} (t _ {f}) = \mathbf {F} (t _ {f}) \mathbf {x} (t _ {f}) = \mathbf {P} (t _ {f}) \mathbf {x} (t _ {f}) \tag {4.3.1}$$

and for the fixed final condition $\mathbf{x}(t_f) = 0$ , and for arbitrary $\lambda(t_f)$ , we have

$$\mathbf {P} (t _ {f}) = \infty . \tag {4.3.2}$$

This means that for the fixed-end-point regulator system, we solve the matrix DRE (3.2.18) using the final condition (4.3.2). In practice, we may start with a very large value of $\mathbf{P}(t_{f})$ instead of $\infty$ .

Alternatively, we present a different procedure to find closed-loop optimal control for the fixed-end-point system [5]. In fact, we will use what is known as inverse Riccati transformation between the state and costate variables and arrive at matrix inverse Riccati equation.

As before, consider a linear, time-varying system

$$\dot {\mathbf {x}} (t) = \mathbf {A} (t) \mathbf {x} (t) + \mathbf {B} (t) \mathbf {u} (t) \tag {4.3.3}$$

with a cost functional

$$J (\mathbf {u}) = \frac {1}{2} \int_ {t _ {0}} ^ {t _ {f}} \left[ \mathbf {x} ^ {\prime} (t) \mathbf {Q} (t) \mathbf {x} (t) + \mathbf {u} ^ {\prime} (t) \mathbf {R} (t) \mathbf {u} (t) \right] d t \tag {4.3.4}$$

where, $\mathbf{x}(t)$ is nth state vector, $\mathbf{u}(t)$ is rth control vector, $\mathbf{A}(t)$ is nxn state matrix, and $\mathbf{B}(t)$ is nxr control matrix. We assume that the control is unconstrained. The boundary conditions are given as

$$\mathbf {x} (t = t _ {0}) = \mathbf {x} _ {0}; \quad \mathbf {x} (t = t _ {f}) = \mathbf {x} _ {f} = 0 \tag {4.3.5}$$

where, $t_f$ is fixed or given a priori. Here, we can easily see that for fixed final condition, there is no meaning in having a terminal cost term in the cost function (4.3.4).
