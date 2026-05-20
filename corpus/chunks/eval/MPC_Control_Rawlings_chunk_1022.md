# Exercise C.4: Basic minmax result

Consider the following two minmax optimization problems in two variables

$$\inf _ {x \in \mathbb {X}} \sup _ {y \in \mathbb {Y}} V (x, y) \quad \sup _ {y \in \mathbb {Y}} \inf _ {x \in \mathbb {X}} V (x, y)$$

in which $x \in \mathbb { X } \subseteq \mathbb { R } ^ { n } , y \in \mathbb { Y } \subseteq \mathbb { R } ^ { m }$ , and $V : \mathbb { X } \times \mathbb { Y } \to \mathbb { R }$ .

(a) Show that the values are ordered as follows

$$\inf _ {x \in \mathbb {X}} \sup _ {y \in \mathbb {Y}} V (x, y) \geq \sup _ {y \in \mathbb {Y}} \inf _ {x \in \mathbb {X}} V (x, y)$$

or, if the solutions to the problems exist,

$$\min _ {x \in \mathbb {X}} \max _ {y \in \mathbb {Y}} V (x, y) \geq \max _ {y \in \mathbb {Y}} \min _ {x \in \mathbb {X}} V (x, y)$$

A handy mnemonic for this result is that the player who goes first (inner problem) has the advantage.9

(b) Use your results to order these three problems

$$\sup _ {x \in \mathbb {X}} \inf _ {y \in \mathbb {Y}} \sup _ {z \in \mathbb {Z}} V (x, y, z) \qquad \inf _ {y \in \mathbb {Y}} \sup _ {z \in \mathbb {Z}} \sup _ {x \in \mathbb {X}} V (x, y, z) \qquad \sup _ {z \in \mathbb {Z}} \sup _ {x \in \mathbb {X}} \inf _ {y \in \mathbb {Y}} V (x, y, z)$$
