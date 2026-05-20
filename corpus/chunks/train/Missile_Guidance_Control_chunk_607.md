$$- \mathbf {V} _ {g} \Delta t = \mathbf {V} _ {m} \Delta t - \mathbf {V} _ {c} \Delta t = d \mathbf {r}. \tag {6.189}$$

To obtain the corresponding velocity changes, it is noted that during the time interval $\Delta t$ the actual missile is acted upon by the sum of the thrust acceleration vector aT and gravity g. Thus, the missile experiences a change in velocity given by

$$\Delta \mathbf {V} _ {m} = \mathbf {a} _ {T} \Delta t + \mathbf {g} \Delta t. \tag {6.190}$$

The corresponding change in correlated velocity is $\mathbf { g } \Delta t$ only, since the correlated missile is assumed to be in free fall. An additional change in ${ \bf V } _ { c }$ must be included, however, in order to accompany the displacement given by (6.189). If the target location and total time of flight are to remain fixed during this process (6.188) indicates that ${ \bf V } _ { c }$ must change by an amount equal to the product of the Q-matrix with the displacement (6.189). Therefore, the total change in $\mathbf { V } _ { c }$ for the two steps is

$$\Delta \mathbf {V} _ {m} = \mathbf {g} \Delta t + Q (- \mathbf {V} _ {g} \Delta t). \tag {6.191}$$

The last step in the derivation consists in the computation of the change in $\mathbf { V } _ { g }$ as the difference between $\Delta \mathbf { V } _ { c }$ and $\Delta \mathbf { V } _ { m }$ . There results from (6.190) and (6.191) the relation

$$\mathbf {V} _ {g} \Delta t = \Delta \mathbf {V} _ {c} - \Delta \mathbf {V} _ {m} = - \mathbf {a} _ {T} \Delta t - Q \mathbf {V} _ {g} \Delta t. \tag {6.192}$$

Dividing both sides of (6.192) by $\Delta t$ yields, in the limit as $\Delta t \to 0$ , the desired differential equation (6.178). The essential ingredients in this derivation are the free-fall property of $\mathbf { V } _ { c }$ and (6.188), relating changes in $\mathbf { V } _ { c }$ to position increments. The former property permits the cancellation of gravity in subtracting (6.190) from (6.191), while the latter allows a positional change to be translated into a corresponding change in $\mathbf { V } _ { g }$ . Any alternative definition of ${ \bf V } _ { c }$ that preserves these properties (with an appropriate redefinition of the Q-matrix) leaves (6.178) as a valid relation. Thus, other applications of these concepts are possible. The missile positional variation $\Delta r _ { m }$ can be approximated by

$$\Delta r _ {m} \cong - \int_ {0} ^ {t} \Delta \mathbf {V} _ {g} d t. \tag {6.193}$$
