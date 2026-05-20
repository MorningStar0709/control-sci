The force acting on bellows 1 in the x direction is $A \left( \overline { { P } } \mathrm { ~ + ~ } p _ { 1 } \right)$ and the force acting on bellows 2, in the negative x direction is $A \left( \overline { { P } } \mathrm { ~ + ~ } p _ { 2 } \right)$ The resultant force balances with kx, the equivalent. spring force of the corrugated sides of the bellows.

$$A \left(p _ {1} - p _ {2}\right) = k x$$

or

$$A \left[ P _ {1} (s) - P _ {2} (s) \right] = k X (s) \tag {4-40}$$

Referring to Equations (4–38) and (4–39), we see that

$$
\begin{array}{l} P _ {1} (s) - P _ {2} (s) = \left(\frac {1}{R _ {1} C s + 1} - \frac {1}{R _ {2} C s + 1}\right) P _ {i} (s) \\ = \frac {R _ {2} C s - R _ {1} C s}{(R _ {1} C s + 1) (R _ {2} C s + 1)} P _ {i} (s) \\ \end{array}
$$

By substituting this last equation into Equation (4–40) and rewriting, the transfer function $X ( s ) / P _ { i } ( s )$ is obtained as

$$\frac {X (s)}{P _ {i} (s)} = \frac {A}{k} \frac {\left(R _ {2} C - R _ {1} C\right) s}{\left(R _ {1} C s + 1\right) \left(R _ {2} C s + 1\right)} \tag {4-41}$$

The numerical values of average resistances $R _ { 1 }$ and $R _ { 2 }$ are

$$R _ {1} = \frac {d \Delta p}{d q _ {1}} = \frac {0 . 5 \times 1 0 ^ {5}}{3 \times 1 0 ^ {- 5}} = 0. 1 6 7 \times 1 0 ^ {1 0} \frac {\mathrm{N/m} ^ {2}}{\mathrm{kg/sec}}R _ {2} = \frac {d \Delta p}{d q _ {2}} = \frac {0 . 5 \times 1 0 ^ {5}}{1 . 5 \times 1 0 ^ {- 5}} = 0. 3 3 3 \times 1 0 ^ {1 0} \frac {\mathrm{N} / \mathrm{m} ^ {2}}{\mathrm{kg} / \mathrm{sec}}$$

The numerical value of capacitance C of each bellows is

$$C = \frac {V}{n R _ {\mathrm{air}} T} = \frac {5 \times 1 0 ^ {- 4}}{1 \times 2 8 7 \times (2 7 3 + 3 0)} = 5. 7 5 \times 1 0 ^ {- 9} \frac {\mathrm{kg}}{\mathrm{N} / \mathrm{m} ^ {2}}$$

where $R _ { \mathrm { a i r } } = 2 8 7 \mathrm { N } \mathrm { - } \mathrm { m } / \mathrm { k g }$ K. (See Problem A–4–3.) Consequently,

$$R _ {1} C = 0. 1 6 7 \times 1 0 ^ {1 0} \times 5. 7 5 \times 1 0 ^ {- 9} = 9. 6 0 \mathrm{sec}R _ {2} C = 0. 3 3 3 \times 1 0 ^ {1 0} \times 5. 7 5 \times 1 0 ^ {- 9} = 1 9. 2 \mathrm{sec}$$

By substituting the numerical values for A, k, $R _ { 1 } C _ { \cdot }$ , and $R _ { 2 } C$ into Equation (4–41), we obtain

$$\frac {X (s)}{P _ {i} (s)} = \frac {1 . 4 4 \times 1 0 ^ {- 7} s}{(9 . 6 s + 1) (1 9 . 2 s + 1)}$$

A–4–5. Draw a block diagram of the pneumatic controller shown in Figure 4–30.Then derive the transfer function of this controller. Assume that $R _ { d } \ll R _ { i }$ Assume also that the two bellows are identical..
