# 7.9.1 Butcher tableaus

Butcher tableaus are a more succinct representation for explicit and implicit Runge-Kutta numerical integration methods. Here’s the general structure for explicit methods.

<table><tr><td>0</td><td></td><td></td><td></td><td></td></tr><tr><td>$ c_{2} $</td><td>$ a_{2,1} $</td><td></td><td></td><td></td></tr><tr><td>$ \vdots $</td><td>$ \vdots $</td><td>$ \ddots $</td><td></td><td></td></tr><tr><td>$ c_{s} $</td><td>$ a_{s,1} $</td><td>$ \cdots $</td><td>$ a_{s,s-1} $</td><td></td></tr><tr><td>$ \hline $</td><td>$ b_{1} $</td><td>$ \cdots $</td><td>$ \cdots $</td><td>$ b_{s} $</td></tr></table>

where s is the number of stages in the method, the matrix $[ a _ { i j } ]$ is the Runge-Kutta matrix, $b _ { 1 } , \dots , b _ { s }$ are the weights, and $c _ { 1 } , \ldots , c _ { s }$ are the nodes. The top-left quadrant contains the sums of the rows in the top-right quadrant. Each column in the right half corresponds to a k coefficient from $\mathbf { k } _ { 1 }$ to ${ \bf k } _ { s }$ .

The family of solutions to $\dot { \mathbf { x } } = f ( t , \mathbf { x } )$ is given by

$$
\begin{array}{l} \mathbf {k} _ {1} = f (t _ {k}, \mathbf {x} _ {k}) \\ \mathbf {k} _ {2} = f (t _ {k} + c _ {2} h, \mathbf {x} _ {k} + h (a _ {2, 1} \mathbf {k} _ {1})) \\ \begin{array}{c} \bullet \\ \vdots \\ \bullet \end{array} \\ \mathbf {k} _ {s} = f \left(t _ {k} + c _ {s} h, \mathbf {x} _ {k} + h \left(a _ {s, 1} \mathbf {k} _ {1} + \dots + a _ {s, s - 1} \mathbf {k} _ {s - 1}\right)\right) \\ \end{array}
\mathbf {x} _ {k + 1} = \mathbf {x} _ {k} + h \sum_ {i = 1} ^ {s} b _ {i} \mathbf {k} _ {i}
$$

where h is the timestep duration.
