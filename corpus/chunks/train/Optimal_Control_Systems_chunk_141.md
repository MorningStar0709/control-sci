# Free-Final Point System with Final Cost Function

This problem is an extension of the problem in Stage IV, with the addition of final cost function. We summarize the result risking the repetition of some of the equations. Let the plant be described as

$$\dot {\mathbf {x}} (t) = \mathbf {f} (\mathbf {x} (t), \mathbf {u} (t), t) \tag {2.8.37}$$

and the performance index be

$$J (\mathbf {u} (t)) = S \left(\mathbf {x} \left(t _ {f}\right), t _ {f}\right) + \int_ {t _ {0}} ^ {t _ {f}} V (\mathbf {x} (t), \mathbf {u} (t), t) d t \tag {2.8.38}$$

along with the boundary conditions

$$\mathbf {x} (t _ {0}) \text { is fixed and } \mathbf {x} (t _ {f}) \text { is free. } \tag {2.8.39}$$

Now, if we rewrite the performance index (2.8.38) to absorb the final cost function S within the integrand, then the results of Stage III can be used to get the optimal conditions. Thus we rewrite (2.8.38) as

$$J _ {1} (\mathbf {u} (t)) = \int_ {t _ {0}} ^ {t _ {f}} \left[ V (\mathbf {x} (t), \mathbf {u} (t), t) + \left(\frac {\partial S}{\partial \mathbf {x}}\right) ^ {\prime} \dot {\mathbf {x}} (t) + \frac {\partial S}{\partial t} \right] d t. \tag {2.8.40}$$

Now we repeat the results of Stage III except for the modification of the final condition equation (2.8.34). Thus the state, costate and control equations are

$$\dot {\mathbf {x}} ^ {*} (t) = + \left(\frac {\partial \mathcal {H}}{\partial \boldsymbol {\lambda}}\right) _ {*} \mid \text { state equation } \tag {2.8.41}\dot {\boldsymbol {\lambda}} ^ {*} (t) = - \left(\frac {\partial \mathcal {H}}{\partial \mathbf {x}}\right) _ {*} \mid \text { costate equation } \tag {2.8.42}\boxed {0 = + \left(\frac {\partial \mathcal {H}}{\partial \mathbf {u}}\right) _ {*} c o n t r o l e q u a t i o n} \tag {2.8.43}$$

and the final boundary condition is

$$\left[ \mathcal {H} + \frac {\partial S}{\partial t} \right] _ {* t _ {f}} \delta t _ {f} + \left[ \left(\frac {\partial S}{\partial \mathbf {x}}\right) - \boldsymbol {\lambda} (t) \right] _ {* t _ {f}} ^ {\prime} \delta \mathbf {x} _ {f} = 0. \tag {2.8.44}$$

The sufficient condition for optimum is

$$\boxed {\left(\frac {\partial^ {2} \mathcal {H}}{\partial \mathbf {u} ^ {2}}\right) _ {*} > 0} \text { for minimum and } \tag {2.8.45}\boxed {\left(\frac {\partial^ {2} \mathcal {H}}{\partial \mathbf {u} ^ {2}}\right) _ {*} < 0} \text { for maximum. } \tag {2.8.46}$$

The state, costate, and control equations (2.8.41) to (2.8.43) are solved along with the given initial condition (2.8.39) and the final condition (2.8.44), thus this formulation leads us to a TPBVP.
