$$
\mathbf {y} = \left[ \begin{array}{l} y _ {1} \\ y _ {2} \end{array} \right] = \left[ \begin{array}{l l} 0 & 1 \\ 1 & 0 \end{array} \right] \mathbf {x} + \left[ \begin{array}{l l} 0 & 0 \\ 0 & 0 \end{array} \right] \mathbf {u} \tag {5.43}
$$

It should be noted that the reduced-order output matrix C is identical to the third-order output matrix in Eq. (5.39) with the second column removed.

A final note is in order. If we obtain the system response of the DC motor for a given input voltage $e _ { \mathrm { i n } } ( t )$ ) and load torque $T _ { L }$ (say, using MATLAB’s Simulink), we will obtain identical system output responses for $y _ { 1 } ( t )$ ) and $y _ { 2 } ( t )$ (angular velocity ?? and current I) whether we use the third-order SSR derived in Example 5.6 or the second-order SSR presented in this example. Both state-space models are based on the same governing system dynamics, and both use the same input and output variables. The third-order SSR in Example 5.6 carries along an additional state variable (??) that does not contribute to either the system dynamics or the output, and hence this state variable and its state equation can therefore be eliminated. However, the angular position information ??(t) of the DC motor is lost when we use the second-order SSR presented in this example.
