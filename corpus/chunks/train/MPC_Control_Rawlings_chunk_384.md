# 3.4.1 Introduction

To proceed realistically we need to sacrifice optimality for simplicity. Many methods for doing so have been proposed in the literature. We outline next one procedure that achieves this objective and that yields robust MPC by solving online an optimal control problem that has the same order of complexity as that employed for conventional MPC. We simplify the decision variable that, ideally, is a policy by replacing it with a finite-dimensional parameterization that consists of an openloop control sequence and a simple local feedback controller. In addition, we replace the tube, whose exact determination is difficult, by a simply determined outer-bounding tube. The underlying idea is quite simple. We generate the “center” of the tube by using conventional MPC with tighter constraints on the nominal system, and restrict the “size” of the tube by using local feedback that attempts to steer all trajectories of the uncertain system to the central trajectory. The resultant controller may be regarded as a “two degrees of freedom” controller. The local feedback around the nominal trajectory is the inner loop and attenuates disturbances while MPC is used in the outer loop.

In this section we address robust MPC of constrained linear systems. To do so, we make use of some concepts in set algebra. Given two subsets A and B of Rn, we define set addition, set subtraction (sometimes called Minkowski or Pontryagin set subtraction), set multiplication and Hausdorff distance between two sets as follows.

Definition 3.13 (Set algebra and Hausdorff distance).

(a) Set addition: A ⊕ $B : = \{ a + b \mid a \in A , b \in B \}$ .   
(b) Set subtraction: $A \ominus B : = \{ x \in \mathbb { R } ^ { n } \mid \{ x \} \oplus B \subseteq A \}$ .   
(c) Set multiplication: Let $K \in \mathbb { R } ^ { m \times n }$ . Then $K A : = \{ K a \mid a \in A \}$ .   
(d) The Hausdorff distance $d _ { H } ( \cdot )$ between two subsets A and B of $\mathbb { R } ^ { n }$

is defined by

$$d _ {H} (A, B) := \max \{\sup _ {a \in A} d (a, B), \sup _ {b \in B} d (b, A) \}$$

in which $d ( x , S )$ denotes the distance of a point $x \in \mathbb { R } ^ { n }$ from a set $S \subset \mathbb { R } ^ { n }$ and is defined by

$$d (x, S) := \inf _ {y} \{d (x, y) \mid y \in S \} \quad d (x, y) := | x - y |$$
