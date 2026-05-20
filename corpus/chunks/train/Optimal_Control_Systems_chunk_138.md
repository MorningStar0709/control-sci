# 2.8.3 Stage III: Optimal Control System with Lagrangian Formalism

Here, we consider the standard control system with a plant described by [56]

$$\dot {\mathbf {x}} (t) = \mathbf {f} (\mathbf {x} (t), \mathbf {u} (t), t), \tag {2.8.15}$$

the given boundary conditions as

$$\mathbf {x} (t _ {0}) \text { is fixed and } \mathbf {x} (t _ {f}) \text { is free, } \tag {2.8.16}$$

and the performance index as

$$J (\mathbf {u} (t)) = \int_ {t _ {0}} ^ {t _ {f}} V (\mathbf {x} (t), \mathbf {u} (t), t) d t. \tag {2.8.17}$$

Now, we rewrite the plant equation (2.8.15) as the condition relation (2.8.9) as

$$\mathbf {g} (\mathbf {x} (t), \dot {\mathbf {x}} (t), \mathbf {u} (t), t) = \mathbf {f} (\mathbf {x} (t), \mathbf {u} (t), t) - \dot {\mathbf {x}} (t) = 0. \tag {2.8.18}$$

Then we form the augmented functional out of the performance index (2.8.17) and the condition relation (2.8.18) as

$$J _ {a} (\mathbf {u} (t)) = \int_ {t _ {0}} ^ {t _ {f}} \mathcal {L} (\mathbf {x} (t), \dot {\mathbf {x}} (t), \mathbf {u} (t), \boldsymbol {\lambda} (t), t) d t \tag {2.8.19}$$

where, the Lagrangian $\mathcal{L}$ is given as

$$
\begin{array}{l} \mathcal {L} = \mathcal {L} (\mathbf {x} (t), \dot {\mathbf {x}} (t), \mathbf {u} (t), \boldsymbol {\lambda} (t), t) \\ = V (\mathbf {x} (t), \mathbf {u} (t), t) + \lambda^ {\prime} (t) \left\{\mathbf {f} (\mathbf {x} (t), \mathbf {u} (t), t) - \dot {\mathbf {x}} (t) \right\}. \tag {2.8.20} \\ \end{array}
$$

Now we just use the previous results of Stage II. For optimal condition, we have the set of Euler-Lagrange equations (2.8.12) and (2.8.13) for the augmented functional (2.8.19) given in terms of $\mathbf{x}(t)$ , $\boldsymbol{\lambda}(t)$ , and $\mathbf{u}(t)$ as

$$\boxed {\left(\frac {\partial \mathcal {L}}{\partial \mathbf {x}}\right) _ {*} - \frac {d}{d t} \left(\frac {\partial \mathcal {L}}{\partial \dot {\mathbf {x}}}\right) _ {*} = 0} \text {state equation,} \tag {2.8.21}\boxed {\left(\frac {\partial \mathcal {L}}{\partial \boldsymbol {\lambda}}\right) _ {*} - \frac {d}{d t} \left(\frac {\partial \mathcal {L}}{\partial \dot {\boldsymbol {\lambda}}}\right) _ {*} = 0} \text { costate equation, and } \tag {2.8.22}\boxed {\left(\frac {\partial \mathcal {L}}{\partial \mathbf {u}}\right) _ {*} - \frac {d}{d t} \left(\frac {\partial \mathcal {L}}{\partial \dot {\mathbf {u}}}\right) _ {*} = 0} \text { control equation. } \tag {2.8.23}$$
