# 7.7.3 Bryson’s rule

Tuning Q and R is more art than science, but Bryson’s rule[9] provides a good starting point. Bryson’s rule sets Q’s diagonal to the inverse square of the acceptable state excursions and R’s diagonal to the inverse square of the acceptable control efforts. The nondiagonal elements are zero.

$$\mathbf {Q} = \operatorname{diag} \left(\frac {\rho}{\mathbf {x} _ {m a x} ^ {2}}\right) \quad \mathbf {R} = \operatorname{diag} \left(\frac {1}{\mathbf {u} _ {m a x} ^ {2}}\right)$$

where $\mathbf { x } _ { m a x }$ is the vector of acceptable state excursions, $\mathbf { u } _ { m a x }$ is the vector of acceptable control efforts, and $\rho$ is a weighting factor that adjusts the balance between state excursion and control effort penalty. Small values of $\rho$ penalize control effort while large values of $\rho$ penalize state excursions. Large values would be chosen in applications like fighter jets where performance is necessary. Spacecrafts would use small values to conserve their limited fuel supply.
