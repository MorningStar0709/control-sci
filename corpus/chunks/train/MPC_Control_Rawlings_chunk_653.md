$$\mathbf {u} ^ {0} (x (0)) = - (\mathcal {B} ^ {\prime} \mathcal {Q B} + \mathcal {R}) ^ {- 1} \mathcal {B} ^ {\prime} \mathcal {Q A} x (0)$$

and the optimal cost is

$$V ^ {0} (x (0)) = \left(\frac {1}{2}\right) x ^ {\prime} (0) \left(Q + \mathcal {A} ^ {\prime} \mathcal {Q} \mathcal {A} - \mathcal {A} ^ {\prime} \mathcal {Q} \mathcal {B} (\mathcal {B} ^ {\prime} \mathcal {Q} \mathcal {B} + \mathcal {R}) ^ {- 1} \mathcal {B} ^ {\prime} \mathcal {Q} \mathcal {A}\right) x (0)$$

If used explicitly, this procedure for computing $ { \mathbf { u } } ^ { 0 }$ would be inefficient because $\mathcal { B } ^ { \prime } \mathcal { Q B } + \mathcal { R }$ is an $( m N \times m N )$ matrix. Notice that in the DP formulation one has to invert instead an $( m \times m )$ matrix N times, which is computationally less expensive.1 Notice also that unlike DP, the least squares approach provides all input moves as a function of the initial state, $x ( 0 )$ . The gain for the control law comes from the first input move in the sequence

$$K (0) = - \left[ I _ {m} \quad 0 \quad \dots \quad 0 \right] (\mathcal {B} ^ {\prime} \mathcal {Q B} + \mathcal {R}) ^ {- 1} \mathcal {B} ^ {\prime} \mathcal {Q A}$$

It is not immediately clear that the K(0) and $V ^ { 0 }$ given above from the least squares approach are equivalent to the result from the Riccati iteration, (1.11)–(1.15) of Chapter 1, but since we have solved the same optimization problem, the two results are the same.2

Retaining the state sequence. In this section we set up the least squares problem again, but with an eye toward improving its efficiency. Retaining the state sequence and adjoining the model equations as equality constraints is a central idea in optimal control and is described in standard texts (Bryson and Ho, 1975, p. 44). We apply this standard approach here. Wright (1997) provides a discussion of this problem in the linear model MPC context and the extensions required for the quadratic programming problem when there are inequality constraints on the states and inputs. Including the state with the input in the sequence of unknowns, we define the enlarged vector z to be

$$
\mathbf {z} = \left[ \begin{array}{c} u (0) \\ x (1) \\ u (1) \\ x (2) \\ \vdots \\ u (N - 1) \\ x (N) \end{array} \right]
$$

The objective function is

$$\min _ {\mathbf {u}} (1 / 2) \left(x ^ {\prime} (0) Q x (0) + \mathbf {z} ^ {\prime} H \mathbf {z}\right)$$

in which
