# DEFINITION

A system is detectable (stabilizable) if all unstable modes are observable (controllable).

Detectability is weaker than observability. An observable system is clearly detectable, since all its modes are observable; in general, the converse is not true. Similarly, stabilizability is a weaker property than controllability.

Internal stability (which implies input–output stability) is required in practice. This cannot be achieved unless the plant is both detectable and stabilizable. The presence of an unstable, unobservable mode means that instability exists but goes undetected by the available sensors. An unstable, uncontrollable mode is almost sure to be excited by some unmodeled disturbance input, while the control inputs are powerless to suppress it.

If the realization is minimal (i.e., controllable and observable), all eigenvalues of $A$ appear as transfer function poles. In that case, if all poles are stable, so are the eigenvalues. Therefore, if a realization is known to be minimal, input-output stability guarantees internal stability. A formal proof may be found in Fortmann and Hitz.

To summarize, internal stability implies input-output stability; input-output stability implies internal stability if the realization is controllable and observable, i.e., minimal.
