$$\Theta (s) = \frac {1}{\sqrt {2}} \frac {1 - s}{1 - s} = \frac {1}{\sqrt {2}}, \quad \Psi (P _ {1}, P _ {2}) = \frac {1}{\sqrt {2}} \frac {s - 1}{s + 1},$$

and $\begin{array} { r } { \delta _ { \nu } ( P _ { 1 } , P _ { 2 } ) = \frac { 1 } { \sqrt { 2 } } , } \end{array}$ . (Note that Θ has no poles or zeros!)

The ν-gap metric can also be computed directly from the system transfer matrices without first finding the normalized coprime factorizations.

Theorem 17.6 The ν-gap metric can be defined as

$$
\delta_ {\nu} (P _ {1}, P _ {2}) = \left\{ \begin{array}{l l} \| \Psi (P _ {1}, P _ {2}) \| _ {\infty}, & \text {if} \det (I + P _ {2} ^ {\sim} P _ {1}) \neq 0   \forall \omega \text {and} \\ & \text {wno} \det (I + P _ {2} ^ {\sim} P _ {1}) + \eta (P _ {1}) - \eta (P _ {2}) - \eta_ {0} (P _ {2}) = 0, \\ 1, & \text {otherwise} \end{array} \right.
$$

where $\Psi ( P _ { 1 } , P _ { 2 } )$ can be written as

$$\Psi (P _ {1}, P _ {2}) = (I + P _ {2} P _ {2} ^ {\sim}) ^ {- 1 / 2} (P _ {1} - P _ {2}) (I + P _ {1} ^ {\sim} P _ {1}) ^ {- 1 / 2}.$$

Proof. Since the number of unstable zeros of $M _ { 1 } ~ ( M _ { 2 } )$ is equal to the number of unstable poles of $P _ { 1 } ~ ( P _ { 2 } )$ , and

$$N _ {2} ^ {\sim} N _ {1} + M _ {2} ^ {\sim} M _ {1} = M _ {2} ^ {\sim} (I + P _ {2} ^ {\sim} P _ {1}) M _ {1},$$

we have

$$\operatorname{wno} \det (N _ {2} ^ {\sim} N _ {1} + M _ {2} ^ {\sim} M _ {1}) = \operatorname{wno} \det \left\{M _ {2} ^ {\sim} (I + P _ {2} ^ {\sim} P _ {1}) M _ {1} \right\}= \operatorname{wnodet} M _ {2} ^ {\sim} + \operatorname{wnodet} (I + P _ {2} ^ {\sim} P _ {1}) + \operatorname{wnodet} M _ {1}.$$

Note that wno det $M _ { 1 } = \eta ( P _ { 1 } )$ , wno det M∼2 = −wno det $M _ { 2 } - \eta _ { 0 } ( M _ { 2 } ^ { - 1 } ) = - \eta ( P _ { 2 } ) -$ $\eta _ { 0 } ( P _ { 2 } )$ , and

$$\operatorname{wnodet} \left(N _ {2} ^ {\sim} N _ {1} + M _ {2} ^ {\sim} M _ {1}\right) = - \eta \left(P _ {2}\right) - \eta_ {0} \left(P _ {2}\right) + \operatorname{wnodet} \left(I + P _ {2} ^ {\sim} P _ {1}\right) + \eta \left(P _ {1}\right).$$

Furthermore,

$$\det (N _ {2} ^ {\sim} N _ {1} + M _ {2} ^ {\sim} M _ {1}) \neq 0, \forall \omega \iff \det (I + P _ {2} ^ {\sim} P _ {1}) \neq 0, \forall \omega .$$

The theorem follows by noting that

$$\Psi (P _ {1}, P _ {2}) = (I + P _ {2} P _ {2} ^ {\sim}) ^ {- 1 / 2} (P _ {1} - P _ {2}) (I + P _ {1} ^ {\sim} P _ {1}) ^ {- 1 / 2}$$

since $\Psi ( P _ { 1 } , P _ { 2 } ) = - \tilde { N } _ { 2 } M _ { 1 } + \tilde { M } _ { 2 } N _ { 1 } = \tilde { M } _ { 2 } ( P _ { 1 } - P _ { 2 } ) M _ { 1 }$ and

$$\tilde {M} _ {2} ^ {\sim} \tilde {M} _ {2} = (I + P _ {2} P _ {2} ^ {\sim}) ^ {- 1}, \quad M _ {1} M _ {1} ^ {\sim} = (I + P _ {1} ^ {\sim} P _ {1}) ^ {- 1}.$$
