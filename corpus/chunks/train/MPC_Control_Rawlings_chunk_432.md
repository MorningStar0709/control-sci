# Exercise 3.1: Removing the outer min in a min-max problem

Show that $V _ { i } ^ { 0 } : { \mathcal { X } } _ { i }  { \mathbb { R } }$ and $\kappa _ { i } : \mathcal { X } _ { i }  \mathbb { U }$ defined by

$$V _ {i} ^ {0} (x) = \min _ {u \in \mathbb {U}} \max _ {w \in \mathbb {W}} \{\ell (x, u, w) + V _ {i - 1} ^ {0} (f (x, u, w)) \mid f (x, u, \mathbb {W}) \subset \mathcal {X} _ {i - 1} \}\kappa_ {i} (x) = \arg \min _ {u \in \mathbb {U}} \max _ {w \in \mathbb {W}} \{\ell (x, u, w) + V _ {i - 1} ^ {0} (f (x, u, w)) \mid f (x, u, \mathbb {W}) \subset \mathcal {X} _ {i - 1} \}\mathcal {X} _ {i} = \{x \in \mathbb {X} \mid \exists u \in \mathbb {U} \text { such that } f (x, u, \mathbb {W}) \subset \mathcal {X} _ {i - 1} \}$$

satisfy

$$V _ {i} ^ {0} (x) = \max _ {w \in \mathbb {W}} \{\ell (x, \kappa_ {i} (x), w) + V _ {i - 1} ^ {0} (f (x, \kappa_ {i} (x), w)) \}$$
