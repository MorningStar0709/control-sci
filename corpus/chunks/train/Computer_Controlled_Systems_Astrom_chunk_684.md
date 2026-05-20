Proof. A transmission zero is a complex number z such that an input signal of the form $z^{k}y_{0}$ gives zero output. For the system (11.56), $\hat{x}(k+1)=\hat{x}(k)=0$ implies that there exist $y_{0}$ and $\hat{z}(k)=\hat{z}_{0}z^{k}$ where $-\infty<k<\infty$ and $y_{0}\neq0$ such that

$$\boldsymbol {K} _ {1} \boldsymbol {C} _ {2} \hat {\boldsymbol {z}} _ {0} - \boldsymbol {K} _ {1} \boldsymbol {y} _ {0} = 0(z I - \Phi_ {2} + K _ {2} C _ {2}) \hat {z} _ {0} - K _ {2} y _ {0} = 0$$

or

$$
\begin{array}{l} \left( \begin{array}{c c} z I - \Phi_ {2} + K _ {2} C _ {2} & - K _ {2} \\ K _ {1} C _ {2} & - K _ {1} \end{array} \right) \binom{\hat {z} _ {0}}{y _ {0}} \\ = \left( \begin{array}{c c} z I - \Phi_ {2} & - K _ {2} \\ 0 & - K _ {1} \end{array} \right) \left( \begin{array}{c c} I & 0 \\ - C _ {2} & I \end{array} \right) \binom{\hat {z} _ {0}}{y _ {0}} = 0 \\ \end{array}
$$

There exists a nonzero solution to this equation only for those z that are eigenvalues of the matrix $\Phi_{2}$ .

Remark. The Kalman filter will have zeros at the poles of the noise model. To obtain a Kalman filter that blocks certain frequencies (a notch filter) is just a matter of choosing a noise model with poles at those frequencies. The attenuation of certain frequencies by the Kalman filter is enhanced if the energy of the noise is increased at those frequencies in the noise model.
