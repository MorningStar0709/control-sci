The angle-of-attack α is taken to be the smallest of the following three quantities:

1. Commanded angle of attack $\alpha _ { c }$ ,   
2. Limiting angle of attack $\alpha _ { \mathrm { m a x } }$   
3. Angle of attack $\alpha _ { N \operatorname* { m a x } }$ , yielding limiting normal acceleration $a _ { N }$ max, as computed by iteratively solving the implicit equation

$$a _ {N \max} = C _ {N} (M, \alpha_ {N \max}) Q A / m$$

for αN max. $\alpha _ { N }$

The commanded angle of attack is obtained by iteratively solving the equation

$$a _ {L A} = (Q A / m) [ C _ {N} (M, \alpha_ {c}) \cos \alpha_ {c} - C _ {x} (M, \alpha_ {c}) \sin \alpha_ {c} ] \tag {4.5}$$

for $\alpha _ { c }$ . Here, $a _ { L A }$ is the desired aerodynamic lift acceleration. It is computed from the desired total lift acceleration $a _ { L d }$ by

$$a _ {L A} = a _ {L d} - I _ {g} \mathbf {g} \cdot \mathbf {1} _ {L}, \tag {4.6}$$

where $a _ { L d }$ is computed by the guidance algorithm and $I _ { g }$ is zero if the input guidance parameter is zero or negative, and $I _ { g }$ equals one otherwise. The guidance algorithm also computes the unit lift vector $\mathbf { 1 } _ { L }$ .

Next, (4.1a) and (4.1b) can be numerically integrated using the fourth-order Runge–Kutta integration scheme with a specified time step. Integration is terminated at each dynamic discontinuity (e.g., staging, burnout, or target closest approach), and if necessary, restarted after the discontinuity.

The missile trajectory is integrated in conjunction with the target trajectory. For the state vector at discrete instant i, the following quantities related to the missile motion are computed and saved:

time $t _ { i }$ , position $\mathbf { r } ( t _ { i } )$ , velocity $\mathbf { v } ( t _ { i } )$ , acceleration $\mathbf { a } ( t _ { i } )$ ,

$$\mathbf {f} (t _ {i}) = \left(1 0 \sigma_ {i} - 4 \Delta_ {i} \mu_ {i} + 0. 5 \Delta_ {i} ^ {2} v _ {i}\right) / \Delta_ {i} ^ {3}, \tag {4.7a}\mathbf {g} (t _ {i}) = (- 1 5 \sigma_ {i} + 7 \Delta_ {i} \mu_ {i} - \Delta_ {i} ^ {2} v _ {i}) / \Delta_ {i} ^ {4}, \tag {4.7b}\mathbf {h} (t _ {i}) = (6 \sigma_ {i} - 3 \Delta_ {i} \mu_ {i} + 0. 5 \Delta_ {i} ^ {2} v _ {i}) / \Delta_ {i} ^ {5}, \tag {4.7c}$$

where

$$\sigma_ {i} = \mathbf {r} _ {i + 1} - \mathbf {r} _ {i} - \Delta_ {i} \mathbf {v} _ {i} - 0. 5 \Delta_ {i} ^ {2} \mathbf {a} _ {i},\mu_ {i} = \mathbf {v} _ {i + 1} - \mathbf {v} _ {i} - \Delta_ {i} \mathbf {a} _ {i},v _ {i} = \mathbf {a} _ {i + 1} - \mathbf {a} _ {i},\Delta_ {i} = t _ {i + 1} - t _ {i}.$$
