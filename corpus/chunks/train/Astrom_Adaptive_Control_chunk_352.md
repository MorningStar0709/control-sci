The vector $\varphi_f^T (t - d_0)$ can be interpreted as the sensitivity derivative of the prediction error $\varepsilon$ with respect to the parameter. The parameter update of Eq. (5.83) is thus a discrete-time version of the MIT rule. The main difference is that the model error $e(t) = y(t) - y_m(t)$ is replaced by the prediction error $\varepsilon (t)$ .

Notice that in the identification-based schemes such as self-tuning controllers we normally attempt to obtain a form similar to

$$y (t) = \varphi_ {f} ^ {T} \theta$$

With the model-reference approach, it is also possible to admit a model of the form

$$y (t) = G (p) \left(\varphi_ {f} ^ {T} \theta\right)$$

where $G(p)$ is SPR. In summary we thus find that the MRAS-type algorithms can be obtained in a straightforward way as a direct self-tuning regulator based on a minimum-degree pole placement design with cancellation of the whole B polynomial.
