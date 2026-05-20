We can deal with the obstacle posed by the fact that the upper bound on $V _ { N } ^ { 0 } ( \cdot )$ holds only in $\mathbb { X } _ { f }$ in much the same way as we did previously for the time-invariant case. For simplicity, however, we invoke instead a uniform controllability assumption.

Assumption 2.36 (Uniform weak controllability). There exists a $\mathcal { K } _ { \infty }$ function $\alpha _ { 1 } ( \cdot )$ such that

$$V _ {N} ^ {0} (x, i) \leq \alpha (| x |) \quad \forall x \in \mathcal {X} _ {N} (i), \forall i \in \mathbb {I} _ {\geq 0}$$

If Assumptions 2.25, 2.26, 2.30, 2.31, 2.34, and 2.36 are satisfied, it follows from the proof of Proposition 2.35 that, for all $i \in \mathbb { I } _ { \geq 0 }$ （号

$$V _ {N} ^ {0} (x, i) \geq \alpha_ {1} (| x |) \quad \forall x \in \mathcal {X} _ {N} (i) \tag {2.30}V _ {N} ^ {0} (x, i) \leq \alpha_ {2} (| x |) \quad \forall x \in \mathcal {X} _ {N} (i) \tag {2.31}V _ {N} ^ {0} (f (x, \kappa_ {N} (x, i), i)) \leq V _ {N} ^ {0} (x, i) - \alpha_ {1} (| x |) \quad \forall x \in \mathcal {X} _ {N} (i) \tag {2.32}$$

Since the bounds in inequalities (2.30)–(2.32) hold independently of time $i \in \mathbb { I } _ { \geq 0 }$ , we may employ Theorems B.11 and B.13 of Appendix B with minor modification to obtain the following stability result.

<table><tr><td>Assumption</td><td>Title</td><td>Page</td></tr><tr><td>2.2</td><td>Continuity of system and cost</td><td>97</td></tr><tr><td>2.3</td><td>Properties of constraint sets</td><td>97</td></tr><tr><td>2.12</td><td>Basic stability assumption</td><td>115</td></tr><tr><td>2.13</td><td>Implied invariance assumption</td><td>115</td></tr><tr><td>2.16</td><td>Bounds on stage and terminal costs</td><td>118</td></tr><tr><td>2.23</td><td>Weak controllability</td><td>122</td></tr></table>

Table 2.1: Stability assumptions; time-invariant case.

<table><tr><td>Assumption</td><td>Title</td><td>Page</td></tr><tr><td>2.25</td><td>Continuity of system and cost</td><td>127</td></tr><tr><td>2.26</td><td>Properties of constraint sets</td><td>128</td></tr><tr><td>2.30</td><td>Basic stability assumption</td><td>129</td></tr><tr><td>2.31</td><td>Implied invariance assumption</td><td>129</td></tr><tr><td>2.34</td><td>Bounds on stage and terminal costs</td><td>130</td></tr><tr><td>2.36</td><td>Uniform weak controllability</td><td>130</td></tr></table>

Table 2.2: Stability assumptions; time-varying case.

Theorem 2.37 (MPC stability; time-varying case). Suppose Assumptions 2.25, 2.26, 2.30, 2.31, 2.34, and 2.36 hold. Then, for each initial time $i \in \mathbb { I } _ { \geq 0 }$ , the origin is asymptotically stable with a region of attraction $\mathcal { X } _ { N } ( i )$ for the time-varying system $x ^ { + } = f ( x , \kappa _ { N } ( x , j ) , j ) , j \geq i$ .
