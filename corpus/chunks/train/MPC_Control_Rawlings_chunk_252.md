# 2.5.1.1 Linear Time-Invariant Systems

Here $f ( x , u ) = A x + B u$ and $\ell ( x , u ) = ( 1 / 2 ) ( | x | _ { O } ^ { 2 } + | u | _ { R } ^ { 2 } )$ where $Q > 0$ and $R > 0$ . If (A, B) is stabilizable, there exists a stabilizing controller $u = K x$ . Let $A _ { K } : = A + B K , Q _ { f } : = Q + K ^ { \prime } R K$ and let $V _ { f } : \mathbb { R } ^ { n } \to \mathbb { R } _ { \geq 0 }$ be defined by $V _ { f } ( x ) : = ( 1 / 2 ) x ^ { \prime } P _ { f } x$ where $P _ { f } > 0$ satisfies the Lyapunov equation

$$A _ {K} ^ {\prime} P _ {f} A _ {K} + Q _ {f} = P _ {f}$$

Since $V _ { N } ^ { 0 } ( x ) ~ \ge ~ \ell ( x , \kappa _ { N } ( x ) ) ~ \ge ~ ( 1 / 2 ) | x | _ { Q } ^ { 2 }$ , it follows that there exist $c _ { 1 } > 0$ and $c _ { 2 } > 0$ such that

$$V _ {N} ^ {0} (x) \geq c _ {1} | x | ^ {2} \quad V _ {f} (x) \leq c _ {2} | x | ^ {2} \quad \forall x \in \mathbb {R} ^ {n}$$

With $f ( \cdot ) , \ell ( \cdot )$ , and $V _ { f } ( \cdot )$ defined this way, problem $\mathbb { P } _ { N } ( x )$ is an unconstrained parametric quadratic program4 of the form mi $\mathrm { n } _ { \mathbf { u } } ( 1 / 2 ) x ^ { \prime } L x +$ $x ^ { \prime } M \mathbf { u } + ( 1 / 2 ) \mathbf { u } ^ { \prime } N \mathbf { u }$ so that $V _ { N } ^ { 0 } ( \cdot )$ is a quadratic function of the parameter x, and $\mathbf { u } ^ { 0 } ( \cdot )$ and $\kappa _ { N } ( \cdot )$ are linear functions of x. Since

$$V _ {f} (A x + B K x) - V _ {f} (x) + \ell (x, K x) = x ^ {\prime} [ A _ {K} ^ {\prime} P _ {f} A _ {K} + Q _ {f} - P _ {f} ] x = 0$$

for all $\boldsymbol { x } \in \mathbb { R } ^ { n }$ ,

$$V _ {f} (A x + B K x) = V _ {f} (x) - \ell (x, K x) \quad \forall x \in \mathbb {R} ^ {n}$$

so that $V _ { f } ( \cdot )$ and $\mathbb { X } _ { f } : = \mathbb { R } ^ { n }$ satisfy Assumptions 2.12 and 2.13 with $u = K x ; V _ { f } ( \cdot )$ is a global CLF and $\mathcal { X } _ { N } = \mathbb { R } ^ { n }$ . Hence,

$$V _ {N} ^ {0} (f (x, \kappa_ {N} (x))) \leq V _ {N} ^ {0} (x) - c _ {1} | x | ^ {2} \quad \forall x \in \mathbb {R} ^ {n}$$

It also follows from Lemma 2.15, which does not require the assumption that U is compact, that

$$V _ {N} ^ {0} (x) \leq V _ {f} (x) \leq c _ {2} | x | ^ {2} \quad \forall x \in \mathbb {R} ^ {n}$$

Summarizing, we have:

With these assumptions on $V _ { f } ( \cdot ) , \mathbb { X } _ { f } ,$ , and $\ell ( \cdot )$ , Assumptions 2.12, 2.13, and 2.16(b) are satisfied and, as shown previously, $V _ { N } ^ { 0 } ( \cdot )$ satisfies (2.26)–(2.28). It follows, as shown in Theorem 2.24(a), that the origin is globally exponentially stable for $x ^ { + } = f ( x , \kappa _ { N } ( x ) )$ .

Since $V _ { f } ( \cdot )$ is a global CLF, there exists a simple stabilizing controller, namely $u \ = \ K x$ . In this case, there is no motivation to use MPC to obtain a stabilizing controller; standard linear $H _ { 2 }$ or $H _ { \infty }$ optimal control theory may be employed to obtain satisfactory control. The situation is different in the time-varying case, which we consider next.
