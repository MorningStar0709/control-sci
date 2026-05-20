# Exercise 2.20: LQR versus LAR

We are now all experts on the linear quadratic regulator (LQR), which employs a linear model and quadratic performance measure. Let’s consider the case of a linear model but absolute value performance measure, which we call the linear absolute regulator $( \mathrm { L A R } ) ^ { 9 }$

$$\min _ {\mathbf {u}} \sum_ {k = 0} ^ {N - 1} (q | x (k) | + r | u (k) |) + q (N) | x (N) |$$

For simplicity consider the following one-step controller, in which u and x are scalars

$$\min _ {u (0)} V (x (0), u (0)) = | x (1) | + | u (0) |$$

subject to

$$x (1) = A x (0) + B u (0)$$

Draw a sketch of x(1) versus u(0) (recall x(0) is a known parameter) and show the x-axis and y-axis intercepts on your plot. Now draw a sketch of $V ( x ( 0 ) , u ( 0 ) )$ versus u(0) in order to see what kind of optimization problem you are solving. You may want to plot both terms in the objective function individually and then add them together to make your V plot. Label on your plot the places where the cost function V suffers discontinuities in slope. Where is the solution in your sketch? Does it exist for all $A , B , x ( 0 ) \ ?$ Is it unique for all $A , B , x ( 0 ) \ ?$

The motivation for this problem is to change the quadratic program (QP) of the LQR to a linear program (LP) in the LAR, because the computational burden for LPs is often smaller than QPs. The absolute value terms can be converted into linear terms with a standard trick involving slack variables.

![](image/c40ae1d1f6d5174cae032a7e416e89ef8751ee1900554986232df777990fb8e6.jpg)

<details>
<summary>text_image</summary>

x
ℓ(x,u) = const
(unreachable)
ℓs(x,u) = const
Unconstrained
ℓs(x,u) = const
Constrained
steady-state line
(xsp,usp)
(xs,us)
(xs,us)
(xs,us)
(xs,us)
(xs,us)
U
u
</details>

Figure 2.10: Inconsistent setpoint $( x _ { \mathrm { s p } } , u _ { \mathrm { s p } } )$ , unreachable stage cost $\ell ( x , u )$ , and optimal steady states $( x _ { s } , u _ { s } )$ , and stage costs $\ell _ { s } ( x , u )$ for constrained and unconstrained systems.
