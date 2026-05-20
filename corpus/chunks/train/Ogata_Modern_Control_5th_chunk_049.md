On the other hand, the closed-loop transfer function $C _ { R } { \big ( } s { \big ) } / R { \big ( } s { \big ) }$ approaches $1 / H ( s )$ as the gain of $G _ { 1 } ( s ) G _ { 2 } ( s ) H ( s )$ increases. This means that if $| G _ { 1 } ( s ) G _ { 2 } ( s ) H ( s ) | \gg 1$ , then the closed-loop transfer function $C _ { R } { \big ( } s { \big ) } / R { \big ( } s { \big ) }$ becomes independent of $G _ { 1 } ( s )$ and $G _ { 2 } ( s )$ and inversely proportional to $H ( s )$ , so that the variations of $G _ { 1 } ( s )$ and $G _ { 2 } ( s )$ do not affect the closed-loop transfer function $C _ { R } { \big ( } s { \big ) } / R { \big ( } s { \big ) }$ . This is another advantage of the closed-loop system. It can easily be seen that any closed-loop system with unity feedback, $H ( s ) = 1$ , tends to equalize the input and output.

Procedures for Drawing a Block Diagram. To draw a block diagram for a system, first write the equations that describe the dynamic behavior of each component. Then take the Laplace transforms of these equations, assuming zero initial conditions, and represent each Laplace-transformed equation individually in block form. Finally, assemble the elements into a complete block diagram.

As an example, consider the RC circuit shown in Figure 2–12(a). The equations for this circuit are

$$i = \frac {e _ {i} - e _ {o}}{R} \tag {2-4}e _ {o} = \frac {\int i d t}{C} \tag {2-5}$$

The Laplace transforms of Equations (2–4) and (2–5), with zero initial condition, become

$$I (s) = \frac {E _ {i} (s) - E _ {o} (s)}{R} \tag {2-6}E _ {o} (s) = \frac {I (s)}{C s} \tag {2-7}$$

Equation (2–6) represents a summing operation, and the corresponding diagram is shown in Figure 2–12(b). Equation (2–7) represents the block as shown in Figure 2–12(c). Assembling these two elements, we obtain the overall block diagram for the system as shown in Figure 2–12(d).

Block Diagram Reduction. It is important to note that blocks can be connected in series only if the output of one block is not affected by the next following block. If there are any loading effects between the components, it is necessary to combine these components into a single block.

Any number of cascaded blocks representing nonloading components can be replaced by a single block, the transfer function of which is simply the product of the individual transfer functions.

Figure 2–12

(a) RC circuit;

(b) block diagram representing Equation (2–6);

(c) block diagram representing Equation (2–7);

(d) block diagram of the RC circuit.
