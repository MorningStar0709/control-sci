For the case of full state feedback, the corresponding quantity (see Equation 8.75) was

$$\operatorname{tr} T _ {\mathbf {w z}} ^ {T} (- s) T _ {\mathbf {w z}} (s) =\operatorname{tr} B _ {1} ^ {T} (- s I - A + B _ {2} K) ^ {- T} \left(C _ {1} - D _ {1 2} K\right) ^ {T}.\left(C _ {1} - D _ {1 2} K\right) \left(s I - A + B _ {2} K\right) ^ {- 1} B _ {1}. \tag {8.77}$$

It is clear that Equation 8.76 is obtained from Equation 8.77 by making the following substitutions: $K^T$ for $B_1, A^T$ for $A, G^T$ for $K, C_2^T$ for $B_2, B_1^T$ for $C_1$ , and $D_{21}^T$ for $D_{12}$ . We solve for $G$ as we solved for $K$ , as the results of an LQ problem. Just as $K$ did not depend on $B_1$ , so $G$ is independent of $K$ .

The solution process can be summarized as follows. The system is

$$\dot {\mathbf {x}} = A \mathbf {x} + B _ {1} \mathbf {w} + B _ {2} \mathbf {u}\mathbf {z} = C _ {1} \mathbf {x} + D _ {1 2} \mathbf {u}\mathbf {y} = C _ {2} \mathbf {x} + D _ {2 1} \mathbf {w} + D _ {2 2} \mathbf {u}.$$

1. The control gain. Solve the LQ control problem for

$$
\dot {\mathbf {x}} = A \mathbf {x} + B _ {2} \mathbf {u}
J = \int_ {0} ^ {\infty} [ \mathbf {x} ^ {T} \mathbf {u} ^ {T} ] \left[ \begin{array}{c c} C _ {1} ^ {T} C _ {1} & C _ {1} ^ {T} D _ {1 2} \\ D _ {1 2} ^ {T} C _ {1} & D _ {1 2} ^ {T} D _ {1 2} \end{array} \right] \left[ \begin{array}{c} \mathbf {x} \\ \mathbf {u} \end{array} \right] d t
$$

and obtain the gain matrix K.

2. The filter. Solve the LQ estimation problem (Kalman filter) for

$$\dot {\mathbf {x}} = A \mathbf {x} + \mathbf {w}\mathbf {y} = C _ {2} \mathbf {x} + \mathbf {v}$$

with the noise intensity matrix

$$
\operatorname{E} \left\{\left[ \begin{array}{l} \mathbf {w} \\ \mathbf {v} \end{array} \right] [ \mathbf {w} ^ {T} \mathbf {v} ^ {T} ] \right\} = \left[ \begin{array}{c c} B _ {1} B _ {1} ^ {T} & B _ {1} D _ {2 1} ^ {T} \\ D _ {2 1} B _ {1} ^ {T} & D _ {2 1} D _ {2 1} ^ {T} \end{array} \right]
$$

and obtain the filter gain G.

3. The controller.

$$\dot {\widehat {\mathbf {x}}} = A \widehat {\mathbf {x}} + B _ {2} \mathbf {u} + G (\mathbf {y} - D _ {2 2} \mathbf {u} - C _ {2} \widehat {\mathbf {x}})$$

or

$$\dot {\widehat {\mathbf {x}}} = (A - B _ {2} K - G C _ {2} + G D _ {2 2} K) \widehat {\mathbf {x}} + G \mathbf {y}\mathbf {u} = - K \widehat {\mathbf {x}}.$$

4. The optimal norm.

$$\min \| T _ {\mathbf {w z}} \| _ {2} ^ {2} = \| T _ {c} \| _ {2} ^ {2} + \| T _ {f} \| _ {2} ^ {2}$$

where $T_{c}$ is the transmission of

$$\dot {\mathbf {x}} = (A - B _ {2} K) \mathbf {x} + B _ {1} \mathbf {w}\mathbf {z} = \left(C _ {1} - D _ {1 2} K\right) \mathbf {x}$$

and $T_{f}$ is the input–output transmission of

$$\tilde {\mathbf {x}} = (A - G C _ {2}) \tilde {\mathbf {x}} + (B _ {1} - G D _ {2 1}) \mathbf {w}\nu = K \widetilde {\mathbf {x}}.$$
