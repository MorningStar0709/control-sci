$$
\begin{array}{l} \frac {E _ {o} (s)}{E _ {i} (s)} = \frac {\frac {1}{C s} \frac {1}{C s} + R _ {1} \left(\frac {1}{C s} + \frac {1}{C s} + R _ {2}\right)}{R _ {1} \left(\frac {1}{C s} + \frac {1}{C s} + R _ {2}\right) + \frac {1}{C s} \frac {1}{C s} + R _ {2} \frac {1}{C s}} \\ = \frac {R _ {1} C R _ {2} C s ^ {2} + 2 R _ {1} C s + 1}{R _ {1} C R _ {2} C s ^ {2} + (2 R _ {1} C + R _ {2} C) s + 1} \\ \end{array}
$$

Figure 3–26 Operationalamplifier circuit.   
![](image/a2c84041a557479f5ac70a9ed2a82791a908b91b4df536555b79cc73f934e481.jpg)

<details>
<summary>text_image</summary>

R₁
R₁
A
-
+
R₂
B
C
eᵢ
eₒ
</details>

A–3–6. Obtain the transfer function $E _ { o } ( s ) / E _ { i } ( s )$ of the op-amp circuit shown in Figure 3–26.

Solution. The voltage at point A is

$$e _ {A} = \frac {1}{2} \left(e _ {i} - e _ {o}\right) + e _ {o}$$

The Laplace-transformed version of this last equation is

$$E _ {A} (s) = \frac {1}{2} \left[ E _ {i} (s) + E _ {o} (s) \right]$$

The voltage at point B is

$$E _ {B} (s) = \frac {\frac {1}{C s}}{R _ {2} + \frac {1}{C s}} E _ {i} (s) = \frac {1}{R _ {2} C s + 1} E _ {i} (s)$$

Since $\big [ E _ { B } ( s ) - E _ { A } ( s ) \big ] K = E _ { o } ( s )$ and $K \gg 1$ we must have, $E _ { A } ( s ) = E _ { B } ( s )$ Thus.

$$\frac {1}{2} \left[ E _ {i} (s) + E _ {o} (s) \right] = \frac {1}{R _ {2} C s + 1} E _ {i} (s)$$

Hence

$$\frac {E _ {o} (s)}{E _ {i} (s)} = - \frac {R _ {2} C s - 1}{R _ {2} C s + 1} = - \frac {s - \frac {1}{R _ {2} C}}{s + \frac {1}{R _ {2} C}}$$

A–3–7. Obtain the transfer function $E _ { o } ( s ) / E _ { i } ( s )$ of the op-amp system shown in Figure 3–27 in terms of complex impedances $Z _ { 1 } , Z _ { 2 } , Z _ { 3 }$ , and $Z _ { 4 }$ . Using the equation derived, obtain the transfer function $E _ { o } ( s ) / E _ { i } ( s )$ of the op-amp system shown in Figure 3–26.

Solution. From Figure 3–27, we find

$$\frac {E _ {i} (s) - E _ {A} (s)}{Z _ {3}} = \frac {E _ {A} (s) - E _ {o} (s)}{Z _ {4}}$$

Figure 3–27 Operationalamplifier circuit.   
![](image/36d181a9f04ae5de81ed7e1f67cbd9c494205e681e0e1491bce8927b8a5f58a4.jpg)

<details>
<summary>text_image</summary>

Z₄
Z₃ A
-
Z₂ B +
eᵢ eₒ
Z₁
</details>

or

$$E _ {i} (s) - \left(1 + \frac {Z _ {3}}{Z _ {4}}\right) E _ {A} (s) = - \frac {Z _ {3}}{Z _ {4}} E _ {o} (s) \tag {3-39}$$

Since

$$E _ {A} (s) = E _ {B} (s) = \frac {Z _ {1}}{Z _ {1} + Z _ {2}} E _ {i} (s) \tag {3-40}$$

by substituting Equation (3–40) into Equation (3–39), we obtain

$$\left[ \frac {Z _ {4} Z _ {1} + Z _ {4} Z _ {2} - Z _ {4} Z _ {1} - Z _ {3} Z _ {1}}{Z _ {4} (Z _ {1} + Z _ {2})} \right] E _ {i} (s) = - \frac {Z _ {3}}{Z _ {4}} E _ {o} (s)$$
