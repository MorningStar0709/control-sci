# 3.6.5 Choosing Z and V

The tightened constraint sets Z and V may, in principle, be computed. Suppose there exists a single state constraint $c ^ { \prime } x \leq e$ . The tightened state constraint set is $\mathbb { Z } : = \{ x \mid c ^ { \prime } x \leq f \}$ where $f < e$ . Assuming that the constant d is known, the tightened state constraint set is suitable provided that

$$\phi (z) := \max _ {x} \{c ^ {\prime} x \mid x \in S _ {d} (z) \} \leq e$$

for all $z \in \mathbb { Z } \cap { \mathcal { Z } } _ { N }$ , i.e., for all $z \in { \mathcal { Z } } _ { N }$ satisfying $c ^ { \prime } z \leq f .$ . In practice, $\phi ( z )$ could be computed for a finite number of representative points in $\mathbb { Z } \cap \mathcal { Z } _ { N }$ . Since $S _ { d } ( z ) : = \{ x \mid V _ { N } ^ { 0 } ( x , z ) \leq d \}$ , φ(z) may be computed using

$$- \phi (z) = \min _ {x} \{- c ^ {\prime} x \mid V _ {N} ^ {0} (x, z) \leq d \} = \min _ {(x, \mathbf {u})} \{- c ^ {\prime} x \mid V _ {N} (x, z, \mathbf {u}) \leq d \}$$

Other state constraints may be similarly treated. The tightened control constraint set also may be computed.

An alternative is the following. If, as is often the case even for nonlinear systems, the sets X and U are polyhedral, we may choose tightened constraint sets $\mathbb { Z } \ = \ \alpha \mathbb { X }$ and $\mathbb { V } ~ = ~ \beta \mathbb { V }$ where α, $\beta \in \mathsf { \Gamma } ( 0 , 1 )$

by a simple modification of the defining inequalities. $\operatorname { I f } ,$ , for example, $\mathbb { X } = \{ x \mid A x \leq a \}$ , then $\alpha \mathbb { X } = \{ x \mid A x \leq \alpha a \}$ . This choice may be tested by Monte Carlo simulation of the controlled system. If constraints are violated in the simulation, α and $\beta$ may be reduced; if the constraints are too conservative, α and $\beta$ may be increased. For each choice of α and $\beta ,$ , the controller provides a degree of robustness that can be adjusted by modifying the “tuning” parameters α and $\beta .$ .
