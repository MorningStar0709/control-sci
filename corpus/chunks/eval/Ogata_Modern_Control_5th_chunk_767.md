$$\phi (s) = \bigl (s - \mu_ {1} \bigr) \bigl (s - \mu_ {2} \bigr) \dots \bigl (s - \mu_ {n} \bigr)$$

where $\mu _ { 1 } , \mu _ { 2 } , \ldots , \mu _ { n }$ are the desired eigenvalues. Equation (10–65) is called Ackermann’s formula for the determination of the observer gain matrix $\mathbf { K } _ { e }$ .

Comments on Selecting the Best ${ \bf K } _ { e }$ . Referring to Figure 10–11, notice that the feedback signal through the observer gain matrix $\mathbf { K } _ { e }$ serves as a correction signal to the plant model to account for the unknowns in the plant. If significant unknowns are involved, the feedback signal through the matrix $\mathbf { K } _ { e }$ should be relatively large. However, if the output signal is contaminated significantly by disturbances and measurement noises, then the output $y$ is not reliable and the feedback signal through the matrix $\mathbf { K } _ { e }$ should be relatively small. In determining the matrix $\mathbf { K } _ { e }$ , we should carefully examine the effects of disturbances and noises involved in the output $y .$ .

Remember that the observer gain matrix $\mathbf { K } _ { e }$ depends on the desired characteristic equation

$$(s - \mu_ {1}) (s - \mu_ {2}) \dots (s - \mu_ {n}) = 0$$

The choice of a set of $\mu _ { 1 } , \mu _ { 2 } , \ldots , \mu _ { n }$ is, in many instances, not unique. As a general rule, however, the observer poles must be two to five times faster than the controller poles to make sure the observation error (estimation error) converges to zero quickly. This means that the observer estimation error decays two to five times faster than does the state vector x. Such faster decay of the observer error compared with the desired dynamics makes the controller poles dominate the system response.

It is important to note that if sensor noise is considerable, we may choose the observer poles to be slower than two times the controller poles, so that the bandwidth of the system will become lower and smooth the noise. In this case the system response will be strongly influenced by the observer poles. If the observer poles are located to the right of the controller poles in the left-half s plane, the system response will be dominated by the observer poles rather than by the control poles.
