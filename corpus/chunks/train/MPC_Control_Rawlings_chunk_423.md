# Example 3.22: Robust control of an exothermic reaction

Consider the control of a continuous-stirred-tank reactor. We use a model derived in Hicks and Ray (1971) and modified by Kameswaran and Biegler (2006). The reactor is described by the second-order differential equation

$$
\begin{array}{l} \dot {x} _ {1} = (1 / \theta) \left(1 - x _ {1}\right) - k x _ {1} \exp (- M / x _ {2}) \\ \dot {x} _ {2} = (1 / \theta) \left(x _ {f} - x _ {2}\right) + k x _ {1} \exp (- M / x _ {2}) - \alpha u \left(x _ {2} - x _ {c}\right) + w \\ \end{array}
$$

in which $x _ { 1 }$ is the product concentration, $x _ { 2 }$ is the temperature, and u is the coolant flowrate. The model parameters are $\theta = 2 0 , k = 3 0 0$ , $M = 5 , x _ { f } = 0 . 3 9 4 7 , x _ { c } = 0 . 3 8 1 6 ,$ , and $\alpha = 0 . 1 1 7 \ :$ . The state, control and disturbance constraint sets are

$$
\begin{array}{l} \mathbb {X} = \{x \in \mathbb {R} ^ {2} \mid x _ {1} \in [ 0, 2 ], x _ {2} \in [ 0, 2 ] \} \\ \mathbb {U} = \{\boldsymbol {u} \in \mathbb {R} \mid \boldsymbol {u} \in [ 0, 2 ] \} \\ \mathbb {W} = \{\boldsymbol {w} \in \mathbb {R} \mid \boldsymbol {w} \in [ - 0. 0 0 1, 0. 0 0 1 ] \} \\ \end{array}
$$

The controller is required to steer the system from a locally stable steady state $x ( 0 ) \ = \ ( 0 . 9 8 3 1 , 0 . 3 9 1 8 )$ at time 0, to a locally unstable steady state $z _ { e } = ( 0 . 2 6 3 2 , 0 . 6 5 1 9 )$ . Because the desired terminal state is $z _ { e }$ rather than the origin, the stage cost $\ell ( z , \upsilon )$ is replaced by $\ell ( z - z _ { e } , \nu - \nu _ { e } )$ where $\ell ( z , \nu ) : = ( 1 / 2 ) ( | z | ^ { 2 } + \nu ^ { 2 } )$ and $( z _ { e } , \nu _ { e } )$ is an equilibrium pair satisfying $z _ { e } = f ( z _ { e } , \nu _ { e } )$ ; the terminal constraint set $\mathbb { Z } _ { f }$ is chosen to be $\{ z _ { e } \}$ . The constraint sets for the nominal control problem are $\mathbb { Z } = \mathbb { X }$ and $\mathbb { V } = [ 0 . 0 2 , 2 ]$ . Since the state constraints are not activated, there is no need to tighten $\mathbb { X } .$ . The disturbance is chosen to be $w ( t ) = A \sin ( \omega t )$ where A and ω are independent uniformly distributed random variables, taking values in the sets [0, 0.001] and [0, 1], respectively. The horizon length is $N = 4 0$ and the sample time is $\Delta \ : = \ : 3$ giving a horizon time of 120. The ancillary controller uses $\ell _ { a } ( x , u ) = ( 1 / 2 ) ( | x | ^ { 2 } + u ^ { 2 } )$ and the same horizon and sample time.

![](image/cdc2796e1f107c8dca0458679e3dd3e436217df0f2a844aa691be4dadd173846.jpg)

<details>
<summary>line</summary>
