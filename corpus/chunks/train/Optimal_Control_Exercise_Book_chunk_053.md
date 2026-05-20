# Solution:

We have to show that the Legendre’s condition is valid, which means that:

$$L _ {y ^ {\prime} y ^ {\prime}} (x, y (x), y ^ {\prime} (x)) \geq 0, \quad \forall x \in [ a, b ] \tag {180}$$

Firstly, we will find the admissible extremal via the Lagrange equation. Let’s also consider the simplified notation $y ( x ) = y , y ^ { \prime } ( x ) = y ^ { \prime }$ and $L = L ( x , y ( x ) , y ^ { \prime } ( x ) )$ ) for convenience.

$$L = \sqrt {1 + y ^ {2} y ^ {\prime 2}} \tag {181}\therefore L _ {y} = \frac {y y ^ {\prime 2}}{\sqrt {1 + y ^ {2} y ^ {\prime 2}}} \tag {182}L _ {y} ^ {\prime} = \frac {y ^ {2} y ^ {\prime}}{\sqrt {1 + y ^ {2} y ^ {\prime 2}}} \tag {183}$$

The Euler-Lagrange equation becomes:

$$\frac {y y ^ {\prime 2}}{\sqrt {1 + y ^ {2} y ^ {\prime 2}}} = \frac {d}{d x} \frac {y ^ {2} y ^ {\prime}}{\sqrt {1 + y ^ {2} y ^ {\prime 2}}} \tag {185}$$

A general solution for the equation is the following

$$y (x) = c _ {2} \sqrt {c _ {1} + 2 x} \tag {186}$$

Given the boundary conditions, we can get:

$$
\left\{ \begin{array}{l} y (0) = 1 \\ y (1) = 3 \end{array} \Longrightarrow \left\{ \begin{array}{l} c _ {2} \sqrt {c _ {1}} = 1 \\ c _ {2} \sqrt {c _ {1} + 4} = 3 \end{array} \Longrightarrow \left\{ \begin{array}{l} c _ {1} = \frac {1}{2} \\ c _ {2} = \sqrt {2} \end{array} \right. \right. \right. \tag {187}
$$

Therefore the admissible extremal is $y ^ { * } ( x ) = \sqrt { 2 } \sqrt { \textstyle { \frac { 1 } { 2 } } + 2 x }$ Now, let’s verify the Legendre’s condition:

$$L _ {y ^ {\prime} y ^ {\prime}} = \frac {y ^ {2} (1 + {y ^ {\prime}} ^ {2} y ^ {2} - {y ^ {\prime}} ^ {2})}{(\sqrt {1 + {y ^ {2}} {y ^ {\prime}} ^ {2}}) ^ {3}} \geq 0, \quad \forall x \in [ a, b ] \tag {188}$$

which is equivalent to verifying that $1 + y ^ { \prime 2 } y ^ { 2 } - y ^ { \prime 2 } \ge 0$ . This yields:

$$y ^ {\prime 2} y ^ {2} - y ^ {\prime 2} \geq - 1 \tag {189}y ^ {\prime 2} \left(y ^ {2} - 1\right) \geq - 1 \tag {190}$$

which always holds given the even more restrictive condition $y ^ { 2 } - 1 \geq 0$ . Let’s subsitute:

$$\left(\sqrt {2} \sqrt {\frac {1}{2} + 2 x}\right) - 1 \geq 0 \tag {191}\not 1 + 4 x \not \rightarrow 1 \geq 0 \tag {192}4 x \geq 0 \quad \forall x \in [ a, b ] \tag {193}$$

Hence, $L _ { y ^ { \prime } y ^ { \prime } } ( x , y ( x ) , y ^ { \prime } ( x ) ) \ge 0$ , $\forall x \in [ a , b ]$ and thus we have shown the Legendre’s condition for optimality holds. 
