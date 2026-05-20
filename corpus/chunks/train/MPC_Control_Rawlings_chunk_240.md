$$
\begin{array}{l} V _ {N} ^ {0} (x) \geq \alpha_ {1} (| x |) \\ V _ {N} ^ {0} (f (x, \kappa_ {N} (x))) \leq V _ {N} ^ {0} (x) - \alpha_ {1} (| x |) \\ V _ {N} ^ {0} (x) \leq \alpha_ {2} (| x |) \\ \end{array}
$$

for all $x \in \mathbb { R } ^ { n }$ . Asymptotic stability of the origin follows from Theorem B.11 in Appendix B. When Assumption 2.16(b) is satisfied, global exponential stability of the origin follows as in the proof of the next part with $\mathcal { X } _ { N } = \mathbb { R } ^ { n }$ .

(b) If Assumption 2.16(a) is satisfied, asymptotic stability of the origin follows from Proposition 2.17 and Theorem 2.22. If Assumption 2.16(b) is satisfied and $x _ { N }$ is bounded, it follows from Propositions 2.18 and 2.19 that there exists $c _ { 2 }$ sufficiently large such that the value function satisfies

$$V _ {N} ^ {0} (x) \geq c _ {1} | x | ^ {a} \tag {2.26}V _ {N} ^ {0} (f (x, \kappa_ {N} (x))) \leq V _ {N} ^ {0} (x) - c _ {1} | x | ^ {a} \tag {2.27}V _ {N} ^ {0} (x) \leq c _ {2} | x | ^ {a} \tag {2.28}$$

for all $x \in \mathcal { X } _ { N }$ . Consider any initial state $x \in \mathcal { X } _ { N }$ , and let $x ( i )$ denote the solution at time i of the difference equation $x ^ { + } = f ( x , \kappa _ { N } ( x ) )$ ) with initial condition $x ( 0 ) = x$ . Since, by Proposition 2.11, XN is positive invariant for $x ^ { + } = f ( x , \kappa _ { N } ( x ) )$ , the entire sequence $\{ x ( i ) \}$ lies in $x _ { N }$ if the initial state x lies in $x _ { N }$ . Hence $\{ x ( i ) \}$ satisfies

$$V _ {N} ^ {0} (x (i + 1)) \leq V _ {N} ^ {0} (x (i)) - c _ {1} | x (i) | ^ {a} \leq (1 - c _ {1} / c _ {2}) V _ {N} ^ {0} (x (i))$$

for all $i \in \mathbb { I } _ { \geq 0 }$ . It follows that

$$V _ {N} ^ {0} (x (i)) \leq \gamma^ {i} V _ {N} ^ {0} (x (0))$$

for all $i \in \mathbb { I } _ { \geq 0 }$ in which $\gamma : = ( 1 - c _ { 1 } / c _ { 2 } ) \in ( 0 , 1 )$ . Hence

$$| x (i) | ^ {a} \leq (1 / c _ {1}) V _ {N} ^ {0} (x (i)) \leq (1 / c _ {1}) \gamma^ {i} V _ {N} ^ {0} (x (0)) \leq (c _ {2} / c _ {1}) \gamma^ {i} | x (0) | ^ {a}$$
