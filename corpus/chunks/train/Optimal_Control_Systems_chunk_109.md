We now illustrate the procedure in the following steps. Also, we first introduce the Lagrangian and then, a little later, introduce the Hamiltonian. Let us first list the various steps and then describe the same in detail.

- Step 1: Assumption of Optimal Conditions   
- Step 2: Variations of Control and State Vectors   
- Step 3: Lagrange Multiplier

\- Step 4: Lagrangian

\- Step 5: First Variation

\- Step 6: Condition for Extrema

\- Step 7: Hamiltonian

\- Step 1: Assumptions of Optimal Conditions: We assume optimum values $\mathbf{x}^{*}(t)$ and $\mathbf{u}^{*}(t)$ for state and control, respectively. Then

$$J \left(\mathbf {u} ^ {*} (t)\right) = \int_ {t _ {0}} ^ {t _ {f}} \left[ V \left(\mathbf {x} ^ {*} (t), \mathbf {u} ^ {*} (t), t\right) + \frac {d S \left(\mathbf {x} ^ {*} (t) , t\right)}{d t} \right] d t\dot {\mathbf {x}} ^ {*} (\mathbf {t}) = \mathbf {f} \left(\mathbf {x} ^ {*} (t), \mathbf {u} ^ {*} (t), t\right). \tag {2.7.7}$$

\- Step 2: Variations of Controls and States: We consider the variations (perturbations) in control and state vectors as (see Figure 2.7)

$$\mathbf {x} (t) = \mathbf {x} ^ {*} (t) + \delta \mathbf {x} (t); \quad \mathbf {u} (t) = \mathbf {u} ^ {*} (t) + \delta \mathbf {u} (t). \tag {2.7.8}$$

![](image/bdbad9c6795535a4402a07eba3def3e3ad4a3b65b0e47fa7e07930d5df888e4f.jpg)

<details>
<summary>line</summary>

| t | x*(t) | x*(t)+ δx(t) |
| --- | --- | --- |
| 0 | x₀ | x₀ |
| t₀ | x₀ | x₀ |
| t_f | x_f | x_f |
| t_f + δt_f | x_f+δx(t_f) | x_f+δx(t_f) |
| t | x_f+δx(t) | x_f |
</details>

Figure 2.7 Free-Final Time and Free-Final State System

Then, the state equation (2.7.1) and the performance index (2.7.5) become

$$\dot {\mathbf {x}} ^ {*} (\mathbf {t}) + \delta \dot {\mathbf {x}} (\mathbf {t}) = \mathbf {f} (\mathbf {x} ^ {*} (\mathbf {t}) + \delta \mathbf {x} (\mathbf {t}), \mathbf {u} ^ {*} (\mathbf {t}) + \delta \mathbf {u} (\mathbf {t}), \mathbf {t})J (\mathbf {u} (t)) = \int_ {t _ {0}} ^ {t _ {f} + \delta t _ {f}} \left[ V (\mathbf {x} ^ {*} (t) + \delta \mathbf {x} (t), \mathbf {u} ^ {*} (t) + \delta \mathbf {u} (t), t) + \frac {d S}{d t} \right] d t \tag {2.7.9}$$

\- Step 3: Lagrange Multiplier: Introducing the Lagrange multiplier vector $\lambda(t)$ (also called costate vector) and using (2.7.6), we introduce the augmented performance index at the optimal condition as
