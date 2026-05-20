$$
\begin{array}{l} V _ {R x} = \alpha_ {0 0} + \alpha_ {1 0} \Delta x + \alpha_ {2 0} \Delta y + \alpha_ {3 0} \Delta z + \alpha_ {4 0} \Delta t \\ + \alpha_ {1 1} \Delta x ^ {2} + \alpha_ {1 2} \Delta x \Delta y + \dots + \alpha_ {4 4} \Delta t ^ {2}, \tag {6.210} \\ \end{array}
$$

where $\alpha _ { 0 0 } = V _ { R x o }$ , that is, α00 is the nominal value of the x-component of the burnout velocity vector, and $\Delta x = ( x - x _ { o } ) , \Delta y = ( y - y _ { o } )$ , etc., are the delta quantities that give the equations their name. Similar expressions are obtained for $V _ { R y }$ and $V _ { R z }$ . The coefficients $\alpha _ { i j }$ are guidance constants that must be determined. More specifically, the $\alpha _ { i j }$ are partial derivatives given as

$$\alpha_ {1 0} = (\partial \dot {x} / \partial x) | _ {\text { burnout }}, \tag {6.211a}\alpha_ {1 2} = (\partial^ {2} \dot {x} / \partial x \partial y) | _ {\text { burnout }}. \tag {6.211b}$$

(Note that in terms of $x , y , z .$ , the coefficients of $\alpha _ { i j }$ correspond to $\alpha _ { 1 0 } = \alpha _ { x x } , \alpha _ { 2 0 } =$ $\alpha _ { x y } , \alpha _ { 3 0 } = \alpha _ { x z } , \alpha _ { 4 0 } = \alpha _ { x t } , \alpha _ { 1 1 } = \alpha _ { x x x } , \alpha _ { 1 2 } = \alpha _ { x x y }$ , etc.) The partial derivatives are defined in terms of a two-dimensional (or more variables) Taylor series as follows:

$$
\begin{array}{l} f (x, y) = f (a, b) + \frac {\partial f (a , b)}{\partial x} (x - a) + \frac {\partial f (a , b)}{\partial y} (x - b) \\ + \frac {1}{2 !} \left[ \frac {\partial^ {2} f (a , b)}{\partial^ {2} x} (x - a) ^ {2} + 2 \frac {\partial^ {2} f (a , b)}{\partial x \partial y} (x - a) (y - b) \right. \\ \left. \left. + \frac {\partial^ {2} f (a , b)}{\partial^ {2} y} (y - b) ^ {2} \right] + \dots , \right. \\ \end{array}
$$
