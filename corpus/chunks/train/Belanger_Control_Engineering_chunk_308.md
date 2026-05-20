# Solution

Since $L(0) = k$ , the position constant is $k_{p} = k$ . The steady-state error to a unit step is given by Equation 6.5:

$$e _ {s s} = \frac {1}{1 + k _ {p}} = \frac {1}{1 + k}.$$

The value of $e_{ss}$ is reduced by increasing k, but this is limited by stability: without stability, there is no steady state. Using Routh's criterion, -1 < k < 8 for stability. Therefore,

$$e _ {s s} > \frac {1}{1 + 8} = \frac {1}{9}.$$

If $L(s)$ has one or more poles at $s = 0$ , i.e., one or more integrations, then $\lim_{s \to 0} L(s) = \infty$ and

$$e _ {s s} = A \lim _ {s \rightarrow 0} \frac {1}{1 + L (s)} = 0. \tag {6.6}$$

That is, the steady-state error to a step is zero if the loop gain has integration.

The dc steady-state error to a ramp input is often of interest, because many signals have ramplike components. Then

$$e _ {\mathrm{ramp}} = \lim _ {s \to 0} s A S (s) \frac {1}{s ^ {2}}= A \lim _ {s \rightarrow 0} \frac {S (s)}{s}. \tag {6.7}$$

In terms of the loop gain,

$$e _ {\text { ramp }} = A \lim _ {s \rightarrow 0} \frac {1}{s + s L (s)}= A \lim _ {s \rightarrow 0} \frac {1}{s L (s)}. \tag {6.8}$$

If $L(0)$ exists, then $e_{\mathrm{ramp}}$ does not; i.e., it is infinite. If $L(s)$ has one pole at $s = 0$ , then $\lim_{s \to 0} sL(s)$ exists. Let that limit be $k_v$ , known as the velocity constant; then

$$e _ {\text { ramp }} = \frac {A}{k _ {v}} \tag {6.9}$$

where

$$k _ {v} = \lim _ {s \rightarrow 0} s L (s). \tag {6.10}$$

If $L(s)$ has two or more poles at $s = 0$ , then $\lim_{s \to 0} sL(s) = \infty$ , and $e_{\mathrm{ramp}} = 0$ .

In the literature, the number of integrations in $L(s)$ is referred to as the system type. For a Type 0 system,

$$e _ {s s} = \frac {A}{1 + k _ {p}}, \quad k _ {p} = L (0); \quad e _ {\text { ramp }} = \infty .$$

For a Type 1 system,

$$e _ {s s} = 0; \quad e _ {\text { ramp }} = \frac {A}{k _ {v}}, \quad k _ {v} = \lim _ {s \rightarrow 0} s L (s).$$

For a system of Type 2 or higher,

$$e _ {s s} = e _ {\text { ramp }} = 0.$$

To summarize, the dc steady-state response is determined by the limiting behavior of $L(s)$ , as $s \rightarrow 0$ . Small errors are achieved by large dc loop gains, with integration (infinite dc gain) actually reducing the step response error to zero.
