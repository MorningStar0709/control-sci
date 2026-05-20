$$\Phi (k _ {0}, k _ {0}) = \mathbf {I}, \quad \Phi (k _ {2}, k _ {1}) \Phi (k _ {1}, k _ {0}) = \Phi (k _ {2}, k _ {0}). \tag {B.3.8}$$

Similarly, the solution of the LTV, discrete-time system (B.3.5) is given by

$$\mathbf {x} (k) = \boldsymbol {\Phi} (k, k _ {0}) \mathbf {x} (k _ {0}) + \sum_ {m = k _ {0}} ^ {k - 1} \boldsymbol {\Phi} (k, m + 1) \mathbf {B} (m) \mathbf {u} (m)\mathbf {y} (k) = \mathbf {C} (k) \boldsymbol {\Phi} (k, k _ {0}) \mathbf {x} (k _ {0}) + \mathbf {C} (k) \sum_ {m = k _ {0}} ^ {k - 1} \boldsymbol {\Phi} (k, m + 1) \mathbf {B} (m) \mathbf {u} (m) + \mathbf {D} (k) \mathbf {u} (k) \tag {B.3.9}$$

where,

$$\Phi (k, k _ {0}) = \mathbf {A} (k - 1) \mathbf {A} (k - 2) \dots \mathbf {A} (k _ {0}) \quad k \text { terms }, \tag {B.3.10}$$

is called the state transition matrix of the discrete-time system (B.3.5) satisfying the properties (B.3.8).
