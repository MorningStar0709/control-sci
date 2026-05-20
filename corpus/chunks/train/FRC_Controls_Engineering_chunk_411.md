# 14.4 Drivetrain linear/angular velocity state-space model

Let the linear and angular voltage contributions be

$$u _ {l i n} = K _ {v, l i n} v + K _ {a, l i n} au _ {a n g} = K _ {v, a n g} \omega + K _ {a, a n g} \alpha$$

Solve for acceleration.

$$a = - \frac {K _ {v , l i n}}{K _ {a , l i n}} v + \frac {1}{K _ {a , l i n}} u _ {l i n}\alpha = - \frac {K _ {v , a n g}}{K _ {a , a n g}} \omega + \frac {1}{K _ {a , a n g}} u _ {l i n}$$

Factor them into a matrix equation.

$$
\dot {\mathbf {x}} = \left[ \begin{array}{c c} - \frac {K _ {v , l i n}}{K _ {a , l i n}} & 0 \\ 0 & - \frac {K _ {v , a n g}}{K _ {a , a n g}} \end{array} \right] \left[ \begin{array}{c} v \\ \omega \end{array} \right] + \left[ \begin{array}{c c} \frac {1}{K _ {a , l i n}} & 0 \\ 0 & \frac {1}{K _ {a , a n g}} \end{array} \right] \left[ \begin{array}{c} u _ {l i n} \\ u _ {a n g} \end{array} \right]
$$

We want to write this model in terms of left and right voltages. The linear and angular voltages have the following relations.

$$u _ {l e f t} = u _ {l i n} - u _ {a n g}u _ {r i g h t} = u _ {l i n} + u _ {a n g}$$

Factor them into a matrix equation, then solve for the linear and angular voltages.

$$
\left[ \begin{array}{c} u _ {l e f t} \\ u _ {r i g h t} \end{array} \right] = \left[ \begin{array}{c c} 1 & - 1 \\ 1 & 1 \end{array} \right] \left[ \begin{array}{c} u _ {l i n} \\ u _ {a n g} \end{array} \right]

\left[ \begin{array}{c} u _ {l i n} \\ u _ {a n g} \end{array} \right] = \left[ \begin{array}{c c} 0. 5 & 0. 5 \\ - 0. 5 & 0. 5 \end{array} \right] \left[ \begin{array}{c} u _ {l e f t} \\ u _ {r i g h t} \end{array} \right]
$$

Plug this into the model input.

$$
\dot {\mathbf {x}} = \left[ \begin{array}{c c} - \frac {K _ {v , l i n}}{K _ {a , l i n}} & 0 \\ 0 & - \frac {K _ {v , a n g}}{K _ {a , a n g}} \end{array} \right] \left[ \begin{array}{c} v \\ \omega \end{array} \right] + \left[ \begin{array}{c c} \frac {1}{K _ {a , l i n}} & 0 \\ 0 & \frac {1}{K _ {a , a n g}} \end{array} \right] \left[ \begin{array}{c c} 0. 5 & 0. 5 \\ - 0. 5 & 0. 5 \end{array} \right] \left[ \begin{array}{c} u _ {l e f t} \\ u _ {r i g h t} \end{array} \right]

\dot {\mathbf {x}} = \left[ \begin{array}{c c} - \frac {K _ {v , l i n}}{K _ {a , l i n}} & 0 \\ 0 & - \frac {K _ {v , a n g}}{K _ {a , a n g}} \end{array} \right] \left[ \begin{array}{c} v \\ \omega \end{array} \right] + \left[ \begin{array}{c c} \frac {0 . 5}{K _ {a , l i n}} & \frac {0 . 5}{K _ {a , l i n}} \\ - \frac {0 . 5}{K _ {a , a n g}} & \frac {0 . 5}{K _ {a , a n g}} \end{array} \right] \left[ \begin{array}{c} u _ {l e f t} \\ u _ {r i g h t} \end{array} \right]
$$
