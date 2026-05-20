# 7.4.2 Problem Solution

We present the solution to this fuel-optimal system under the following steps. First let us list the steps.

\- Step 1: Hamiltonian

\- Step 2: Optimal Condition

\- Step 3: Costate Functions

\- Step 4: Normal Fuel-Optimal Control System

\- Step 5: Bang-off-Bang Control Law

\- Step 6: Implementation

\- Step 1: Hamiltonian: Let us formulate the Hamiltonian for the system (7.4.1) and the performance measure (7.4.4) as

$$\mathcal {H} (\mathbf {x} (t), \mathbf {u} (t), \boldsymbol {\lambda} (t)) = \sum_ {j = 1} ^ {r} | u _ {j} (t) | + \boldsymbol {\lambda} ^ {\prime} (t) \mathbf {A x} (t) + \boldsymbol {\lambda} ^ {\prime} (t) \mathbf {B u} (t). \tag {7.4.5}$$

\- Step 2: Optimal Condition: According to the Pontryagin Principle, the optimal condition is given by

$$
\begin{array}{l} \mathcal {H} \left(\mathbf {x} ^ {*} (t), \boldsymbol {\lambda} ^ {*} (t), \mathbf {u} ^ {*} (t)\right) \leq \mathcal {H} \left(\mathbf {x} ^ {*} (t), \boldsymbol {\lambda} ^ {*} (t), \mathbf {u} (t)\right), \\ = \min _ {| \mathbf {u} (t) | \leq 1} \left\{\mathcal {H} (\mathbf {x} ^ {*} (t), \boldsymbol {\lambda} ^ {*} (t), \mathbf {u} (t)) \right\}. \tag {7.4.6} \\ \end{array}
$$

Using (7.4.5) in (7.4.6), we have

$$
\begin{array}{l} \sum_ {j = 1} ^ {r} \left| u _ {j} ^ {*} (t) \right| + \boldsymbol {\lambda} ^ {* \prime} (t) \mathbf {A x} ^ {*} (t) + \boldsymbol {\lambda} ^ {* \prime} (t) \mathbf {B u} ^ {*} (t) \\ \leq \sum_ {j = 1} ^ {r} | u _ {j} (t) | + \boldsymbol {\lambda} ^ {* \prime} (t) \mathbf {A x} ^ {*} (t) + \boldsymbol {\lambda} ^ {* \prime} (t) \mathbf {B u} (t) \tag {7.4.7} \\ \end{array}
$$

which in turn yields

$$\sum_ {j = 1} ^ {r} | u _ {j} ^ {*} (t) | + \boldsymbol {\lambda} ^ {* \prime} (t) \mathbf {B u} ^ {*} (t) \leq \sum_ {j = 1} ^ {r} | u _ {j} (t) | + \boldsymbol {\lambda} ^ {* \prime} (t) \mathbf {B u} (t)$$

or transposing

$$\sum_ {j = 1} ^ {r} \left| u _ {j} ^ {*} (t) \right| + \mathbf {u} ^ {* \prime} (t) \mathbf {B} ^ {\prime} \boldsymbol {\lambda} ^ {*} (t) \leq \sum_ {j = 1} ^ {r} \left| u _ {j} (t) \right| + \mathbf {u} ^ {\prime} (t) \mathbf {B} ^ {\prime} \boldsymbol {\lambda} ^ {*} (t). \tag {7.4.8}$$

Considering the various possibilities as before for the double integral system, we have

$$\mathbf {q} ^ {*} (t) = \mathbf {B} ^ {\prime} \boldsymbol {\lambda} ^ {*} (t). \tag {7.4.9}$$

Using the earlier relations (7.3.11) and (7.3.12) for the dead-zone function, we can write the condition (7.4.6) as
