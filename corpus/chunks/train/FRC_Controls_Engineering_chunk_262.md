# Theorem 9.2.1 — Luenberger observer.

$$\dot {\hat {\mathbf {x}}} = \mathbf {A} \hat {\mathbf {x}} + \mathbf {B} \mathbf {u} + \mathbf {L} (\mathbf {y} - \hat {\mathbf {y}}) \tag {9.1}\hat {\mathbf {y}} = \mathbf {C} \hat {\mathbf {x}} + \mathbf {D} \mathbf {u} \tag {9.2}\hat {\mathbf {x}} _ {k + 1} = \mathbf {A} \hat {\mathbf {x}} _ {k} + \mathbf {B} \mathbf {u} _ {k} + \mathbf {L} (\mathbf {y} _ {k} - \hat {\mathbf {y}} _ {k}) \tag {9.3}\hat {\mathbf {y}} _ {k} = \mathbf {C} \hat {\mathbf {x}} _ {k} + \mathbf {D} \mathbf {u} _ {k} \tag {9.4}$$

A system matrix xˆ state estimate vector   
B input matrix u input vector   
C output matrix y output vector   
D feedthrough matrix yˆ output estimate vector   
L estimator gain matrix

<table><tr><td>Matrix</td><td>Rows × Columns</td><td>Matrix</td><td>Rows × Columns</td></tr><tr><td>A</td><td>states × states</td><td> $\hat{x}$ </td><td>states × 1</td></tr><tr><td>B</td><td>states × inputs</td><td>u</td><td>inputs × 1</td></tr><tr><td>C</td><td>outputs × states</td><td>y</td><td>outputs × 1</td></tr><tr><td>D</td><td>outputs × inputs</td><td> $\hat{y}$ </td><td>outputs × 1</td></tr><tr><td>L</td><td>states × outputs</td><td></td><td></td></tr></table>

Table 9.1: Luenberger observer matrix dimensions

Variables denoted with a hat are estimates of the corresponding variable. For example, xˆ is the estimate of the true state x.

Notice that a Luenberger observer has an extra term in the state evolution equation. This term uses the difference between the estimated outputs and measured outputs to steer the estimated state toward the true state. L approaching $\mathbf { C } ^ { + }$ trusts the measurements more while L approaching 0 trusts the model more.

![](image/d4fd5c9e6e8f9363fbe9d65eefdf07971cabfa1e0378921510cd60eaeac80c82.jpg)

Using an estimator forfeits the performance guarantees from earlier,[3] but the responses are still generally very good if the process and measurement noises are small enough.

A Luenberger observer combines the prediction and update steps of an estimator. To run them separately, use the equations in theorem 9.2.2 instead.
