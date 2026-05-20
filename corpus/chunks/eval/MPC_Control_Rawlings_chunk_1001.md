We return to this point later. Perhaps the simplest method for proving Proposition C.22 is the penalty approach adopted by Bertsekas (1999), Proposition 3.3.5. We merely give an outline of the proof. The constrained problem of minimizing $f ( \nu )$ over U is approximated, for each $k \in \mathbb { I } _ { \geq 0 }$ by a penalized problem defined below; as k increases the penalized problem becomes a closer approximation to the constrained problem. For each $i \in { \mathcal { I } }$ , we define

$$g _ {i} ^ {+} (\nu) := \max \{g _ {i} (\nu), 0 \}$$

For each $k ,$ , the penalized problem $\mathbb { P } ^ { k }$ is then defined as the problem of minimizing $F ^ { k } ( \upsilon )$ defined by

$$F ^ {k} (\nu) := f (\nu) + (k / 2) \sum_ {i \in \mathcal {I}} (g _ {i} ^ {+} (\nu)) ^ {2} + (k / 2) \sum_ {j \in \mathcal {E}} (h _ {j} (\nu)) ^ {2} + (1 / 2) | \nu - u | ^ {2}$$

subject to the constraint

$$S := \{\nu \mid | \nu - u | \leq \varepsilon \}$$

where $\epsilon > 0$ is such that $f ( u ) \leq f ( \nu )$ for all v in $S \cap U$ . Let $\nu ^ { k }$ denote the solution of $\mathbb { P } ^ { k }$ . Bertsekas shows that $\nu ^ { k } \to u$ as $k  \infty$ so that for all k sufficiently large, $\nu ^ { k }$ lies in the interior of S and is, therefore, the unconstrained minimizer of $F ^ { k } ( \upsilon )$ . Hence for each k sufficiently large, $\nu ^ { k }$ satisfies $\nabla F ^ { k } ( \nu ^ { k } ) = 0$ , or

$$\nabla f (\boldsymbol {v} ^ {k}) + \sum_ {i \in \mathcal {I}} \bar {\mu} _ {i} ^ {k} \nabla g (\boldsymbol {v} ^ {k}) + \sum_ {i \in \mathcal {E}} \bar {\lambda} _ {i} ^ {k} \nabla h (\boldsymbol {v} ^ {k}) = 0 \tag {C.27}$$

where

$$\bar {\mu} _ {i} ^ {k} := k g _ {i} ^ {+} (\nu^ {k}), \quad \bar {\lambda} _ {i} ^ {k} := k h _ {i} (\nu^ {k})$$

Let $\mu ^ { k }$ denote the vector with elements $\mu _ { i } ^ { k } , i \in \mathcal { I }$ and $\lambda ^ { k }$ the vector with elements $\lambda _ { i } ^ { k } , k \in \mathcal { F }$ . Dividing (C.27) by $\delta ^ { \dot { k } }$ defined by

$$\delta^ {k} := [ 1 + | \mu^ {k} | ^ {2} + | \lambda^ {k} | ^ {2} ] ^ {1} / 2$$

yields

$$\mu_ {0} ^ {k} \nabla f (\boldsymbol {v} ^ {k}) + \sum_ {i \in \mathcal {I}} \mu_ {i} ^ {k} \nabla g (\boldsymbol {v} ^ {k}) + \sum_ {j \in \mathcal {E}} \lambda_ {j} ^ {k} \nabla h (\boldsymbol {v} ^ {k}) = 0$$

where

$$\mu_ {0} ^ {k} := \bar {\mu} _ {i} ^ {k} / \delta^ {k}, \quad \mu_ {i} ^ {k} := \bar {\mu} _ {i} ^ {k} / \delta^ {k}, \quad \lambda_ {j} ^ {k} := \bar {\lambda} _ {i} ^ {k} / \delta^ {k}$$

and

$$(\mu_ {0} ^ {k}) ^ {2} + | \mu^ {k} | ^ {2} + | \lambda^ {k} | ^ {2} = 1$$
