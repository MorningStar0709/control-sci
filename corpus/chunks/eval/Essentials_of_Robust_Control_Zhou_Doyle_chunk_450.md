# Gap Metric and ν-Gap Metric

In the previous chapters, we have seen that all of robust control design techniques assume that we have some description of the model uncertainties (i.e., we have a measure of the distance from the nominal plant to the set of uncertainty systems). This measure is usually chosen to be a metric or a norm. However, the operator norm can be a poor measure of the distance between systems in respect to feedback control system design. For example, consider

$$P _ {1} (s) = \frac {1}{s}, P _ {2} (s) = \frac {1}{s + 0 . 1}.$$

The closed-loop complementary sensitivity functions corresponding to $P _ { 1 }$ and $P _ { 2 }$ with unity feedback are relatively close and their difference is

$$\left\| P _ {1} (I + P _ {1}) ^ {- 1} - P _ {2} (I + P _ {2}) ^ {- 1} \right\| _ {\infty} = 0. 0 9 0 9,$$

but the difference between $P _ { 1 }$ and $P _ { 2 }$ is

$$\left\| P _ {1} - P _ {2} \right\| _ {\infty} = \infty .$$

This shows that the closed-loop behavior of two systems can be very close even though the norm of the difference between the two open-loop systems can be arbitrarily large.

To deal with such problems, the gap metric and the ν-gap metric were introduced into the control literature by Zames and El-Sakkary [1980] (see also El-Sakkary [1985] and Vinnicombe [1993]) as being appropriate for the study of uncertainty in feedback systems. An alternative metric, the graph metric, was also introduced by Vidyasagar [1984] in terms of normalized coprime factorizations. All of these metrics are equivalent, and thus induce the same topology. This topology is the weakest in which feedback stability is a robust property. The metrics define notions of distance in the space of (possible) unstable systems that do not assume that the plants have the same number of poles in the right-half plane.

We shall briefly introduce the gap metric in Section 17.1 and study some of its applications in robust control. Our focus in this chapter is Sections 17.2–17.4, which study in some detail the ν-gap metric. In particular, we introduce the ν-gap metric in Section 17.2 and explore its frequency domain interpretation and applications in Section 17.3 and Section 17.4. Finally, we consider controller order reduction in the gap or ν-gap metric framework in Section 17.5.
