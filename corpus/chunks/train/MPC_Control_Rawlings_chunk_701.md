2. The cost decreases on iteration: $V ( x _ { 1 } ( 0 ) , x _ { 2 } ( 0 ) , ( { \bf u } _ { 1 } , { \bf u } _ { 2 } ) ^ { p + 1 } ) \ \le$ $V ( x _ { 1 } ( 0 ) , x _ { 2 } ( 0 ) , ( { \bf u } _ { 1 } , { \bf u } _ { 2 } ) ^ { p } )$ for all $x _ { 1 } ( 0 ) , x _ { 2 } ( 0 )$ , and for all feasible $( \mathbf { u } _ { 1 } , \mathbf { u } _ { 2 } ) ^ { p } \in ( \mathbb { U } _ { 1 } , \mathbb { U } _ { 2 } )$ . The systemwide cost satisfies the following inequalities

$$
\begin{array}{l} V (x (0), \mathbf {u} _ {1} ^ {p + 1}, \mathbf {u} _ {2} ^ {p + 1}) = V \left(x (0), \left(w _ {1} (\mathbf {u} _ {1} ^ {0}, \mathbf {u} _ {2} ^ {p}) + w _ {2} (\mathbf {u} _ {1} ^ {p}, \mathbf {u} _ {2} ^ {0})\right)\right) \\ \leq w _ {1} V (x (0), \left(\mathbf {u} _ {1} ^ {0}, \mathbf {u} _ {2} ^ {p}\right)) + w _ {2} V (x (0), \left(\mathbf {u} _ {1} ^ {p}, \mathbf {u} _ {2} ^ {0}\right)) \\ \leq w _ {1} V (x (0), \left(\mathbf {u} _ {1} ^ {p}, \mathbf {u} _ {2} ^ {p}\right)) + w _ {2} V (x (0), \left(\mathbf {u} _ {1} ^ {p}, \mathbf {u} _ {2} ^ {p}\right)) \\ = V (x (0), \mathbf {u} _ {1} ^ {p}, \mathbf {u} _ {2} ^ {p}) \\ \end{array}
$$

The first equality follows from (6.14). The next inequality follows from convexity of V . The next follows from optimality of ${ \bf u } _ { 1 } ^ { 0 }$ and ${ \bf u } _ { 2 } ^ { 0 }$ , and the last follows from $w _ { 1 } + w _ { 2 } = 1$ . Because the cost is bounded below, the cost iteration converges.

3. The converged solution of the cooperative problem is equal to the optimal solution of the centralized problem. Establishing this property is discussed in Exercise 6.26.

Exponential stability of the closed-loop system. We next consider the closed-loop system. The two players’ warm starts at the next sample are as defined previously

$$
\begin{array}{l} \tilde {\mathbf {u}} _ {1} ^ {+} = \left\{u _ {1} (1), u _ {1} (2), \dots , u _ {1} (N - 1), 0 \right\} \\ \widetilde {\mathbf {u}} _ {2} ^ {+} = \{u _ {2} (1), u _ {2} (2), \dots , u _ {2} (N - 1), 0 \} \\ \end{array}
$$

We define again the functions $g _ { 1 } ^ { p } , g _ { 2 } ^ { p }$ as the outcome of applying the control iteration procedure p times

$$
\begin{array}{l} \mathbf {u} _ {1} ^ {p} = g _ {1} ^ {p} (x _ {1}, x _ {2}, \mathbf {u} _ {1}, \mathbf {u} _ {2}) \\ \mathbf {u} _ {2} ^ {p} = g _ {2} ^ {p} (x _ {1}, x _ {2}, \mathbf {u} _ {1}, \mathbf {u} _ {2}) \\ \end{array}
$$

The important difference between the previous unconstrained and this constrained case is that the functions $\bar { g } _ { 1 } ^ { p } , g _ { 2 } ^ { p }$ are nonlinear due to the input constraints. The system evolution is then given by
