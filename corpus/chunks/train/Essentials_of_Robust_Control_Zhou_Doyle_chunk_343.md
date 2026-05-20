J _ {2} := \left[ \begin{array}{c c} (A - B _ {1} D _ {2 1} ^ {*} R _ {2} ^ {- 1} C _ {2}) ^ {*} & - C _ {2} ^ {*} R _ {2} ^ {- 1} C _ {2} \\ - B _ {1} (I - D _ {2 1} ^ {*} R _ {2} ^ {- 1} D _ {2 1}) B _ {1} ^ {*} & - (A - B _ {1} D _ {2 1} ^ {*} R _ {2} ^ {- 1} C _ {2}) \end{array} \right]
$$

belong to dom(Ric), and, moreover, $X _ { 2 } : = \operatorname { R i c } ( H _ { 2 } ) \geq 0$ and $Y _ { 2 } : = \operatorname { R i c } ( J _ { 2 } ) \geq 0$ . Define

$$F _ {2} := - R _ {1} ^ {- 1} (B _ {2} ^ {*} X _ {2} + D _ {1 2} ^ {*} C _ {1}), \quad L _ {2} := - (Y _ {2} C _ {2} ^ {*} + B _ {1} D _ {2 1} ^ {*}) R _ {2} ^ {- 1}$$

and

$$
A _ {F _ {2}} := A + B _ {2} F _ {2}, \quad C _ {1 F _ {2}} := C _ {1} + D _ {1 2} F _ {2}A _ {L _ {2}} := A + L _ {2} C _ {2}, \quad B _ {1 L _ {2}} := B _ {1} + L _ {2} D _ {2 1}\hat {A} _ {2} := A + B _ {2} F _ {2} + L _ {2} C _ {2}
G _ {c} (s) := \left[ \begin{array}{c c} A _ {F _ {2}} & I \\ \hline C _ {1 F _ {2}} & 0 \end{array} \right], \qquad G _ {f} (s) := \left[ \begin{array}{c c} A _ {L _ {2}} & B _ {1 L _ {2}} \\ \hline I & 0 \end{array} \right].
$$

Before stating the main theorem, we note the following fact:

Lemma 13.6 Let $U , V \in \mathcal { R } \mathcal { H } _ { \infty }$ be defined as

$$
U := \left[ \begin{array}{c c} A _ {F _ {2}} & B _ {2} R _ {1} ^ {- 1 / 2} \\ \hline C _ {1 F _ {2}} & D _ {1 2} R _ {1} ^ {- 1 / 2} \end{array} \right], \quad V := \left[ \begin{array}{c c} A _ {L _ {2}} & B _ {1 L _ {2}} \\ \hline R _ {2} ^ {- 1 / 2} C _ {2} & R _ {2} ^ {- 1 / 2} D _ {2 1} \end{array} \right].
$$

Then U is an inner and V is a co-inner, $U ^ { \sim } G _ { c } \in \mathcal { R } \mathcal { H } _ { 2 } ^ { \bot }$ , and $G _ { f } V ^ { \sim } \in \mathcal { R } \mathcal { H } _ { 2 } ^ { \bot }$ .

Proof. The proof uses standard manipulations of state-space realizations. From U we get

$$
U ^ {\sim} (s) = \left[ \begin{array}{c c} - A _ {F _ {2}} ^ {*} & - C _ {1 F _ {2}} ^ {*} \\ \hline R _ {1} ^ {- 1 / 2} B _ {2} ^ {*} & R _ {1} ^ {- 1 / 2} D _ {1 2} ^ {*} \end{array} \right].
$$

Then it is easy to compute

$$
U ^ {\sim} U = \left[ \begin{array}{c c c} - A _ {F _ {2}} ^ {*} & - C _ {1 F _ {2}} ^ {*} C _ {1 F _ {2}} & - C _ {1 F _ {2}} ^ {*} D _ {1 2} R _ {1} ^ {- 1 / 2} \\ 0 & A _ {F _ {2}} & B _ {2} R _ {1} ^ {- 1 / 2} \\ \hline R _ {1} ^ {- 1 / 2} B _ {2} ^ {*} & R _ {1} ^ {- 1 / 2} D _ {1 2} ^ {*} C _ {1 F _ {2}} & I \end{array} \right]

U ^ {\sim} G _ {c} = \left[ \begin{array}{c c c} - A _ {F _ {2}} ^ {*} & - C _ {1 F _ {2}} ^ {*} C _ {1 F _ {2}} & 0 \\ 0 & A _ {F _ {2}} & I \\ \hline R _ {1} ^ {- 1 / 2} B _ {2} ^ {*} & R _ {1} ^ {- 1 / 2} D _ {1 2} ^ {*} C _ {1 F _ {2}} & 0 \end{array} \right].
$$

Now do the similarity transformation

$$
\left[ \begin{array}{c c} I & - X _ {2} \\ 0 & I \end{array} \right]
$$

on the states of the preceding transfer matrices and note that
