$$(\partial / \partial t) u _ {i} + \sum_ {j = 1} ^ {n} u _ {j} (\partial u _ {i} / \partial x _ {j}) = \nu \Delta u _ {i} - (\partial p / \partial x _ {i}) + f _ {i} (x, t) \quad (\boldsymbol {x} \in \mathbf {R} ^ {n}, t \geq 0), \tag {2.51}\operatorname{div} u = \sum_ {i = 1} ^ {n} (\partial u _ {i} / \partial x _ {i}) = 0 \quad (\boldsymbol {x} \in \mathbf {R} ^ {n}, t \geq 0), \tag {2.52}$$

with initial conditions

$$\mathbf {u} (\boldsymbol {x}, 0) = \mathbf {u} ^ {0} (\boldsymbol {x}), \quad \boldsymbol {x} \in \mathbf {R} ^ {n}, \tag {2.53}$$

where

$$\Delta = \sum_ {i = 1} ^ {n} (\partial^ {2} / \partial x _ {i} ^ {2})$$

is the Laplacian in the space variables.

Here, ${ \pmb u } ^ { 0 } ( { \pmb x } )$ is a given $c ^ { \infty }$ divergence-free vector field on $\mathbf { R } ^ { n } , f _ { i } ( x , t )$ are the components of a given externally applied force (e.g., gravity), and ν is a positive coefficient (the viscosity). Equation (2.51) is just Newton’s law $f = m { \pmb a }$ for a fluid element subject to the external force $f { = } ( f _ { i } ( x , t ) ) _ { 1 { \leq } i { \leq } n }$ and to the force arising from pressure and friction. Equation (2.52) just says that the fluid is incompressible. For physically reasonable solutions, we want to make sure that ${ \pmb u } ( { \pmb x } , t )$ does not grow large as $| x | \to \infty$ . Moreover, we accept a solution of equations (2.51)–(2.53) as physically reasonable only if it satisfies

$$p, \boldsymbol {u} \in \boldsymbol {C} ^ {\infty} (\mathbf {R} ^ {n} \times [ 0, \infty))$$

and

$$\int_ {\mathbf {R} ^ {n}} | \boldsymbol {u} (\mathbf {x}, t) | ^ {2} d x < \boldsymbol {C} \quad \forall t \geq 0 (\text { bounded energy }).$$
