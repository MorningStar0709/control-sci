The entire computations are shown in Table 6.2 for $k = 2$ and in Table 6.3 for $k = 1,0$ .

The data from Tables 6.2 and 6.3 corresponding to optimal conditions is represented in the dynamic programming context in Figure 6.7. Here in this figure, $u_{0}^{*}=u^{*}(x(0),0)$ and $u_{1}^{*}=u^{*}(x(1),1)$ and the quantities within parenthesis are the optimal cost values at that stage and state. For example, at stage k=1 and state $x(k)=1.0$ , the value $J_{12}^{*}=0.75$ indicates that the cost of transfer the state from $x(1)$ to $x(2)$ is 0.75. Thus, in Figure 6.7, for finding the optimal trajectories for any initial state, we simply follow the arrows. For example, to transfer the state $x(0)=1$ to state $x(2)=0$ , we need to apply first $u_{0}^{*}=-1$ to transfer it to $x(1)=0$ and then $u_{1}^{*}=0$ .

Note: In the previous example, it so happened that for the given control and state quantization and constraint values (6.3.7) and (6.3.8), respectively, the calculated values using $x(k+1)=x(k)+u(k)$ either exactly coincide with the quantized values or outside the range. In some cases, it may happen that for the given control and state quantization and constraint values, the corresponding values of states may not exactly coincide with the quantized values, in which case, we need to perform some kind of interpolation on the values. For example, let us say, the state constraint and quantization is

$$- 1 \leq x (k) \leq + 2, k = 0, 1 \quad \text { or }x (k) = - 1. 0, \quad 0, \quad 0. 5, \quad 1. 0 \quad 2. 0. \tag {6.3.13}$$

Table 6.2 Computation of Cost during the Last Stage k = 2
