# Model-Following

The Diophantine equation (3.4) determines only the polynomials R and S. Other conditions must be introduced to also determine the polynomial T in the controller (3.2). To do this, we will require that the response from the command signal $u_{c}$ to the output be described by the dynamics

$$A _ {m} y _ {m} (t) = B _ {m} u _ {c} (t) \tag {3.5}$$

It then follows from Eqs. (3.3) that the following condition must hold:

$$\frac {B T}{A R + B S} = \frac {B T}{A _ {c}} = \frac {B _ {m}}{A _ {m}} \tag {3.6}$$

This model-following condition says that the response of the closed-loop system to command signals is as specified by the model (3.5). Whether model-following can be achieved depends on the model, the system, and the command signal. If it is possible to make the error equal to zero for all command signals, then perfect model-following is achieved.

The consequences of the model-following condition will now be explored. Equation (3.6) implies that there are cancellations of factors of BT and $A_{c}$ . Factor the B polynomial as

$$\boldsymbol {B} = \boldsymbol {B} ^ {+} \boldsymbol {B} ^ {-} \tag {3.7}$$

where $B^{+}$ is a monic polynomial whose zeros are stable and so well damped that they can be canceled by the controller and $B^{-}$ corresponds to unstable or poorly damped factors that cannot be canceled. It thus follows that $B^{-}$ must be a factor of $B_{m}$ . Hence

$$\boldsymbol {B} _ {m} = \boldsymbol {B} ^ {-} \boldsymbol {B} _ {m} ^ {\prime} \tag {3.8}$$

Since $B^{+}$ is canceled, it must be a factor of $A_{c}$ . Furthermore, it follows from Eq. (3.6) that $A_{m}$ must also be a factor of $A_{c}$ . The closed-loop characteristic polynomial thus has the form

$$\boldsymbol {A} _ {c} = \boldsymbol {A} _ {o} \boldsymbol {A} _ {m} \boldsymbol {B} ^ {+} \tag {3.9}$$

Since $B^{+}$ is a factor of $B$ and $A_{c}$ , it follows from Eq. (3.4) that it also divides $R$ . Hence

$$R = R ^ {\prime} B ^ {+} \tag {3.10}$$

and the Diophantine equation (3.4) reduces to

$$A R ^ {\prime} + B ^ {-} S = A _ {o} A _ {m} = A _ {c} ^ {\prime} \tag {3.11}$$

Introducing Eqs. (3.7), (3.8), and (3.9) into Eq. (3.6) gives

$$T = A _ {o} B _ {m} ^ {\prime} \tag {3.12}$$
