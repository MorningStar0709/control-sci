# 18.1 Model Validation

A key to the success of the robust control theory developed in this book is to have appropriate descriptions of the uncertain system (whether it is an additive uncertainty model or a general linear fractional model). Then an important question is how one can decide if a model description is appropriate $( { \mathrm { i . e . } }$ , how to validate a model).

For simplicity of presentation, we have chosen to present the discrete time model validation in this section with the understanding that a continuous time problem can be approximated by fast sampling. Suppose we have modeled a set of uncertain dynamical systems by

$$\pmb {\Delta} := \{\Delta : \Delta \in \mathcal {H} _ {\infty}, \| \Delta \| _ {\infty} \leq 1 \}$$

where the $\mathcal { H } _ { \infty }$ norm of a discrete time system $\Delta \in \mathcal { H } _ { \infty }$ is defined as $\| \Delta ( z ) \| _ { \infty } =$ $\begin{array} { r } { \operatorname* { s u p } _ { | z | > 1 } \overline { { \sigma } } \left( \Delta ( z ) \right) } \end{array}$ ). In order to verify whether this model assumption is correct, some experimental data are collected. For example, let the input to the system be the sequence $u = ( u _ { 0 } , u _ { 1 } , \dotsc , u _ { l - 1 } )$ and the output $y = ( y _ { 0 } , y _ { 1 } , \dotsc , y _ { l - 1 } )$ . A natural question is whether these data are consistent with our modeling assumption. In other words, does there exist a model $\Delta \in \Delta$ such that the output of the $\Delta$ for the period of $t \ =$ $0 , 1 , \ldots , l - 1$ is exactly $y = ( y _ { 0 } , y _ { 1 } , \dotsc , y _ { l - 1 } )$ with the input $u = ( u _ { 0 } , u _ { 1 } , \dotsc , u _ { l - 1 } ) ?$ If there does not exist a such $\Delta$ , then the model is invalidated. If there exists a such $\Delta$ , however, it does not mean that the model is validated but it only means that the model is not validated by this set of data and it may be invalidated by another set of data in the future. Hence it is actually more accurate to say our validation procedure is model invalidation.

Let ∆ be a stable, causal, linear, time-invariant system with transfer matrix

$$\Delta (z) = h _ {0} + h _ {1} z ^ {- 1} + h _ {2} z ^ {- 2} + \dots$$

where $h _ { i } , i = 0 , 1 , \ldots$ are the matrix Markov parameters. Suppose we have applied the input sequence $u = ( u _ { 0 } , u _ { 1 } , \dotsc , u _ { l - 1 } )$ to the system and collected the output for the period $t = 0 , 1 , \ldots , \ell - 1 , y = \left( y _ { 0 } , y _ { 1 } , \ldots , y _ { l - 1 } \right)$ . Then the input and output sequences are related by a Toeplitz matrix:
