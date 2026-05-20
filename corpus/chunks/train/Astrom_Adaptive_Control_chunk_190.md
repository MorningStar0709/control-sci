# Modifications of the Estimator

Disturbances will change the relations between the inputs and the outputs in the model. Load disturbances such as steps will have a particularly bad effect on the low-frequency properties of the model. Several ways to deal with this problem are discussed in Section 11.5. One possibility is to include the disturbance in the model and estimate it; another, which we will use here, is to filter the signal so that the effect of the disturbance is not so large. In the model given by Eq. (3.1) the equation error is $B(q)v$ . This could be a very large quantity if $B(1) \neq 0$ and $v$ is a large step. If the disturbance $v$ in Eq. (3.1) can be described by Eq. (3.37) we find that Eq. (3.1) can be written as

$$A _ {d} A y (t) = A _ {d} B (u (t) + v (t)) = A _ {d} B y (t) + e (t)$$

Hence

$$A y _ {f} (t) = B u _ {f} (t) + e (t) \tag {3.42}$$

By introducing the filtered signals $y_{f} = A_{d}y$ and $u_{f} = A_{d}u$ we thus obtain a model in which the equation error is e instead of v, where e is significantly smaller than v. For example, if v is a step and $A_{d} = q - 1$ as in Example 3.9, we find that e is zero except at the time where the step in v occurs.

The next example shows that the difficulties encountered in Example 3.9 can be avoided by using a self-tuner with a modified estimator and a modified control design.
