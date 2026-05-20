# 3.4 Operations on Systems

In this section, we present some facts about system interconnection. Since these proofs are straightforward, we will leave the details to the reader.

Suppose that $G _ { 1 }$ and $G _ { 2 }$ are two subsystems with state-space representations:

$$
G _ {1} = \left[ \begin{array}{c c} A _ {1} & B _ {1} \\ \hline C _ {1} & D _ {1} \end{array} \right], \quad G _ {2} = \left[ \begin{array}{c c} A _ {2} & B _ {2} \\ \hline C _ {2} & D _ {2} \end{array} \right].
$$

Then the series or cascade connection of these two subsystems is a system with the output of the second subsystem as the input of the first subsystem, as shown in the following diagram:

![](image/e1c7a326b0a7783fc22bde24aecf0442d422185846597b28056c94418420836c.jpg)

This operation in terms of the transfer matrices of the two subsystems is essentially the product of two transfer matrices. Hence, a representation for the cascaded system can be obtained as

$$
\begin{array}{l} G _ {1} G _ {2} = \left[ \begin{array}{c c} A _ {1} & B _ {1} \\ \hline C _ {1} & D _ {1} \end{array} \right] \left[ \begin{array}{c c} A _ {2} & B _ {2} \\ \hline C _ {2} & D _ {2} \end{array} \right] \\ = \left[ \begin{array}{c c c} A _ {1} & B _ {1} C _ {2} & B _ {1} D _ {2} \\ 0 & A _ {2} & B _ {2} \\ \hline C _ {1} & D _ {1} C _ {2} & D _ {1} D _ {2} \end{array} \right] = \left[ \begin{array}{c c c} A _ {2} & 0 & B _ {2} \\ B _ {1} C _ {2} & A _ {1} & B _ {1} D _ {2} \\ \hline D _ {1} C _ {2} & C _ {1} & D _ {1} D _ {2} \end{array} \right]. \\ \end{array}
$$

Similarly, the parallel connection or the addition of $G _ { 1 }$ and $G _ { 2 }$ can be obtained as

$$
G _ {1} + G _ {2} = \left[ \begin{array}{c c} A _ {1} & B _ {1} \\ \hline C _ {1} & D _ {1} \end{array} \right] + \left[ \begin{array}{c c} A _ {2} & B _ {2} \\ \hline C _ {2} & D _ {2} \end{array} \right] = \left[ \begin{array}{c c c c} A _ {1} & 0 & B _ {1} \\ 0 & A _ {2} & B _ {2} \\ \hline C _ {1} & C _ {2} & D _ {1} + D _ {2} \end{array} \right].
$$

For future reference, we shall also introduce the following definitions.

Definition 3.7 The transpose of a transfer matrix G(s) or the dual system is defined as

$$G \longmapsto G ^ {T} (s) = B ^ {*} (s I - A ^ {*}) ^ {- 1} C ^ {*} + D ^ {*}$$

or, equivalently,

$$
\left[ \begin{array}{c c} A & B \\ \hline C & D \end{array} \right] \longmapsto \left[ \begin{array}{c c} A ^ {*} & C ^ {*} \\ \hline B ^ {*} & D ^ {*} \end{array} \right].
$$

Definition 3.8 The conjugate system of $G ( s )$ is defined as

$$G \longmapsto G ^ {\sim} (s) := G ^ {T} (- s) = B ^ {*} (- s I - A ^ {*}) ^ {- 1} C ^ {*} + D ^ {*}$$

or, equivalently,
