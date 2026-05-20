# Algorithm Development

There are several important issues that relate to algorithm development. Current toolboxes for adaptive control use only a few of the algorithms that have been developed. It seems safe to guess that the toolboxes will be expanded, and it would also seem useful to include auto-tuners in the toolboxes to simplify initialization. Significant improvements can thus be achieved with tools that are already known, but there is also a need for improved techniques. Better methods for control system design are needed. Techniques that can explicitly handle actuator constraints and model uncertainties would be valuable contributions. It would be very useful to have methods for estimating the unstructured uncertainties.

Diagnostic routines that will tell whether a control algorithm is behaving as expected are needed. Such algorithms are well known for minimum-variance control, in which monitoring can be done simply by calculating covariances. It is straightforward to develop similar techniques for other design methods.

There is both theoretical and experimental evidence that probing signals are useful. It is also clear that it is not practical to introduce probing via stochastic control theory because of the excessive computational requirements. A significant challenge is therefore to find other ways to introduce probing. There are many who intuitively object to introducing probing signals intentionally. It must be remembered that a poorly tuned regulator will give larger than necessary deviations in controlled variables.

A systematic approach to design and implementation of safety networks is an issue of great practical relevance. Expert systems may be useful in this context.
