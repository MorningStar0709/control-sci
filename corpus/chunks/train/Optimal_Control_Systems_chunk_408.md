$$\boxed {\mathbf {u} ^ {*} (t) = - D E Z \{\mathbf {q} ^ {*} (t) \} = - D E Z \{\mathbf {B} ^ {\prime} \boldsymbol {\lambda} ^ {*} (t) \}} \tag {7.4.10}$$

or component wise,

$$u _ {j} ^ {*} (t) = - d e z \{q _ {j} ^ {*} (t) \} = - d e z \{\mathbf {b} _ {j} ^ {\prime} \lambda^ {*} (t) \} \tag {7.4.11}$$

where, $j = 1, 2, \ldots, r$ . The optimal control (7.4.10) in terms of the dead-zone (dez) function is shown in Figure 7.24.

![](image/c58fe1efb65c241ca92ab4f3425ce4a178d748fc534ebabbe35698018c657024.jpg)

<details>
<summary>text_image</summary>

-q*
-1
+1
-1
u*
</details>

Figure 7.24 Optimal Control as Dead-Zone Function

\- Step 3: Costate Functions: The costate functions $\lambda^{*}(t)$ are given in terms of the Hamiltonian as

$$\dot {\boldsymbol {\lambda}} ^ {*} (t) = - \frac {\partial \mathcal {H}}{\partial \mathbf {x}} = - \mathbf {A} ^ {\prime} \boldsymbol {\lambda} ^ {*} (t) \tag {7.4.12}$$

the solution of which is

$$\boldsymbol {\lambda} ^ {*} (t) = \epsilon^ {- \mathbf {A} ^ {\prime} t} \boldsymbol {\lambda} (0). \tag {7.4.13}$$

Depending upon the nature of the function $\mathbf{q}^{*}(t)$ , we can classify it as normal fuel-optimal control (NFOC) system, if $|\mathbf{q}^{*}(t)| = 1$ only at switch times as shown in Figure 7.25 or singular fuel-optimal control (SFOC) system, if $|\mathbf{q}^{*}(t)| = 1$ as shown in Figure 7.26, for some $t \in [T_{1}, T_{2}]$ .

![](image/2ae0cdbabf98ebdf37853ecb376d583c881e939fb7a1a363b7090ff845e9012c.jpg)

<details>
<summary>line</summary>

| t | u*(t) | q*(t) |
| --- | --- | --- |
| t0 | +1 | -1 |
| t1 | 0 | -1 |
| t2 | +1 | -1 |
| t3 | 0 | -1 |
| t4 | +1 | 0 |
| t5 | 0 | 0 |
| t6 | +1 | -1 |
| tf | 0 | -1 |
</details>

Figure 7.25 Normal Fuel-Optimal Control System

\- Step 4: Normal Fuel-Optimal Control System: We first derive the necessary conditions for the fuel-optimal system to be singular and then translate these into sufficient conditions for the system to be normal, that is, the negation of the conditions for singular is taken as that for normal.

For the fuel-optimal system to be singular, it is necessary that in the system interval $[0, t_{f}]$ , there is at least one subinterval $[T_{1}, T_{2}]$ for which

$$\mathbf {q} ^ {*} (t) = 1 \forall t \in [ T _ {1}, T _ {2} ]. \tag {7.4.14}$$

Using (7.4.9), the previous condition becomes

$$| \mathbf {q} ^ {*} (t) | = | \mathbf {B} ^ {\prime} \boldsymbol {\lambda} ^ {*} (t) | = 1. \tag {7.4.15}$$
