Also, if Ackermann’s formula given by Equation (10–65) is to be used, then it should be modified to

$$
\mathbf {K} _ {e} = \phi (\mathbf {A} _ {b b}) \left[ \begin{array}{c} \mathbf {A} _ {a b} \\ \mathbf {A} _ {a b} \mathbf {A} _ {b b} \\ \cdot \\ \cdot \\ \cdot \\ \mathbf {A} _ {a b} \mathbf {A} _ {b b} ^ {n - 3} \\ \mathbf {A} _ {a b} \mathbf {A} _ {b b} ^ {n - 2} \end{array} \right] ^ {- 1} \left[ \begin{array}{l} 0 \\ 0 \\ \cdot \\ \cdot \\ \cdot \\ 0 \\ 1 \end{array} \right] \tag {10-97}
$$

where

$$\phi (\mathbf {A} _ {b b}) = \mathbf {A} _ {b b} ^ {n - 1} + \hat {\alpha} _ {1} \mathbf {A} _ {b b} ^ {n - 2} + \dots + \hat {\alpha} _ {n - 2} \mathbf {A} _ {b b} + \hat {\alpha} _ {n - 1} \mathbf {I}$$

Observed-State Feedback Control System with Minimum-Order Observer. For the case of the observed-state feedback control system with full-order state observer, we have shown that the closed-loop poles of the observed-state feedback control system consist of the poles due to the pole-placement design alone, plus the poles due to the observer design alone. Hence, the pole-placement design and the full-order observer design are independent of each other.

For the observed-state feedback control system with minimum-order observer, the same conclusion applies. The system characteristic equation can be derived as

$$\left| s \mathbf {I} - \mathbf {A} + \mathbf {B K} \right| \left| s \mathbf {I} - \mathbf {A} _ {b b} + \mathbf {K} _ {e} \mathbf {A} _ {a b} \right| = 0 \tag {10-98}$$

(See Problem A–10–11 for the details.) The closed-loop poles of the observed-state feedback control system with a minimum-order observer comprise the closed-loop poles due to pole placement Cthe eigenvalues of matrix $\mathbf { \left( A - B K \right) }$ D and the closed-loop poles due to the minimum-order observer Cthe eigenvalues of matrix $\left( { \bf A } _ { b b } - { \bf K } _ { e } { \bf A } _ { a b } \right) ]$ .Therefore, the pole-placement design and the design of the minimum-order observer are independent of each other.

Determining Observer Gain Matrix ${ \bf K } _ { e }$ with MATLAB. Because of the duality of pole-placement and observer design, the same algorithm can be applied to both the pole-placement problem and the observer-design problem. Thus, the commands acker and place can be used to determine the observer gain matrix $\mathbf { K } _ { e }$ .
