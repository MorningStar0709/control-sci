# Extensions

The problem discussed can be extended in many different directions. The controller given by Eq. (4.34) has a time delay of one sampling period. The reason for this is that the feedback is based on an observer that gives $\hat{x}(k \mid k - 1)$ . It is possible to obtain a controller without extra delays by using instead the control law

$$u (k) = - L \hat {x} (k \mid k) \tag {4.38}$$

where $\hat{x}(k \mid k)$ is obtained from the observer given by Eq. (4.32). The properties of the system obtained is analogous to the case that has just been investigated, so the details are left as exercises. See the problem section at the end of this chapter. Notice, however, that the feedback matrix L does not have to be changed when we change the observer. This is a very nice consequence of the separation of the problem into a state feedback and an observer.
