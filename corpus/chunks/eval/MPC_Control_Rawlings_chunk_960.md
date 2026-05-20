# B.9 Incremental-Input/Output-to-State Stability

Definition B.45 (Incremental input/output-to-state stable). The system (B.14) is incrementally input/output-to-state stable (i-IOSS) if there exists some $\beta ( \cdot ) \in \mathcal { K L }$ and $\chi _ { 1 } ( \cdot ) , \chi _ { 2 } ( \cdot ) \in \mathcal { K }$ such that, for every two initial states $z _ { 1 }$ and $z _ { 2 }$ and any two control sequences $\mathbf { u } _ { 1 } = \{ u _ { 1 } ( j ) \}$ and ${ \bf u } _ { 2 } = \{ u _ { 2 } ( j ) \}$ }

$$\left| x (k; z _ {1}, \mathbf {u} _ {1}) - x (k; z _ {2}, \mathbf {u} _ {2}) \right| \leq\max \left\{\beta (| z _ {1} - z _ {2} |, k), \gamma_ {1} (\| \mathbf {u} _ {1} - \mathbf {u} _ {2} \| _ {0: k - 1}), \gamma_ {2} (\left| \left| \mathbf {y} _ {z _ {1}, \mathbf {u} _ {1}} - \mathbf {y} _ {z _ {2}, \mathbf {u} _ {2}} \right| \right| _ {0: k}) \right\}$$
