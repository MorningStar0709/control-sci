# A.11 Continuity

3. A function $f : \mathbb { R } ^ { n }  \mathbb { R } ^ { m }$ is said to be upper semicontinuous at a point $\boldsymbol { x } \in \mathbb { R } ^ { n }$ , if for every $\delta > 0$ there exists a $\rho > 0$ such that

$$f (x ^ {\prime}) - f (x) < \delta \forall x ^ {\prime} \in \operatorname{int} (B (x, \rho))$$

A function $f : \mathbb { R } ^ { n }  \mathbb { R } ^ { m }$ is said to be upper semicontinuous if it is upper semicontinuous at all $\boldsymbol { x } \in \mathbb { R } ^ { n }$ .

4. A function $f : \mathbb { R } ^ { n }  \mathbb { R } ^ { m }$ is said to be lower semicontinuous at a point $\boldsymbol { x } \in \mathbb { R } ^ { n }$ , if for every $\delta > 0$ there exists a $\rho > 0$ such that

$$f (x ^ {\prime}) - f (x) > - \delta \forall x ^ {\prime} \in \operatorname{int} (B (x, \rho))$$

A function $f : \mathbb { R } ^ { n }  \mathbb { R } ^ { m }$ is said to be lower semicontinuous if it is continuous at all $\boldsymbol { x } \in \mathbb { R } ^ { n }$ .

5. A function $f : \mathbb { R } ^ { n }  \mathbb { R } ^ { m }$ is said to be uniformly continuous on a subset $X \subset \mathbb { R } ^ { n }$ if for any $\delta > 0$ there exists a $\rho > 0$ such that for any $x ^ { \prime } , x ^ { \prime \prime } \in X$ satisfying $| x ^ { \prime } - x ^ { \prime \prime } | < \rho$ ,

$$\left| f (x ^ {\prime}) - f (x ^ {\prime \prime}) \right| < \delta$$

Proposition A.5 (Uniform continuity). Suppose that $f : \mathbb { R } ^ { n }  \mathbb { R } ^ { m }$ is continuous and that $X \subset \mathbb { R } ^ { n }$ is compact. Then f is uniformly continuous on X .

Proof. For the sake of contradiction, suppose that f is not uniformly continuous on X. Then, for some $\delta > 0$ , there exist sequences $\{ x _ { i } ^ { \prime } \} , \{ x _ { i } ^ { \prime \prime } \}$ in X such that

$$\left| x _ {i} ^ {\prime} - x _ {i} ^ {\prime \prime} \right| < (1 / i), \text { for all } i \in \mathbb {I} _ {\geq 0}$$

but

$$\left| f (x _ {i} ^ {\prime}) - f (x _ {i} ^ {\prime \prime}) \right| > \delta , \text { for all } i \in \mathbb {I} _ {\geq 0} \tag {A.1}$$

Since X is compact, there must exist a subsequence $\{ x _ { i } ^ { \prime } \} _ { i \in K }$ such that $x _ { i } ^ { \prime } \stackrel { K } {  } x ^ { \ast } \in X$ as $i  \infty$ . Furthermore, because of (A.1), $x _ { i } ^ { \prime \prime } \stackrel { K } {  } x ^ { \ast }$ also holds. Hence, since $f ( \cdot )$ is continuous, we must have $f ( x _ { i } ^ { \prime } ) \stackrel { K } {  } f ( x ^ { * } )$ and $f ( x _ { i } ^ { \prime \prime } ) \stackrel { K } {  } f ( x ^ { \ast } )$ . Therefore, there exists a $i _ { 0 } \in K$ such that for all $i \in K , i \geq i _ { 0 }$

$$| f (x _ {i} ^ {\prime}) - f (x _ {i} ^ {\prime \prime}) | \leq | f (x _ {i} ^ {\prime}) - f (x ^ {*}) | + | f (x ^ {*}) - f (x _ {i} ^ {\prime \prime}) | < \delta / 2$$

contradicting (A.1). This completes our proof.

Proposition A.6 (Compactness of continuous functions of compact sets). Suppose that $X \subset \mathbb { R } ^ { n }$ is compact and that $f : \mathbb { R } ^ { n }  \mathbb { R } ^ { m }$ is continuous. Then the set

$$f (X) := \{f (x) \mid x \in X \}$$

is compact.
