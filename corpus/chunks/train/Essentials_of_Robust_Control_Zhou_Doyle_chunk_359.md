$$X _ {\infty} A + A ^ {*} X _ {\infty} + X _ {\infty} (B _ {1} B _ {1} ^ {*} / \gamma^ {2} - B _ {2} B _ {2} ^ {*}) X _ {\infty} + C _ {1} ^ {*} C _ {1} = 0 \tag {14.14}$$

and

$$A + (B _ {1} B _ {1} ^ {*} / \gamma^ {2} - B _ {2} B _ {2} ^ {*}) X _ {\infty} = - X _ {\infty} ^ {- 1} (A + C _ {1} ^ {*} C _ {1} X _ {\infty} ^ {- 1}) X _ {\infty} = - X _ {\infty} ^ {- 1} (A + C _ {1} ^ {*} C _ {1} Y / \gamma^ {2}) X _ {\infty}$$

is stable.

Similarly, applying Theorem 14.4 to part (ii) of Lemma 14.3, we conclude that there exists an $X > X _ { 1 } > 0$ such that

$$X A + A ^ {*} X + X B _ {1} B _ {1} ^ {*} X / \gamma^ {2} + C _ {1} ^ {*} C _ {1} - \gamma^ {2} C _ {2} ^ {*} C _ {2} = 0$$

and $A + B _ { 1 } B _ { 1 } ^ { * } X / \gamma ^ { 2 }$ is antistable. Let $Y _ { \infty } : = \gamma ^ { 2 } X ^ { - 1 }$ , we have

$$A Y _ {\infty} + Y _ {\infty} A ^ {*} + Y _ {\infty} (C _ {1} ^ {*} C _ {1} / \gamma^ {2} - C _ {2} ^ {*} C _ {2}) Y _ {\infty} + B _ {1} B _ {1} ^ {*} = 0 \tag {14.15}$$

and $A + ( C _ { 1 } ^ { * } C _ { 1 } / \gamma ^ { 2 } - C _ { 2 } ^ { * } C _ { 2 } ) Y _ { \infty }$ is stable.

Finally, note that the rank condition in part (iii) of Lemma 14.3 is automatically satisfied by $r \geq n$ , and

$$
\left[ \begin{array}{c c} \gamma Y _ {\infty} ^ {- 1} & I _ {n} \\ I _ {n} & \gamma X _ {\infty} ^ {- 1} \end{array} \right] = \left[ \begin{array}{c c} X / \gamma & I _ {n} \\ I _ {n} & Y / \gamma \end{array} \right] > \left[ \begin{array}{c c} X _ {1} / \gamma & I _ {n} \\ I _ {n} & Y _ {1} / \gamma \end{array} \right] \geq 0
$$

or $\rho ( X _ { \infty } Y _ { \infty } ) < \gamma ^ { 2 } .$ .

✷

Proof of Theorem 14.1: To complete the proof, we only need to show that the controller $K _ { \mathrm { s u b } }$ given in Theorem 14.1 renders $\| T _ { z w } \| _ { \infty } < \gamma$ . Note that the closed-loop transfer function with $K _ { \mathrm { s u b } }$ is given by

$$
T _ {z w} = \left[ \begin{array}{c c c} A & B _ {2} F _ {\infty} & B _ {1} \\ - Z _ {\infty} L _ {\infty} C _ {2} & \hat {A} _ {\infty} & - Z _ {\infty} L _ {\infty} D _ {2 1} \\ \hline C _ {1} & D _ {1 2} F _ {\infty} & 0 \end{array} \right] =: \left[ \begin{array}{c c} A _ {c c} & B _ {c c} \\ \hline C _ {c c} & D _ {c c} \end{array} \right].
$$

Define

$$
P = \left[ \begin{array}{c c} \gamma^ {2} Y _ {\infty} ^ {- 1} & - \gamma^ {2} Y _ {\infty} ^ {- 1} Z _ {\infty} ^ {- 1} \\ - \gamma^ {2} (Z _ {\infty} ^ {*}) ^ {- 1} Y _ {\infty} ^ {- 1} & \gamma^ {2} Y _ {\infty} ^ {- 1} Z _ {\infty} ^ {- 1} \end{array} \right].
$$

Then it is easy to show that $P > 0$ and

$$P A _ {c} + A _ {c} ^ {*} P + P B _ {c} B _ {c} ^ {*} P / \gamma^ {2} + C _ {c} ^ {*} C _ {c} = 0.$$

Moreover,
