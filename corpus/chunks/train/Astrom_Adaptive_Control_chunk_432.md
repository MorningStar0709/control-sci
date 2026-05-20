# The Averaged Equations

The analysis of the dynamics of adaptive systems is generally quite complicated because the complete system is often of high order. Analysis of a direct algorithm for a discrete-time second-order system with four unknown parameters using a gradient method leads to a difference equation of order 8 (two states of the system, four parameters, and two difference equations to generate the regression variables). Ten more equations are obtained if a least-squares estimation algorithm is used.

Because of the special properties of adaptive systems, however, there is an approximate method that will simplify the analysis considerably. The basic idea is that the parameters change much more slowly than the other variables of the system. This property is intrinsic to the adaptive algorithms. If this were not the case, we could hardly justify using the notion of parameters.

To describe the averaging methods, consider the adaptive system described by Eqs. (6.1) and (6.2). The rate of change of the parameter $\hat{\theta}$ can be made arbitrarily small by choosing the adaptation gain $\gamma$ sufficiently small. For simplicity we use the simple gradient algorithm

$$\frac {d \hat {\theta}}{d t} = \gamma \varphi (\vartheta , \xi) e (\vartheta , \xi) \tag {6.48}$$

The product $\varphi e$ on the right-hand side depends on $\vartheta$ and $\xi$ , where $\vartheta = \vartheta(\hat{\theta})$ varies slowly and $\xi$ varies fast. The key idea in the averaging method is to approximate the product $\varphi e$ by

$$G (\hat {\theta}) = \operatorname{avg} \left\{\varphi (\vartheta (\hat {\theta}), \xi (\vartheta (\hat {\theta}), t)) e (\vartheta (\hat {\theta}), \xi (\vartheta (\hat {\theta}), t)) \right\}$$

where $\operatorname{avg}\{\cdot\}$ denotes the average and $\xi(\vartheta(\hat{\theta}),t)$ is computed under the assumption that the parameters $\hat{\theta}$ are constant. The average can be computed in many ways. Typical examples are
