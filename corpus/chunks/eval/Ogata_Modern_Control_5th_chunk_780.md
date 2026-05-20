Noting that terms $\mathbf { A } _ { b a } x _ { a }$ and $\mathbf { B } _ { b } \boldsymbol { u }$ are known quantities, Equation (10–84) describes the dynamics of the unmeasured portion of the state.

In what follows we shall present a method for designing a minimum-order observer. The design procedure can be simplified if we utilize the design technique developed for the full-order state observer.

Let us compare the state equation for the full-order observer with that for the minimum-order observer. The state equation for the full-order observer is

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} u$$

and the “state equation” for the minimum-order observer is

$$\dot {\mathbf {x}} _ {b} = \mathbf {A} _ {b b} \mathbf {x} _ {b} + \mathbf {A} _ {b a} x _ {a} + \mathbf {B} _ {b} u$$

The output equation for the full-order observer is

$$y = \mathbf {C x}$$

and the “output equation” for the minimum-order observer is

$$\dot {x} _ {a} - A _ {a a} x _ {a} - B _ {a} u = \mathbf {A} _ {a b} \mathbf {x} _ {b}$$

The design of the minimum-order observer can be carried out as follows: First, note that the observer equation for the full-order observer was given by Equation (10–57), which we repeat here:

$$\tilde {\mathbf {x}} = \left(\mathbf {A} - \mathbf {K} _ {e} \mathbf {C}\right) \tilde {\mathbf {x}} + \mathbf {B} u + \mathbf {K} _ {e} y \tag {10-85}$$

Then, making the substitutions of Table 10–1 into Equation (10–85), we obtain

$$\tilde {\mathbf {x}} _ {b} = \left(\mathbf {A} _ {b b} - \mathbf {K} _ {e} \mathbf {A} _ {a b}\right) \tilde {\mathbf {x}} _ {b} + \mathbf {A} _ {b a} x _ {a} + \mathbf {B} _ {b} u + \mathbf {K} _ {e} \left(\dot {x} _ {a} - A _ {a a} x _ {a} - B _ {a} u\right) \tag {10-86}$$

where the state observer gain matrix $\mathbf { K } _ { e }$ is an $( n - 1 ) \times 1$ matrix. In Equation (10–86), notice that in order to estimate $\widetilde { \textbf { x } } _ { b } ,$ we need the derivative of $x _ { a }$ . This presents a difficulty, because differentiation amplifies noise. If $x _ { a } \left( = y \right)$ is noisy, the use of ${ \dot { x } } _ { a }$ is unacceptable.

Table 10–1 List of Necessary Substitutions for Writing the Observer Equation for the Minimum-Order State Observer
