$$V _ {f} (x) := (1 / 2) x ^ {\prime} P ^ {*} x + \lambda (x ^ {\prime} P x) ^ {3 / 2}$$

is a global CLF for $x ^ { + } = A x + B u$ , satisfying

$$V _ {f} (A x + B \kappa_ {f} (x)) - V _ {f} (x) + (1 / 2) | x | _ {Q ^ {*}} ^ {2} \leq 0 \tag {2.37}$$

for all $\boldsymbol { x } \in \mathbb { R } ^ { n }$ . Suppose now the optimal control problem defining the receding horizon controller (or model predictive controller) is

$$\mathbb {P} _ {N} (x): \quad V _ {N} ^ {0} (x) = \min _ {\mathbf {u}} \{V _ {N} (x, \mathbf {u}) \mid \mathbf {u} \in \mathbb {U} ^ {N} \}$$

in which the cost $V _ { N } ( \cdot )$ is defined by

$$V _ {N} (x, \mathbf {u}) := \sum_ {i = 0} ^ {N - 1} \ell (x (i), u (i)) + V _ {f} (x (N))$$

and, for all $i , x ( i ) = \phi ( i ; x , { \bf u } )$ , the solution of $x ^ { + } = A x + B u$ at time i if the initial state at time 0 is x and the control sequence is u. The stage cost is

$$\ell (x, u) := (1 / 2) \left(\left| x \right| _ {Q} ^ {2} + \left| u \right| _ {R} ^ {2}\right)$$

where Q and R are positive definite and R is diagonal. We wish to ensure that $V _ { f } ( \cdot )$ , defined previously, and $\mathbb { X } _ { f } : = \mathbb { R } ^ { n }$ satisfy Assumption 2.12 so that the system with MPC has satisfactory stability properties. But Assumptions 2.12 and 2.13 are satisfied for all $\boldsymbol { x } \in \mathbb { R } ^ { n }$ if

$$V _ {f} (A x + B \kappa_ {f} (x)) - V _ {f} (x) + \ell (x, \kappa_ {f} (x)) \leq 0 \tag {2.38}$$

It follows from (2.37) that Assumption 2.12 is satisfied if

$$(1 / 2) x ^ {\prime} Q ^ {*} x \geq \ell (x, \kappa_ {f} (x)) = (1 / 2) x ^ {\prime} Q x + (1 / 2) \kappa_ {f} (x) ^ {\prime} R \kappa_ {f} (x) \tag {2.39}$$

We can achieve this by choosing $Q ^ { * }$ appropriately. Suppose

$$Q ^ {*} := Q + K ^ {\prime} R K$$

Then

$$x ^ {\prime} Q ^ {*} x = x ^ {\prime} Q x + (K x) ^ {\prime} R K x$$

But

$$\kappa_ {f} (x) ^ {\prime} R \kappa_ {f} (x) = (\operatorname{sat} (K x)) ^ {\prime} R \operatorname{sat} (K x)$$

Since R is diagonal and positive definite, and since $( \operatorname { s a t } ( a ) ) ^ { 2 } \leq a ^ { 2 }$ if a is a scalar, we have

$$\kappa_ {f} (x) ^ {\prime} R \kappa_ {f} (x) \leq (\operatorname{sat} (K x)) ^ {\prime} R \operatorname{sat} (K x) \leq (K x) ^ {\prime} R K x \forall x \in \mathbb {R} ^ {n}$$

It follows that (2.39) and, hence, (2.38) are satisfied. Therefore, with $V _ { f } ( \cdot )$ as defined previously, $\mathbb { X } _ { f } : = \mathbb { R } ^ { n }$ , and $\ell ( \cdot )$ as defined previously, Assumptions 2.12, 2.13, and 2.16(b) are satisfied. Summarizing, we have:

If these assumptions on $V _ { f } ( \cdot ) , \mathbb { X } _ { f } ,$ , and $\ell ( \cdot )$ hold, and Assumption 2.3 is satisfied, then Assumptions 2.12, 2.13, and 2.16(b) are satisfied, and $\mathcal { X } _ { N } = \mathbb { X } _ { f } = \mathbb { R } ^ { n }$ . It follows from Theorem 2.24 that the origin is globally exponentially stable for the controlled system $x ^ { + } = A x + B \kappa _ { N } ( x )$ .

Because $V _ { f } ( \cdot )$ is not quadratic, the optimal control problem $\mathbb { P } _ { N } ( x )$ is no longer a quadratic program.
