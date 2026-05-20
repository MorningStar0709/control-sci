$$\dot {x} _ {1} = a _ {1 1} x _ {1} + a _ {1 2} x _ {2} + a _ {1 3} x _ {3} + b _ {1 1} u _ {1} + b _ {1 2} u _ {2}\dot {x} _ {2} = a _ {2 1} x _ {1} + a _ {2 2} x _ {2} + a _ {2 3} x _ {3} + b _ {2 1} u _ {1} + b _ {2 2} u _ {2}\dot {x} _ {3} = a _ {3 1} x _ {1} + a _ {3 2} x _ {2} + a _ {3 3} x _ {3} + b _ {3 1} u _ {1} + b _ {3 2} u _ {2}$$

Note that the first time derivatives of the states are linear combinations of all three states $( x _ { 1 } , x _ { 2 } , x _ { 3 } )$ ) and both inputs $( u _ { 1 } , u _ { 2 } )$ . In this case where $n = 3$ and r = 2, we will have a total of $n ^ { 2 } = 9 a _ { i j }$ coefficients and $n \times r = 6$ $b _ { i j }$ coefficients. If the system has two sensors that produce two measurements $( m = 2 )$ ) that are linear functions of the state and input variables, our output equations will have the general form:

$$y _ {1} = c _ {1 1} x _ {1} + c _ {1 2} x _ {2} + c _ {1 3} x _ {3} + d _ {1 1} u _ {1} + d _ {1 2} u _ {2}y _ {2} = c _ {2 1} x _ {1} + c _ {2 2} x _ {2} + c _ {2 3} x _ {3} + d _ {2 1} u _ {1} + d _ {2 2} u _ {2}$$

In this case where $n = 3 , r = 2$ , and $m = 2$ , we will have a total of m $\times n = 6 ~ c _ { i j }$ coefficients and $m \times r = 4$ $d _ { i j }$ coefficients. For a time-invariant system, all coefficients $a , b , c ,$ , and d are constants.

For a general, nth-order LTI system with r inputs and m outputs, the state equations will have the form

$$\dot {x} _ {1} = a _ {1 1} x _ {1} + a _ {1 2} x _ {2} + \dots + a _ {1 n} x _ {n} + b _ {1 1} u _ {1} + b _ {1 2} u _ {2} + \dots b _ {1 r} u _ {r}\dot {x} _ {2} = a _ {2 1} x _ {1} + a _ {2 2} x _ {2} + \dots + a _ {2 n} x _ {n} + b _ {2 1} u _ {1} + b _ {2 2} u _ {2} + \dots b _ {2 r} u _ {r}\dot {x} _ {n} = a _ {n 1} x _ {1} + a _ {n 2} x _ {2} + \dots + a _ {n n} x _ {n} + b _ {n 1} u _ {1} + b _ {n 2} u _ {2} + \dots b _ {n r} u _ {r}$$

and the output equations will have the form

$$y _ {1} = c _ {1 1} x _ {1} + c _ {1 2} x _ {2} + \dots + c _ {1 n} x _ {n} + d _ {1 1} u _ {1} + d _ {1 2} u _ {2} + \dots d _ {1 r} u _ {r}y _ {2} = c _ {2 1} x _ {1} + c _ {2 2} x _ {2} + \dots + c _ {2 n} x _ {n} + d _ {2 1} u _ {1} + d _ {2 2} u _ {2} + \dots d _ {2 r} u _ {r}y _ {m} = c _ {m 1} x _ {1} + c _ {m 2} x _ {2} + \dots + c _ {m n} x _ {n} + d _ {m 1} u _ {1} + d _ {m 2} u _ {2} + \dots d _ {m r} u _ {r}$$

Because the state-variable and output equations are linear combinations of the state and input variables, we can assemble both equations in a compact matrix-vector format. To begin, we assemble the r input variables into an input vector u and the m output variables into an output vector y, in the same manner as the definition of the state vector x:
