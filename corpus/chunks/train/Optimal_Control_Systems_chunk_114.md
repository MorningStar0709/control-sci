where the partials are evaluated at the optimal (\*) condition. Next, since the independent control variation $\delta\mathbf{u}(t)$ is arbitrary, the coefficient of the control variation $\delta\mathbf{u}(t)$ in (2.7.18) should be set to zero. That is

$$\left(\frac {\partial \mathcal {L}}{\partial \mathbf {u}}\right) _ {*} = 0. \tag {2.7.20}$$

Finally, the first variation (2.7.18) reduces to

$$\mathcal {L} ^ {*} | _ {t _ {f}} \delta t _ {f} + \left. \left[ \left(\frac {\partial \mathcal {L}}{\partial \dot {\mathbf {x}}}\right) _ {*} ^ {\prime} \delta \mathbf {x} (t) \right] \right| _ {t _ {f}} = 0. \tag {2.7.21}$$

Let us note that the condition (or plant) equation (2.7.1) can be written in terms of the Lagrangian (2.7.12) as

$$\left(\frac {\partial \mathcal {L}}{\partial \boldsymbol {\lambda}}\right) _ {*} = 0. \tag {2.7.22}$$

![](image/611e3bff5be29dd5869275e941124f32f8dfd04198af9127dd345bcf35db04e3.jpg)  
Figure 2.8 Final-Point Condition with a Moving Boundary $\theta(t)$

In order to convert the expression containing $\delta\mathbf{x}(t)$ in (2.7.21) into an expression containing $\delta\mathbf{x}_{f}$ (see Figure 2.8), we note that the slope of $\dot{\mathbf{x}}^{*}(t)+\delta\dot{\mathbf{x}}(t)$ at $t_{f}$ is approximated as

$$\dot {\mathbf {x}} ^ {*} (t _ {f}) + \delta \dot {\mathbf {x}} (t _ {f}) \approx \frac {\delta \mathbf {x} _ {f} - \delta \mathbf {x} (t _ {f})}{\delta t _ {f}} \tag {2.7.23}$$

which is rewritten as

$$\delta \mathbf {x} _ {f} = \delta \mathbf {x} (t _ {f}) + \left\{\dot {\mathbf {x}} ^ {*} (t) + \delta \dot {\mathbf {x}} (t) \right\} \delta t _ {f} \tag {2.7.24}$$

and retaining only the linear (in $\delta$ ) terms in the relation (2.7.24), we have

$$\delta \mathbf {x} (t _ {f}) = \delta \mathbf {x} _ {f} - \dot {\mathbf {x}} ^ {*} (t _ {f}) \delta t _ {f}. \tag {2.7.25}$$

Using $(2.7.25)$ in the boundary condition $(2.7.21)$ , we have the general boundary condition in terms of the Lagrangian as

$$\left. \left[ \mathcal {L} ^ {*} - \left(\frac {\partial \mathcal {L}}{\partial \dot {\mathbf {x}}}\right) _ {*} ^ {\prime} \dot {\mathbf {x}} (t) \right] \right| _ {t _ {f}} \delta t _ {f} + \left. \left(\frac {\partial \mathcal {L}}{\partial \dot {\mathbf {x}}}\right) _ {*} ^ {\prime} \right| _ {t _ {f}} \delta \mathbf {x} _ {f} = 0. \tag {2.7.26}$$
