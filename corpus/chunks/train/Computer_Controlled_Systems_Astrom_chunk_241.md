# Direct Calculation of the State Variables

The problem was solved in Sec. 3.4 for the special case when there are no inputs. We will now extend this solution slightly and it will be shown that the state can be computed directly from past inputs and outputs. For simplicity it is assumed that there is only one output. The output $y(k) = Cx(k)$ obtained at sampling instant k gives one linear equation for determining the state variable. Using information from n different sampling instants $k, k-1, \ldots, k-n+1$ gives the following linear equations.

$$
\begin{array}{l} y (k - n + 1) = C x (k - n + 1) \\ y (k - n + 2) = C \Phi x (k - n + 1) + C \Gamma u (k - n + 1) \\ y (k) = C \Phi^ {n - 1} x (k - n + 1) + C \Phi^ {n - 2} \Gamma u (k - n + 1) + \dots + C \Gamma u (k - 1) \tag {4.24} \\ \end{array}
$$

•
•
•

By introducing the vectors $U_{k-1}$ and $Y_{k}$

$$
\mathbf {Y} _ {k} = \left( \begin{array}{c} y (k - n + 1) \\ y (k - n + 2) \\ \vdots \\ y (k) \end{array} \right) \quad U _ {k - 1} = \left( \begin{array}{c} u (k - n + 1) \\ u (k - n + 2) \\ \vdots \\ u (k - 1) \end{array} \right)
$$

whose components are past inputs and outputs, Eq. (4.24) can be written as

$$Y _ {k} = W _ {o} x (k - n + 1) + W _ {u} U _ {k - 1}$$

where the matrices $W_{o}$ and $W_{u}$ are given by

$$
W _ {o} = \left( \begin{array}{c} C \\ C \Phi \\ C \Phi^ {2} \\ \vdots \\ C \Phi^ {n - 1} \end{array} \right) \quad W _ {u} = \left( \begin{array}{c c c c} 0 & 0 & \dots & 0 \\ C \Gamma & 0 & \dots & 0 \\ C \Phi \Gamma & C \Gamma & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ C \Phi^ {n - 2} \Gamma & C \Phi^ {n - 3} \Gamma & \dots & C \Gamma \end{array} \right)
$$

The matrix $W_{o}$ is invertible if the system is observable; we can then solve for $x(k - n + 1)$ and obtain

$$x (k - n + 1) = W _ {o} ^ {- 1} Y _ {k} - W _ {o} ^ {- 1} W _ {u} U _ {k - 1}$$

The state has thus been obtained in terms of future outputs and measurements. Repeated use of Eq. (4.23) gives

$$x (k) = \Phi^ {n - 1} x (k - n + 1) + \Phi^ {n - 2} \Gamma u (k - n + 1) + \dots + \Gamma u (k - 1)$$

and we find that

$$x (k) = A _ {y} Y _ {k} - B _ {u} U _ {k - 1} \tag {4.25}$$

where

$$
A _ {y} = \Phi^ {n - 1} W _ {o} ^ {- 1} \quad B _ {u} = \left( \begin{array}{l l} \Phi^ {n - 2} \Gamma & \Phi^ {n - 3} \Gamma \dots \Gamma \end{array} \right) - \Phi^ {n - 1} W _ {o} ^ {- 1} W _ {u} \tag {4.26}
$$

The state vector $x(k)$ is thus a linear combination of $y(k), y(k-1), \ldots, y(k-n+1)$ and $u(k-1), u(k-2), \ldots, u(k-n+1)$ . We illustrate by an example.
