# 2.8 Summary of Variational Approach

than minimized and hence it is called Pontryagin Maximum Principle. For this reason, the Hamiltonian is also sometimes called Pontryagin H-function. Let us note that minimization of the performance index J is equivalent to the maximization of -J. Then, if we define the Hamiltonian as

$$\mathcal {H} (\mathbf {x} (t), \mathbf {u} (t), \boldsymbol {\lambda} (t), t) = - V (\mathbf {x} (t), \mathbf {u} (t), t) + \hat {\boldsymbol {\lambda}} ^ {\prime} (t) \mathbf {f} (\mathbf {x} (t), \mathbf {u} (t), t) \tag {2.8.51}$$

we have Maximum Principle. Further discussion on Pontryagin Principle is given in Chapter 6.

5. Hamiltonian at the Optimal Condition: At the optimal condition the Hamiltonian can be written as

$$
\begin{array}{l} \mathcal {H} ^ {*} = \mathcal {H} ^ {*} (\mathbf {x} ^ {*} (t), \mathbf {u} ^ {*} (t), \boldsymbol {\lambda} ^ {*} (t), t) \\ \frac {d \mathcal {H} ^ {*}}{d t} = \frac {d \mathcal {H} ^ {*}}{d t} \\ = \left(\frac {\partial \mathcal {H}}{\partial \mathbf {x}}\right) _ {*} ^ {\prime} \dot {\mathbf {x}} ^ {*} (t) + \left(\frac {\partial \mathcal {H}}{\partial \boldsymbol {\lambda}}\right) _ {*} ^ {\prime} \dot {\boldsymbol {\lambda}} ^ {*} (t) + \left(\frac {\partial \mathcal {H}}{\partial \mathbf {u}}\right) _ {*} ^ {\prime} \dot {\mathbf {u}} ^ {*} (t) \\ + \left(\frac {\partial \mathcal {H}}{\partial t}\right) _ {*} \tag {2.8.52} \\ \end{array}
$$

Using the state, costate and control equations (2.8.30) to (2.8.32) in the previous equation, we get

$$\left(\frac {d \mathcal {H}}{d t}\right) _ {*} = \left(\frac {\partial \mathcal {H}}{\partial t}\right) _ {*}. \tag {2.8.53}$$

We observe that along the optimal trajectory, the total derivative of H w.r.t. time is the same as the partial derivative of H w.r.t. time. If H does not depend on t explicitly, then

$$\boxed {\left. \frac {d \mathcal {H}}{d t} \right| _ {*} = 0} \tag {2.8.54}$$

and H is constant w.r.t. the time t along the optimal trajectory.

6. Two-Point Boundary Value Problem (TPBVP): As seen earlier, the optimal control problem of a dynamical system leads to a TPBVP.

![](image/84a5bde79ca7e18227c0bac337428652968e929abf120c3babdd7860fd7ad6a8.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Open-Loop Optimal Controller"] -->|u*(t)| B["Plant"]
    B -->|x*(t)| C
```
</details>

Figure 2.15 Open-Loop Optimal Control
