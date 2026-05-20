# 14.3 Drivetrain left/right velocity state-space model

$$
\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} \mathbf {u}
\mathbf {x} = \left[ \begin{array}{c} \text {left velocity} \\ \text {right velocity} \end{array} \right] \quad \dot {\mathbf {x}} = \left[ \begin{array}{c} \text {left acceleration} \\ \text {right acceleration} \end{array} \right] \quad \mathbf {u} = \left[ \begin{array}{c} \text {left voltage} \\ \text {right voltage} \end{array} \right]
$$

We want to derive what A and B are from linear and angular feedforward models. Since the left and right dynamics are symmetric, we’ll guess the model has the form

$$
\mathbf {A} = \left[ \begin{array}{c c} A _ {1} & A _ {2} \\ A _ {2} & A _ {1} \end{array} \right] \quad \mathbf {B} = \left[ \begin{array}{c c} B _ {1} & B _ {2} \\ B _ {2} & B _ {1} \end{array} \right]
$$

Let $K _ { v , l i n }$ be the linear velocity gain, $K _ { a , l i n }$ be the linear acceleration gain, $K _ { v , a n g }$ be the angular velocity gain, and $K _ { a , a n g }$ be the angular acceleration gain. Let ${ \bf u } =$ $\left[ K _ { v , l i n } v \quad K _ { v , l i n } v \right] ^ { \mathsf { T } }$ be the input that makes both sides of the drivetrain move at a constant velocity v. Therefore, $\mathbf { x } = \left[ v \quad v \right] ^ { \mathsf { T } } { \mathrm { a n d } } { \dot { \mathbf { x } } } = \left[ 0 \quad 0 \right] ^ { \mathsf { T } }$ . Substitute these into the state-space model.

$$
\left[ \begin{array}{c} 0 \\ 0 \end{array} \right] = \left[ \begin{array}{c c} A _ {1} & A _ {2} \\ A _ {2} & A _ {1} \end{array} \right] \left[ \begin{array}{c} v \\ v \end{array} \right] + \left[ \begin{array}{c c} B _ {1} & B _ {2} \\ B _ {2} & B _ {1} \end{array} \right] \left[ \begin{array}{c} K _ {v, l i n} v \\ K _ {v, l i n} v \end{array} \right]
$$

Since the column vectors contain the same element, the elements in the second row can be rearranged.

$$
\left[ \begin{array}{c} 0 \\ 0 \end{array} \right] = \left[ \begin{array}{c c} A _ {1} & A _ {2} \\ A _ {1} & A _ {2} \end{array} \right] \left[ \begin{array}{c} v \\ v \end{array} \right] + \left[ \begin{array}{c c} B _ {1} & B _ {2} \\ B _ {1} & B _ {2} \end{array} \right] \left[ \begin{array}{c} K _ {v, l i n} v \\ K _ {v, l i n} v \end{array} \right]
$$

Since the rows are linearly dependent, we can use just one of them.

$$
0 = \left[ \begin{array}{c c} A _ {1} & A _ {2} \end{array} \right] v + \left[ \begin{array}{c c} B _ {1} & B _ {2} \end{array} \right] K _ {v, l i n} v
