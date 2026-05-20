$$\mathbf {x} ^ {\mathsf {T}} (\mathbf {A} ^ {\mathsf {T}} \mathbf {P} + \mathbf {P A}) \mathbf {x} - \mathbf {x} ^ {\mathsf {T}} \mathbf {P B R} ^ {- 1} \mathbf {N B} ^ {\mathsf {T}} \mathbf {P x} - \mathbf {x} ^ {\mathsf {T}} \mathbf {P B N R} ^ {- 1} \mathbf {B} ^ {\mathsf {T}} \mathbf {P x} < 0\mathbf {x} ^ {\mathsf {T}} (\mathbf {A} ^ {\mathsf {T}} \mathbf {P} + \mathbf {P A} - \mathbf {P B R} ^ {- 1} \mathbf {N B} ^ {\mathsf {T}} \mathbf {P} - \mathbf {P B N R} ^ {- 1} \mathbf {B} ^ {\mathsf {T}} \mathbf {P}) \mathbf {x} < 0$$

Since we assumed R is diagonal, we can swap the order of $\mathbf { R } ^ { - 1 } \mathbf { N }$ in $\mathbf { P B R ^ { - 1 } N B ^ { \top } P }$ .

$$
\begin{array}{l} \mathbf {x} ^ {\top} \left(\mathbf {A} ^ {\top} \mathbf {P} + \mathbf {P A} - \mathbf {P B N R} ^ {- 1} \mathbf {B} ^ {\top} \mathbf {P} - \mathbf {P B N R} ^ {- 1} \mathbf {B} ^ {\top} \mathbf {P}\right) \mathbf {x} <   0 \\ \mathbf {x} ^ {\mathsf {T}} (\mathbf {A} ^ {\mathsf {T}} \mathbf {P} + \mathbf {P A} - \mathbf {P B 2 N R} ^ {- 1} \mathbf {B} ^ {\mathsf {T}} \mathbf {P}) \mathbf {x} <   0 \\ \end{array}
$$

Substitute in the CARE $\mathbf { A } ^ { \mathsf { T } } \mathbf { P } + \mathbf { P A } = \mathbf { P B } \mathbf { R } ^ { - 1 } \mathbf { B } ^ { \mathsf { T } } \mathbf { P } - \mathbf { Q } .$ .

$$
\begin{array}{l} \mathbf {x} ^ {\mathsf {T}} (\mathbf {P B R} ^ {- 1} \mathbf {B} ^ {\mathsf {T}} \mathbf {P} - \mathbf {Q} - \mathbf {P B 2 N R} ^ {- 1} \mathbf {B} ^ {\mathsf {T}} \mathbf {P}) \mathbf {x} <   0 \\ \mathbf {x} ^ {\mathsf {T}} (\mathbf {P B} (\mathbf {I} - 2 \mathbf {N}) \mathbf {R} ^ {- 1} \mathbf {B} ^ {\mathsf {T}} \mathbf {P} - \mathbf {Q}) \mathbf {x} <   0 \\ \mathbf {x} ^ {\mathsf {T}} (\mathbf {Q} - \mathbf {P B} (\mathbf {I} - 2 \mathbf {N}) \mathbf {R} ^ {- 1} \mathbf {B} ^ {\mathsf {T}} \mathbf {P}) \mathbf {x} > 0 \\ \end{array}
$$

This inequality is satisfied if and only if

$$\mathbf {Q} - \mathbf {P B} (\mathbf {I} - 2 \mathbf {N}) \mathbf {R} ^ {- 1} \mathbf {B} ^ {\top} \mathbf {P} > \mathbf {0} \tag {B.2}$$

which is satisfied for $\mathbf { N } _ { i , i } ~ > ~ 0 . 5$ . Thus, for each input, LQR allows one-half gain reduction and has infinite gain margin.
