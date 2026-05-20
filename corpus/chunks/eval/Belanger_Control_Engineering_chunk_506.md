$$\dot {\mathbf {x}} = A \widehat {\mathbf {x}} + B _ {2} \mathbf {u} + G (\mathbf {y} - D _ {2 2} \mathbf {u} - C _ {2} \widehat {\mathbf {x}})$$

which leads to

$$\tilde {\mathbf {x}} = (A - G C _ {2}) \tilde {\mathbf {x}} + (B _ {1} - G D _ {2 1}) \mathbf {w}. \tag {8.71}$$

From Equations 8.69 and 8.70, we deduce that $\mathbf{z}$ is of the form

$$\mathbf {z} = T _ {1} \mathbf {w} + T _ {2} \nu .$$

From Equations 8.68 and 8.71, we have

$$\pmb {\nu} = T _ {w v} \mathbf {w}$$

so that

$$\mathbf {z} = (T _ {1} + T _ {2} T _ {\mathbf {w} \nu}) \mathbf {w}. \tag {8.72}$$

Clearly,

$$
\begin{array}{l} T _ {\mathbf {w z}} ^ {T} (- s) T _ {\mathbf {w z}} (s) = T _ {1} ^ {T} (- s) T _ {1} (s) + T _ {1} ^ {T} (- s) T _ {2} (s) T _ {\mathbf {w} \nu} (s) \\ + T _ {\mathbf {w} \nu} ^ {T} (- s) T _ {2} ^ {T} (- s) T _ {1} (s) + T _ {\mathbf {w} \nu} ^ {T} (- s) T _ {2} ^ {T} (- s) T _ {2} (s) T _ {\mathbf {w} \nu} (s). \tag {8.73} \\ \end{array}
$$

Key results in Doyle et al. [4] are that (i) $T_2^T(-s)T_2(s) = I$ and (ii) the Parseval integrals of the two middle terms in Equation 8.73 are zero. Therefore,

$$\| T _ {\mathbf {w z}} \| _ {2} ^ {2} = \| T _ {1} \| _ {2} ^ {2} + \| T _ {\mathbf {w} \nu} \| ^ {2}. \tag {8.74}$$

Note that $T_{1}$ is the w-to-z transmissions of the system

$$
\begin{array}{l} \dot {\mathbf {x}} = (A - B _ {2} K) \mathbf {x} + B _ {1} \mathbf {w} \\ \mathbf {z} = (C _ {1} - D _ {1 2} K) \mathbf {x} \tag {8.75} \\ \end{array}
$$

which is precisely the $T_{wz}$ for the case of full state feedback. This transmission is not a function of G, so the minimization is carried over the second term in Equation 8.74.

From Equations 8.68 and 8.71,

$$T _ {w \nu} = K (s I - A + G C _ {2}) ^ {- 1} (B _ {1} - G D _ {2 1})$$

and

$$\operatorname{tr} T _ {\mathbf {w} \nu} ^ {T} (- s) T _ {\mathbf {w} \nu} (s) =\operatorname{tr} \left(B _ {1} - G D _ {2 1}\right) ^ {T} (- s I - A + G C _ {2}) ^ {- T} K ^ {T} K.(s I - A + G C _ {2}) ^ {- 1} \left(B _ {1} - G D _ {2 1}\right).$$

The fact that $\operatorname{tr} AB = \operatorname{tr} BA$ allows us to write

$$\operatorname{tr} T _ {\mathbf {w} \nu} ^ {T} (- s) T _ {\mathbf {w} \nu} (s) =\operatorname{tr} K (s I - A + G C _ {2}) ^ {- 1} \left(B _ {1} - G D _ {2 1}\right).\left(B _ {1} - G D _ {2 1}\right) ^ {T} \left(s I - A + G C _ {2}\right) ^ {- T} K ^ {T}.$$

Because $\operatorname{tr} A^T = \operatorname{tr} A$ ,

$$\operatorname{tr} T _ {\mathbf {w} \nu} ^ {T} (- s) T _ {\mathbf {w} \nu} (s) =\operatorname{tr} K (- s I - A + G C _ {2}) ^ {- T} \left(B _ {1} - G D _ {2 1}\right) \cdot(B _ {1} - G D _ {2 1}) ^ {T} (s I - A + G C _ {2}) ^ {- T} K ^ {T}. \tag {8.76}$$
