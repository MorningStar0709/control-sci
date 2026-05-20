(b) If $ { \mathcal { X } } _ { 0 } : =  { \mathbb { X } } _ { f }$ is control invariant for $x ^ { + } = f ( x , u ) , u \in \mathbb { U }$ , then, for each $j \in \mathbb { I } _ { \geq 0 }$ , the set $\chi _ { j }$ is also control invariant, $\boldsymbol { \mathcal { X } } _ { j } \supseteq \boldsymbol { \mathcal { X } } _ { j - 1 }$ , and $0 \in \mathcal { X } _ { j }$ . In addition, the set $x _ { N }$ is positive invariant for $x ^ { + } = f ( x , \kappa _ { N } ( x ) )$ .

(c) For each $j \geq 0$ , the set $\chi _ { j }$ is closed.

Proof.

(a) This proof is almost identical to the proof of Proposition 2.4.

(b) By assumption, $\mathcal { X } _ { 0 } = \mathbb { X } _ { f } \subseteq \mathbb { X }$ is control invariant. By (2.12)

$$\mathcal {X} _ {1} = \{x \in \mathbb {X} \mid \exists u \in \mathbb {U} \text { such that } f (x, u) \in \mathcal {X} _ {0} \}$$

Since $x _ { 0 }$ is control invariant for $x ^ { + } = f ( x , u ) , u \in \mathbb { U }$ , for every $x \in \mathcal { X } _ { 0 }$ there exist a $u \in \mathbb { V }$ such that $f ( x , u ) \in \mathcal { X } _ { 0 }$ so that $x \in \mathcal { X } _ { 1 }$ . Hence $x _ { 1 } \ \supseteq \ x _ { 0 }$ . Since for every $x \ \in \ { \mathcal { X } } _ { 1 }$ , there exists a $u \in \mathbb { V }$ such that $f ( x , u ) \in \mathcal { X } _ { 0 } \subseteq \mathcal { X } _ { 1 }$ , it follows that $x _ { 1 }$ is control invariant for $x ^ { + } =$ $f ( x , u ) , u \in \mathbb { U }$ . If for some integer $j \in \mathbb { I } _ { \geq 0 } , \chi _ { j - 1 }$ is control invariant for $x ^ { + } = f ( x , u )$ , it follows by similar reasoning that $\mathscr { X } _ { j } \supseteq \mathscr { X } _ { j - 1 }$ and that $\chi _ { j }$ is control invariant. By induction $\chi _ { j }$ is control invariant and $\boldsymbol { \mathcal { X } } _ { j } ~ \equiv ~ \boldsymbol { \mathcal { X } } _ { j - 1 }$ for all $j > 0$ . Hence $0 \in \mathcal X _ { j }$ for all $j \in \mathbb { I } _ { \geq 0 }$ . That $x _ { N }$ is positive invariant for $x ^ { + } = f ( x , \kappa _ { N } ( x ) )$ follows from (2.11), which shows that $\kappa _ { N } ( \cdot )$ steers every $\boldsymbol { x } \in \mathcal { X } _ { N }$ into $\mathcal { X } _ { N - 1 } \subseteq \mathcal { X } _ { N }$ .
