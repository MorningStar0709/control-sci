# Robust control algorithm.

Initialization: At time 0, set $i = 0 , x = x ( 0 )$ , and $z = x$ . Solve $\bar { \mathbb { P } } _ { N }$ for N time steps to obtain the nominal closed-loop state and control sequences $\mathbf { v } ^ { * } \ = \ \mathbf { v } ^ { * } ( z ) \ = \ \{ \nu ^ { * } ( 0 ; z ) , \nu ^ { * } ( 1 ; z ) , \ldots , \nu ^ { * } ( N - 1 ; z ) \}$ and $\mathbf { z } ^ { * } = \mathbf { z } ^ { * } ( z ) = \{ z ^ { * } ( 0 ; z ) , z ^ { * } ( 1 ; z ) , \ldots , z ^ { * } ( N ; z ) \}$ , and set $u =$ $\bar { \kappa } _ { N } ( z ) = \nu ^ { * } ( 0 ; z ) . ^ 7$

Step 1 (Compute control): At time i, compute $u = \kappa _ { N } ( x , z )$ by solving $\mathbb { P } _ { N } ( x , z )$ .

Step 2 (Control): Apply u to the system being controlled.

Step 3 (Update x): Set $x = x ^ { + }$ where $x ^ { + } = f ( x , u ) + w$ is the successor state.

Step 4 (Update $z , \mathbf { v } ^ { * }$ , and $\mathbf { z } ^ { \ast } )$ : Compute $\nu ^ { * } ~ = ~ \bar { \kappa } _ { N } ( z ^ { * } ( N ) )$ and $z ^ { * } =$ $f ( z ^ { * } ( N ) , \nu ^ { * } )$ by solving $\mathbb { P } _ { N } ( z ^ { * } ( N ) )$ . Set $z = z ^ { * } ( 1 )$ . Set $\begin{array} { r l } { \mathbf { v } ^ { * } } & { { } = } \end{array}$ $\{ \nu ^ { * } ( 1 ) , \ldots , \nu ^ { * } ( N - 1 ) , \nu ^ { * } \}$ and set $\mathbf { z } ^ { * } = \{ z ^ { * } ( 1 ) , \ldots , z ^ { * } ( N ) , z ^ { * } \}$ .

Step 5 (Repeat): Set $i = i + 1$ . Go to Step 1.

A check step may be incorporated as done previously to safeguard against unanticipated events.
