# Example 2.15

We consider the same Example 2.12 with changed performance index

$$J = \frac {1}{2} [ x _ {1} (2) - 4 ] ^ {2} + \frac {1}{2} [ x _ {2} (2) - 2 ] ^ {2} + \frac {1}{2} \int_ {0} ^ {2} u ^ {2} d t \tag {2.7.71}$$

and boundary conditions as

$$\mathbf {x} (0) = [ 1 2 ]; \quad \mathbf {x} (2) = \text { is free. } \tag {2.7.72}$$

Following the procedure illustrated in Table 2.1 (Type (b)), we get the same optimal control, states and costates as given in (2.7.54) and (2.7.55), which are reproduced here for ready reference. Thus

![](image/2cb6a34e3dc6dac3698438c94b047db1d37c6dfcfb0ec531fba67deaab87ad81.jpg)

<details>
<summary>line</summary>

| t | x₁(t) | x₂(t) | u(t) |
| --- | --- | --- | --- |
| 0.0 | 1.0 | 2.0 | -1.5 |
| 0.5 | 1.8 | 1.6 | -1.2 |
| 1.0 | 2.2 | 1.0 | -0.9 |
| 1.5 | 2.5 | 0.6 | -0.6 |
| 2.0 | 2.7 | 0.3 | -0.3 |
| 2.5 | 2.8 | 0.1 | -0.1 |
| 3.0 | 2.9 | 0.0 | 0.0 |
</details>

Figure 2.13 Optimal Control and States for Example 2.14

we have

$$x _ {1} ^ {*} (t) = \frac {C _ {3}}{6} t ^ {3} - \frac {C _ {4}}{2} t ^ {2} + C _ {2} t + C _ {1},x _ {2} ^ {*} (t) = \frac {C _ {3}}{2} t ^ {2} - C _ {4} t + C _ {2},\lambda_ {1} ^ {*} (t) = C _ {3},\lambda_ {2} ^ {*} (t) = - C _ {3} t + C _ {4},u ^ {*} (t) = - \lambda_ {2} (t) = C _ {3} t - C _ {4}. \tag {2.7.73}$$

The only difference is in solving for the constants $C_{1}$ to $C_{4}$ using the given and obtained boundary conditions. Since $t_{f}$ is specified as 2, $\delta t_{f}$ is zero and since $\mathbf{x}(2)$ unspecified, $\delta x_{f}$ is free in the boundary condition (2.7.32), which now reduces to

$$\boldsymbol {\lambda} ^ {*} (t _ {f}) = \left(\frac {\partial S}{\partial \mathbf {x}}\right) _ {* t _ {f}} \tag {2.7.74}$$

where,

$$S (\mathbf {x} (t _ {f})) = \frac {1}{2} [ x _ {1} (2) - 4 ] ^ {2} + \frac {1}{2} [ x _ {2} (2) - 2 ] ^ {2}. \tag {2.7.75}$$

Thus, (2.7.74) becomes

$$\lambda_ {1} ^ {*} (t _ {f}) = \left(\frac {\partial S}{\partial x _ {1}}\right) _ {t _ {f}} \longrightarrow \lambda_ {1} ^ {*} (2) = x _ {1} (2) - 4\lambda_ {2} ^ {*} (t _ {f}) = \left(\frac {\partial S}{\partial x _ {2}}\right) _ {t _ {f}} \longrightarrow \lambda_ {2} ^ {*} (2) = x _ {2} (2) - 2. \tag {2.7.76}$$

Now, we have two initial conditions from (2.7.72) and two final conditions from (2.7.76) to solve for the four constants as

$$C _ {1} = 1, \quad C _ {2} = 2, \quad C _ {3} = \frac {3}{7}, \quad C _ {4} = \frac {4}{7}. \tag {2.7.77}$$

Finally, we have the optimal states, costates and control given as
