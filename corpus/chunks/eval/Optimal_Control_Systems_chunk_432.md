# 7.6 Optimal Control Systems with State Constraints

By simple calculus, we see that the expression $\frac{1}{2} u^2 (t) + \lambda_2^* (t)u(t)$ will attain the optimum value for

$$u ^ {*} (t) = - \lambda_ {2} ^ {*} (t) \tag {7.6.26}$$

when the control $u^{*}(t)$ is unconstrained. This can also be seen alternatively by using the relation

$$\frac {\partial \mathcal {H}}{\partial u} = 0 \longrightarrow u ^ {*} (t) + \lambda_ {2} ^ {*} (t) = 0 \longrightarrow u ^ {*} (t) = - \lambda_ {2} ^ {*} (t). \tag {7.6.27}$$

But, for the present constrained control situation (7.6.14), we see from (7.6.25) or (7.6.26) that

$$
u ^ {*} (t) = \left\{ \begin{array}{l l} - 1, & \text { if } \quad \lambda_ {2} ^ {*} (t) > + 1 \\ + 1, & \text { if } \quad \lambda_ {2} ^ {*} (t) <   - 1. \end{array} \right. \tag {7.6.28}
$$

Combining the unsaturated or unconstrained control (7.6.26) with the saturated or constrained control (7.6.28), we have

$$
u ^ {*} (t) = \left\{ \begin{array}{l l} + 1, & \text { if } \quad \lambda_ {2} ^ {*} (t) <   - 1 \\ - 1, & \text { if } \quad \lambda_ {2} ^ {*} (t) > + 1 \\ - \lambda_ {2} ^ {*} (t), & \text { if } \quad - 1 \leq \lambda_ {2} ^ {*} (t) \leq + 1. \end{array} \right. \tag {7.6.29}
$$

Using the definition of saturation function (7.5.28), the previous optimal control strategy can be written as

$$u _ {j} ^ {*} (t) = - s a t \left\{\lambda_ {2} ^ {*} (t) \right\}. \tag {7.6.30}$$

The situation is shown in Figure 7.43. Thus, one has to solve for the costate function $\lambda_2^*(t)$ completely to find the optimal control $u^*(t)$ from (7.6.29) to get open-loop optimal control implementation.

Note: In obtaining the optimal control strategy in general, one cannot obtain the unconstrained or unsaturated control first and then just extend the same for constrained or saturated region. Instead, one has to really use the Hamiltonian relation (7.6.13) to obtain the optimal control. Although, in this chapter, we considered control constraints and state constraints separately, we can combine both of them and have a situation with constraints as

$$\mathbf {g} (\mathbf {x} (t), \mathbf {u} (t), t) \leq 0. \tag {7.6.31}$$

For further details, see the recent book [61] and the survey article [62].

![](image/bea03e5e249374c6503b71f44dbf00c5665ee86297c2b5bb1ddc95347db8077c.jpg)

<details>
<summary>text_image</summary>

λ₂*(t)
-1
+1
-1
+1
u*(t)
</details>

Figure 7.43 Relation between Optimal Control $u^{*}(t)$ and Optimal Costate $\lambda_2^*(t)$
