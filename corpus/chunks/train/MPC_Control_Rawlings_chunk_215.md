For all $j \in \mathbb { I } _ { 0 : N - 1 }$ , let $V _ { j } ( x , \mathbf { u } ) , \mathcal { U } _ { j } ( x ) , \mathbb { P } _ { j } ( x )$ , and $V _ { j } ^ { 0 } ( x )$ be defined, respectively, by (2.4), (2.5), (2.6), and (2.7), with N replaced by j. As shown in Section C.1 of Appendix C, DP solves not only $\mathbb { P } _ { N } ( x )$ for all $\boldsymbol { x } \in \mathcal { X } _ { N }$ , the domain of $V _ { N } ^ { 0 } ( \cdot )$ , but also $\mathbb { P } _ { j } ( x )$ for all $x \in \mathcal { X } _ { j }$ , the domain of $V _ { j } ^ { 0 } ( \cdot )$ , all $j \in \mathbb { I } _ { 0 : N - 1 }$ . The DP equations are

$$V _ {j} ^ {0} (x) = \min _ {u \in \mathbb {U}} \left\{\ell (x, u) + V _ {j - 1} ^ {0} (f (x, u)) \mid f (x, u) \in \mathcal {X} _ {j - 1} \right\}, \forall x \in \mathcal {X} _ {j} \tag {2.10}\kappa_ {j} (x) = \arg \min _ {u \in \mathbb {U}} \left\{\ell (x, u) + V _ {j - 1} ^ {0} (f (x, u)) \mid f (x, u) \in \mathcal {X} _ {j - 1} \right\}, \forall x \in \mathcal {X} _ {j} \tag {2.11}\mathcal {X} _ {j} = \{x \in \mathbb {X} \mid \exists u \in \mathbb {U} \text { such that } f (x, u) \in \mathcal {X} _ {j - 1} \} \tag {2.12}$$

for $j = 1 , 2 , \dots , N$ (j is time to go), with terminal conditions

$$V _ {0} ^ {0} (x) = V _ {f} (x) \forall x \in \mathcal {X} _ {0} \quad \mathcal {X} _ {0} = \mathbb {X} _ {f}$$

For each $j , V _ { j } ^ { 0 } ( x )$ is the optimal cost for problem $\mathbb { P } _ { j } ( x )$ if the current state is x, current time is 0 (or i), and the terminal time is $j \left( \mathrm { o r } i + j \right)$ , and $\chi _ { j }$ is its domain; $\chi _ { j }$ is also the set of states in X that can be steered to the terminal set $\mathbb { X } _ { f }$ in $j$ steps by an admissible control sequence, i.e., a control sequence that satisfies the control, state, and terminal constraints and, therefore, lies in the set $\mathcal { U } _ { j } ( \boldsymbol { x } )$ . Hence, for each j

$$\mathcal {X} _ {j} = \{x \in \mathbb {X} \mid \mathcal {U} _ {j} (x) \neq \emptyset \}$$

Definition 2.9 (Feasible preimage of the state). Let $\mathbb { Z } : = \mathbb { X } \times \mathbb { U }$ . The set-valued function $f _ { \mathbb { Z } } ^ { - 1 } : \mathbb { X } \to \mathbb { Z }$ is defined by

$$f _ {\mathbb {Z}} ^ {- 1} (x) := f ^ {- 1} (x) \cap \mathbb {Z}$$

in which

$$f ^ {- 1} (x) := \{z \in \mathbb {R} ^ {n} \times \mathbb {R} ^ {m} \mid f (z) = x \}$$

For all $j \geq 0$ , let the set $\mathcal { Z } _ { j } \subseteq \mathbb { R } ^ { n } \times \mathbb { R } ^ { m }$ be defined by

$$\mathcal {Z} _ {j} := f _ {\mathbb {Z}} ^ {- 1} \left(\mathcal {X} _ {j - 1}\right) = \{(x, u) \mid f (x, u) \in \mathcal {X} _ {j - 1} \} \cap \mathbb {Z}$$
