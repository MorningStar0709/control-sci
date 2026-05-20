# 6.2.1 Summary of Pontryagin Principle

The Pontryagin Principle is now summarized below. Given the plant as

$$\dot {\mathbf {x}} (t) = \mathbf {f} (\mathbf {x} (t), \mathbf {u} (t), t), \tag {6.2.14}$$

the performance index as

$$J = S (\mathbf {x} (t _ {f}), t _ {f}) + \int_ {t _ {0}} ^ {t _ {f}} V (\mathbf {x} (t), \mathbf {u} (t), t) d t, \tag {6.2.15}$$

and the boundary conditions as

$$\mathbf {x} (t _ {0}) = \mathbf {x} _ {0} \text { and } t _ {f}, \quad \mathbf {x} (t _ {f}) = \mathbf {x} _ {f} \text { are free }, \tag {6.2.16}$$

to find the optimal control, form the Pontryagin H function

$$\mathcal {H} (\mathbf {x} (t), \mathbf {u} (t), \boldsymbol {\lambda} (t), t) = V (\mathbf {x} (t), \mathbf {u} (t), t) + \boldsymbol {\lambda} ^ {\prime} (t) \mathbf {f} (\mathbf {x} (t), \mathbf {u} (t), t), \tag {6.2.17}$$

minimize $\mathcal{H}$ w.r.t. $\mathbf{u}(t)(\leq \mathbf{U})$ as

$$\mathcal {H} (\mathbf {x} ^ {*} (t), \mathbf {u} ^ {*} (t), \boldsymbol {\lambda} ^ {*} (t), t) \leq \mathcal {H} (\mathbf {x} ^ {*} (t), \mathbf {u} (t), \boldsymbol {\lambda} ^ {*} (t), t), \tag {6.2.18}$$

and solve the set of 2n state and costate equations

$$\dot {\mathbf {x}} ^ {*} (t) = \left(\frac {\partial \mathcal {H}}{\partial \boldsymbol {\lambda}}\right) _ {*} \text { and } \dot {\boldsymbol {\lambda}} ^ {*} (t) = - \left(\frac {\partial \mathcal {H}}{\partial \mathbf {x}}\right) _ {*} \tag {6.2.19}$$

Table 6.1 Summary of Pontryagin Minimum Principle
