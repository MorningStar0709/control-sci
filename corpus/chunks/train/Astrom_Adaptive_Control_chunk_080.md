# Statistical Interpretation

The least-squares method can be interpreted in statistical terms. It is then necessary to make assumptions about how the data has been generated. Assume, that the process is

$$y (i) = \varphi^ {T} (i) \theta^ {0} + e (i) \tag {2.12}$$

where $\theta^{0}$ is the vector of “true” parameters and $\{e(i), i = 1, 2, \ldots\}$ is a sequence of independent, equally distributed random variables with zero mean. It is also assumed that e is independent of $\varphi$ . Equation (2.4) can be written as

$$Y = \Phi \theta^ {0} + \mathcal {E}$$

Multiplying by $(\Phi^T\Phi)^{-1}\Phi^T$ gives

$$\left(\Phi^ {T} \Phi\right) ^ {- 1} \Phi^ {T} Y = \hat {\theta} = \hat {\theta} ^ {0} + \left(\Phi^ {T} \Phi\right) ^ {- 1} \Phi^ {T} E \tag {2.13}$$

Provided that E is independent of $\Phi^{T}$ , which is equivalent to saying that $e(i)$ is independent of $\varphi(i)$ , the mathematical expectation of $\hat{\theta}$ is equal to $\theta^{0}$ . An estimate with this property is called unbiased. The following theorem is given without proof.
