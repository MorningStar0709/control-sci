# 14.5 An Optimal Controller

To offer a general idea about the appearance of an optimal controller, we shall give in the following (without proof) the conditions under which an optimal controller exists and an explicit formula for an optimal controller.

Theorem 14.6 There exists an admissible controller such that $\| T _ { z w } \| _ { \infty } \leq \gamma \ i f f$ the following three conditions hold:

(i) There exists a full column rank matrix

$$
\left[ \begin{array}{l} X _ {\infty 1} \\ X _ {\infty 2} \end{array} \right] \in \mathbb {R} ^ {2 n \times n}
$$

such that

$$
H _ {\infty} \left[ \begin{array}{l} X _ {\infty 1} \\ X _ {\infty 2} \end{array} \right] = \left[ \begin{array}{l} X _ {\infty 1} \\ X _ {\infty 2} \end{array} \right] T _ {X}, \text {Re} \lambda_ {i} (T _ {X}) \leq 0 \forall i
$$

and

$$X _ {\infty 1} ^ {*} X _ {\infty 2} = X _ {\infty 2} ^ {*} X _ {\infty 1};$$

(ii) There exists a full column rank matrix

$$
\left[ \begin{array}{l} Y _ {\infty 1} \\ Y _ {\infty 2} \end{array} \right] \in \mathbb {R} ^ {2 n \times n}
$$

such that

$$
J _ {\infty} \left[ \begin{array}{l} Y _ {\infty 1} \\ Y _ {\infty 2} \end{array} \right] = \left[ \begin{array}{l} Y _ {\infty 1} \\ Y _ {\infty 2} \end{array} \right] T _ {Y}, \text {   Re   } \lambda_ {i} (T _ {Y}) \leq 0 \forall i
$$

and

$$Y _ {\infty 1} ^ {*} Y _ {\infty 2} = Y _ {\infty 2} ^ {*} Y _ {\infty 1};$$

(iii)

$$
\left[ \begin{array}{c c} X _ {\infty 2} ^ {*} X _ {\infty 1} & \gamma^ {- 1} X _ {\infty 2} ^ {*} Y _ {\infty 2} \\ \gamma^ {- 1} Y _ {\infty 2} ^ {*} X _ {\infty 2} & Y _ {\infty 2} ^ {*} Y _ {\infty 1} \end{array} \right] \geq 0.
$$

Moreover, when these conditions hold, one such controller is

$$K _ {\mathrm{opt}} (s) := C _ {K} (s E _ {K} - A _ {K}) ^ {+} B _ {K}$$

where

$$E _ {K} := Y _ {\infty 1} ^ {*} X _ {\infty 1} - \gamma^ {- 2} Y _ {\infty 2} ^ {*} X _ {\infty 2}B _ {K} := Y _ {\infty 2} ^ {*} C _ {2} ^ {*}C _ {K} := - B _ {2} ^ {*} X _ {\infty 2}{A _ {K}} {:=} {E _ {K} T _ {X} - B _ {K} C _ {2} X _ {\infty 1} = T _ {Y} ^ {*} E _ {K} + Y _ {\infty 1} ^ {*} B _ {2} C _ {K}.}$$
