# 2.8.2 Stage II: Optimization of a Functional with Condition

Consider the optimization of a functional

$$J = \int_ {t _ {0}} ^ {t _ {f}} V (\mathbf {x} (t), \dot {\mathbf {x}} (t), t) d t \tag {2.8.7}$$

with given boundary values as

$$\mathbf {x} (t _ {0}) \text { fixed and } \mathbf {x} (t _ {f}) \text { free, } \tag {2.8.8}$$

and the condition relation

$$\mathbf {g} (\mathbf {x} (t), \dot {\mathbf {x}} (t), t) = 0. \tag {2.8.9}$$

Here, the condition $(2.8.9)$ is absorbed by forming the augmented functional

$$J _ {a} = \int_ {t _ {0}} ^ {t _ {f}} \mathcal {L} (\mathbf {x} (t), \dot {\mathbf {x}} (t), \boldsymbol {\lambda} (t), t) d t \tag {2.8.10}$$

where, $\lambda(t)$ is the Lagrange multiplier (also called the costate function), and L is the Lagrangian given by

$$\boxed {\mathcal {L} (\mathbf {x} (t), \dot {\mathbf {x}} (t), \boldsymbol {\lambda} (t), t) = V (\mathbf {x} (t), \dot {\mathbf {x}} (t), t) + \boldsymbol {\lambda} ^ {\prime} (t) \mathbf {g} (\mathbf {x} (t), \dot {\mathbf {x}} (t), t).} \tag {2.8.11}$$

Now, we just use the results of the previous Stage I for the augmented functional (2.8.10) except its integrand is L instead of V. For optimal condition, we have the Euler-Lagrange equation (2.8.3) for the augmented functional (2.8.10) given in terms of $\mathbf{x}(t)$ and $\boldsymbol{\lambda}(t)$ as

$$
\begin{array}{l} \left(\frac {\partial \mathcal {L}}{\partial \mathbf {x}}\right) _ {*} - \frac {d}{d t} \left(\frac {\partial \mathcal {L}}{\partial \dot {\mathbf {x}}}\right) _ {*} = 0 \\ \overline {{\left(\frac {\partial \mathcal {L}}{\partial \boldsymbol {\lambda}}\right) _ {*} - \frac {d}{d t} \left(\frac {\partial \mathcal {L}}{\partial \dot {\boldsymbol {\lambda}}}\right) _ {*} = 0}} \\ \end{array}
$$

state equation and (2.8.12)

costate equation. (2.8.13)

Let us note from (2.8.11) that the Lagrangian $\mathcal{L}$ is independent of $\dot{\lambda}^{*}(t)$ and that the Euler-Lagrange equation (2.8.13) for the costate $\lambda(t)$ is nothing but the constraint relation (2.8.9). The general boundary
