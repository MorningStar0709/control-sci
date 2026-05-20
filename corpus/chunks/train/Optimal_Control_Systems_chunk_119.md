# 2.7 Variational Approach to Optimal Control Systems

\- Type (d): Free-Final Time and Dependent Free-Final State System: If $t_f$ and $\mathbf{x}(t_f)$ are related such that $\mathbf{x}(t_f)$ lies on a moving curve $\theta(t)$ as shown in Figure 2.8, then

$$\mathbf {x} (t _ {f}) = \boldsymbol {\theta} (t _ {f}) \quad \text { and } \quad \delta \mathbf {x} _ {f} \approx \dot {\boldsymbol {\theta}} (t _ {f}) \delta t _ {f}. \tag {2.7.35}$$

Using (2.7.35), the boundary condition (2.7.32) for the optimal condition becomes

$$\left[ \left(\mathcal {H} + \frac {\partial S}{\partial t}\right) _ {*} + \left(\frac {\partial S}{\partial \mathbf {x}} - \boldsymbol {\lambda} ^ {*} (t)\right) _ {*} ^ {\prime} \dot {\boldsymbol {\theta}} (t) \right] _ {t _ {f}} \delta t _ {f} = 0. \tag {2.7.36}$$

Since $t_f$ is free, $\delta t_f$ is arbitrary and hence the coefficient of $\delta t_f$ in (2.7.36) is zero. That is

$$\left[ \left(\mathcal {H} + \frac {\partial S}{\partial t}\right) _ {*} + \left(\frac {\partial S}{\partial \mathbf {x}} - \boldsymbol {\lambda} ^ {*} (t)\right) _ {*} ^ {\prime} \dot {\boldsymbol {\theta}} (t) \right] _ {t _ {f}} = 0. \tag {2.7.37}$$

\- Type (e): Free-Final Time and Independent Free-Final State: If $t_f$ and $\mathbf{x}(t_f)$ are not related, then $\delta t_f$ and $\delta \mathbf{x}_f$ are unrelated, and the boundary condition (2.7.32) at the optimal condition becomes

$$\left(\mathcal {H} + \frac {\partial S}{\partial t}\right) _ {* t _ {f}} = 0 \tag {2.7.38}\left(\frac {\partial S}{\partial \mathbf {x}} - \boldsymbol {\lambda} ^ {*} (t)\right) _ {* t _ {f}} = 0. \tag {2.7.39}$$
