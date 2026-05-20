# Unification

The different recursive algorithms discussed are quite similar. They can all be described by the equations

$$
\begin{array}{l} \hat {\theta} (t) = \hat {\theta} (t - 1) + P (t) \varphi (t - 1) \varepsilon (t) \\ P (t) = \frac {1}{\lambda} \left(P (t - 1) - \frac {P (t - 1) \varphi (t - 1) \varphi^ {T} (t - 1) P (t - 1)}{\lambda + \varphi^ {T} (t - 1) P (t - 1) \varphi (t - 1)}\right) \\ \end{array}
$$

where $\theta$ , $\varphi$ , and $\varepsilon$ are different for the different methods.
