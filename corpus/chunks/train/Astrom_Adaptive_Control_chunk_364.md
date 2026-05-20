# EXAMPLE 5.18 Adaptive stabilization by backstepping

Consider the system

$$\frac {d x _ {1}}{d t} = x _ {2} + \theta f (x _ {1})\frac {d x _ {2}}{d t} = x _ {3}\frac {d x _ {3}}{d t} = u$$

where $f$ is a known function and $\theta$ an unknown parameter. We derive a control law that stabilizes the system when the parameter $\theta$ is unknown. Introduce a new state variable $\xi_1 = x_1$ . We write the derivative of $\xi_1$ as a sum of terms in which one of them depends on known quantities only. For this purpose we introduce the parameter estimate $\hat{\theta}$ and the error $\tilde{\theta} = \theta - \hat{\theta}$ . The derivative of $\xi_1$ then becomes

$$\frac {d \xi_ {1}}{d t} = - \xi_ {1} + \xi_ {1} + x _ {2} + \hat {\theta} f (\xi_ {1}) + \bar {\theta} f (\xi_ {1})$$

Introduce the next state variable $\xi_{2}$ as

$$\xi_ {2} = x _ {2} + a _ {1} (\xi_ {1}, \hat {\theta})$$

where

$$a _ {1} \left(\xi_ {1}, \hat {\theta}\right) = \xi_ {1} + \hat {\theta} f \left(\xi_ {1}\right) \tag {5.94}$$

The differential equation for $\xi_{1}$ can then be written as

$$\frac {d \xi_ {1}}{d t} = - \xi_ {1} + \xi_ {2} + \tilde {\theta} f \tag {5.95}$$

We now proceed to rewrite the derivative of $\xi_{2}$ as a sum of two terms in which the first depends only on $\xi_{1},\xi_{2}$ , and $\hat{\theta}$ . Hence

$$\frac {d \xi_ {2}}{d t} = \frac {d x _ {2}}{d t} + \frac {\partial a _ {1}}{\partial \xi_ {1}} \cdot \frac {d \xi_ {1}}{d t} + \frac {\partial a _ {1}}{\partial \hat {\theta}} \cdot \frac {d \hat {\theta}}{d t}$$

Equation (5.95) gives the desired separation of terms in $d\xi_{1}/dt$ . Some work is required to obtain a similar expression for $d\hat{\theta}/dt$ . We have

$$\frac {d \xi_ {2}}{d t} = x _ {3} + \frac {\partial a _ {1}}{\partial \xi_ {1}} (- \xi_ {1} + \xi_ {2} + \bar {\theta} f) + \frac {\partial a _ {1}}{\partial \hat {\theta}} \cdot \frac {d \hat {\theta}}{d t} \tag {5.96}$$

Following the idea of backstepping, we consider $x_{3}$ to be a control variable that can be chosen freely. The Lyapunov function

$$2 V = \xi_ {1} ^ {2} + \xi_ {2} ^ {2} + \tilde {\theta} ^ {2}$$

can be used to find a control law and an adaptation law that stabilizes the error equation for variables $\xi_{1}$ and $\xi_{2}$ . After some calculations we find that the derivative of V is given by
