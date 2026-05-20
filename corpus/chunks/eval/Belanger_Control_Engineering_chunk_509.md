The $H_{\infty}$ solution revolves around the two Hamiltonian matrices

$$
H _ {c} = \left[ \begin{array}{c c} A & \gamma^ {2} B _ {1} B _ {1} ^ {T} - B _ {2} B _ {2} ^ {T} \\ - C _ {1} ^ {T} C _ {1} & - A ^ {T} \end{array} \right] \tag {8.78}
$$

and

$$
H _ {f} = \left[ \begin{array}{c c} A ^ {T} & \gamma^ {2} C _ {1} ^ {T} C _ {1} - C _ {2} ^ {T} C _ {2} \\ - B _ {1} B _ {1} ^ {T} & - A \end{array} \right]. \tag {8.79}
$$

The technical assumptions are:

(i) $(A, B_2)$ is stabilizable and $(C_2, A)$ is detectable.   
(ii) $D_{12}^{T}D_{12}$ and $D_{21}D_{21}^{T}$ are nonsingular.

In Doyle et al. [4], a third assumption is:

(iiiia) $(A, B_{1})$ is stabilizable and $(C_{1}, A)$ is detectable.

In [5], the third assumption is:

(iiib) $\left[\begin{array}{cc}A-j\omega I & B_2 \\ C_1 & D_{12}\end{array}\right]$ and $\left[\begin{array}{cc}A^T-j\omega I & C_2^T \\ B_1^T & D_{21}^T\end{array}\right]$ have full column rank for all $\omega$ .

Both (iiiia) and (iiib) disallow uncontrollable modes of $(A, B_1)$ and unobservable modes of $(C_1, A)$ on the imaginary axis. However, (iiib) would allow open RHP uncontrollable or unobservable modes, whereas (iiiia) would not. On the other hand, (iiib) states that $(A, B_2, C_1, D_{12})$ and $(A^T, C_2^T, B_1^T, D_{21}^T)$ shall have no transmission zeros on the $j$ -axis, whereas (iiiia) has nothing direct to say about zeros.

The theorem is the same in both Doyle et al. [4] and The Mathworks [5].

■ Theorem 8.3 There exists an admissible controller such that $\| T_{\mathbf{wz}} \|_{\infty} < \gamma$ if, and only if:

(i) $H_{c}$ and $H_{f}$ both satisfy the complementarity and stability conditions.   
(ii) The Riccati-equation solutions $P_{c}$ and $P_{f}$ associated with $H_{c}$ and $H_{f}$ are positive semidefinite;   
(iii) The spectral radius (i.e., maximum eigenvalue) $\rho(P_c P_f) < \gamma^{-2}$ .

When these conditions hold, one such controller is

$$\tilde {\mathbf {x}} = A _ {c} \widehat {\mathbf {x}} + G _ {c} \mathbf {y}\mathbf {u} = - K _ {c} \widehat {\mathbf {x}} \tag {8.80}$$

where

$$A _ {c} = A + (\gamma^ {2} B _ {1} B _ {1} ^ {T} - B _ {2} B _ {2} ^ {T}) P _ {c} - (I - \gamma^ {2} P _ {f} P _ {c}) ^ {- 1} P _ {f} C _ {2} ^ {T} C _ {2} \tag {8.81}G _ {c} = (I - \gamma^ {2} P _ {f} P _ {c}) ^ {- 1} P _ {f} C _ {2} ^ {T} \tag {8.82}K _ {c} = B _ {2} ^ {T} P _ {c}. \tag {8.83}$$
