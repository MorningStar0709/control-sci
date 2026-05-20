# 2.5 Changing Coordinates In State-Space Models

Consider the discrete-time system (2.16). We will now discuss how new coordinates can be introduced. Assume that T is a nonsingular matrix and define a new state vector $z(k) = Tx(k)$ . Then

$$
\begin{array}{l} z (k + 1) = T x (k + 1) = T \Phi x (k) + T \Gamma u (k) = T \Phi T ^ {- 1} z (k) + T \Gamma u (k) \\ = \tilde {\Phi} z (k) + \tilde {\Gamma} u (k) \\ \end{array}
$$

and

$$y (k) = C x (k) + D u (k) = C T ^ {- 1} z (k) + D u (k) = \tilde {C} z (k) + \bar {D} u (k)$$

The state-space representation thus depends on the coordinate system chosen to represent the state. The invariants under the transformation are of interest.

THEOREM 2.2 INVARIANCE OF THE CHARACTERISTIC EQUATION The characteristic equation

$$\det (\lambda I - \Phi) = 0$$

is invariant when new states are introduced through the nonsingular transformation matrix T.

Proof.

$$
\begin{array}{l} \det (\lambda I - \bar {\Phi}) = \det (\lambda T T ^ {- 1} - T \Phi T ^ {- 1}) = \det T \det (\lambda I - \Phi) \det T ^ {- 1} \\ = \det (\lambda I - \Phi) \\ \end{array}
$$

To find a transformation matrix is the same as solving for the $n^{2}$ elements of T from the linear set of equations

$$T \Phi = \tilde {\Phi} T$$

Coordinates can be chosen to give simple forms of the system equations.
