in which $a = \operatorname* { m i n } ( \widetilde a , \overline { { a } } ) > 0 , b = \operatorname* { m a x } ( \widetilde b , \overline { { b } } )$ . Next we compute the cost change

$$W (\hat {x} ^ {+}, \mathbf {u} ^ {+}, e ^ {+}) - W (\hat {x}, \mathbf {u}, e) = V (\hat {x} ^ {+}, \mathbf {u} ^ {+}) - V (\hat {x}, \mathbf {u}) + J (e ^ {+}) - J (e)$$

The Lyapunov function V is quadratic in $( x , \mathbf { u } )$ and therefore Lipschitz continuous on bounded sets. Therefore, for all $\hat { x } , u _ { 1 } , u _ { 2 } , \mathbf { u } ^ { + }$ , e in some

bounded set,

$$\left| V (A \hat {x} + \overline {{B}} _ {1} u _ {1} + \overline {{B}} _ {2} u _ {2} + L e, \mathbf {u} ^ {+}) - V (A \hat {x} + \overline {{B}} _ {1} u _ {1} + \overline {{B}} _ {2} u _ {2}, \mathbf {u} ^ {+}) \right| \leq L _ {V} | L e |$$

in which $L _ { V }$ is the Lipschitz constant for V with respect to its first argument. Using the system evolution we have

$$V (\hat {x} ^ {+}, \mathbf {u} ^ {+}) \leq V (A \hat {x} + \overline {{B}} _ {1} u _ {1} + \overline {{B}} _ {2} u _ {2}, \mathbf {u} ^ {+}) + L _ {V} ^ {\prime} | e |$$

in which $L _ { V } ^ { \prime } = L _ { V } \left| L \right|$ . Subtracting $V ( \hat { x } , { \mathbf { u } } )$ from both sides gives

$$V (\hat {x} ^ {+}, \mathbf {u} ^ {+}) - V (\hat {x}, \mathbf {u}) \leq - \tilde {c} | \hat {x} | ^ {2} + L _ {V} ^ {\prime} | e |$$

Substituting this result into the equation for the change in W gives

$$
\begin{array}{l} W \left(\hat {x} ^ {+}, \mathbf {u} ^ {+}, e ^ {+}\right) - W (\hat {x}, \mathbf {u}, e) \leq - \tilde {c} | \hat {x} | ^ {2} + L _ {V} ^ {\prime} | e | - \bar {c} | e | \\ \leq - \widetilde {c} | \hat {x} | ^ {2} - (\overline {{c}} - L _ {V} ^ {\prime}) | e | \\ W (\hat {x} ^ {+}, \mathbf {u} ^ {+}, e ^ {+}) - W (\hat {x}, \mathbf {u}, e) \leq - c (| \hat {x} | ^ {2} + | e |) \tag {6.24} \\ \end{array}
$$

in which we choose $\overline { { c } } > L _ { V } ^ { \prime }$ , which is possible because we may choose $\overline { { c } }$ as large as we wish, and $c = \operatorname* { m i n } ( \widetilde { c } , \overline { { c } } - L _ { V } ^ { \prime } ) > 0$ . Notice this step is what motivated using the first power of the norm in $J ( \cdot )$ . Lastly, we require the constraint

$$| \mathbf {u} | \leq d | \hat {x} | \quad \hat {x} \in \tilde {r} \mathcal {B} \tag {6.25}$$

Lemma 6.13 (Exponential stability of perturbed system). If either $x _ { N }$ or U is compact, the origin for the state plus estimate error (x, e) is exponentially stable for system (6.22) under cooperative distributed MPC.

The proof is based on the properties (6.23), (6.24) and (6.25) of function $W ( \hat { x } , { \mathbf { u } } , e )$ and is similar to the proof of Lemma 6.4. The region of attraction is the set of states and initial estimate errors for which the unstable modes of the two subsystems can be brought to zero in N moves while satisfying the respective input constraints. If both subsystems are stable, for example, the region of attraction is $( x , e ) \in \mathcal { X } _ { N } { \times } \mathbb { R } ^ { n }$ .
