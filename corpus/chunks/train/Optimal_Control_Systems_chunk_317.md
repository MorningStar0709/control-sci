# 6.1 Constrained System

In this section, we consider a practical limitation on controls and states [79]. Let us reconsider the optimal control system (see Chapter 2, Table 2.1).

$$\dot {\mathbf {x}} (t) = \mathbf {f} (\mathbf {x} (t), \mathbf {u} (t), t) \tag {6.1.1}$$

where, $\mathbf{x}(t)$ and $\mathbf{u}(t)$ are the n- and r- dimensional state and control unconstrained variables respectively, and the performance index

$$J = S \left(\mathbf {x} \left(t _ {f}\right), t _ {f}\right) + \int_ {t _ {0}} ^ {t _ {f}} V (\mathbf {x} (t), \mathbf {u} (t), t) d t \tag {6.1.2}$$

with given boundary conditions

$$\mathbf {x} (t = 0) = \mathbf {x} _ {0}, \quad \mathbf {x} (t = t _ {f}) = \mathbf {x} _ {f} \text { is free }, t _ {f} \text { is free }. \tag {6.1.3}$$

The important stages in obtaining optimal control for the previous system are

1. the formulation of the Hamiltonian

$$\mathcal {H} (\mathbf {x} (t), \mathbf {u} (t), \boldsymbol {\lambda} (t), t) = V (\mathbf {x} (t), \mathbf {u} (t), t) + \boldsymbol {\lambda} ^ {\prime} (t) \mathbf {f} (\mathbf {x} (t), \mathbf {u} (t), t), \tag {6.1.4}$$

where, $\pmb{\lambda}(t)$ is the costate variable, and

2. the three relations for control, state and costate as

$$0 = + \left(\frac {\partial \mathcal {H}}{\partial \mathbf {u}}\right) _ {*} \quad \text { control relation }, \tag {6.1.5}\dot {\mathbf {x}} ^ {*} (t) = + \left(\frac {\partial \mathcal {H}}{\partial \boldsymbol {\lambda}}\right) _ {*} \quad \text {state relation, and} \tag {6.1.6}\dot {\boldsymbol {\lambda}} ^ {*} (t) = - \left(\frac {\partial \mathcal {H}}{\partial \mathbf {x}}\right) _ {*} \quad \text {costate relation} \tag {6.1.7}$$

to solve for the optimal values $\mathbf{x}^{*}(t)$ , $\mathbf{u}^{*}(t)$ , and $\boldsymbol{\lambda}^{*}(t)$ , respectively, along with the general boundary condition

$$\left[ \frac {\partial S}{\partial \mathbf {x}} - \boldsymbol {\lambda} (t) \right] _ {* t _ {f}} \delta \mathbf {x} _ {f} + \left[ \mathcal {H} + \frac {\partial S}{\partial t} \right] _ {* t _ {f}} \delta t _ {f} = 0. \tag {6.1.8}$$
