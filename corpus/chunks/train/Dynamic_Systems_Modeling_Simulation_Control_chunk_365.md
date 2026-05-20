# Impulse Response of a First-Order System

Recall that an impulse input is a constant-magnitude input applied over an infinitesimal time duration. Therefore, we can obtain the impulse response of a system by evaluating the pulse response in the limit as pulse duration goes to zero. Consider again the first-order system shown in Fig. 7.7 with a pulse input of magnitude P and pulse duration T. The area or weight of the pulse is A = PT. The pulse response is given in Eq. (7.42), which is rewritten below (as $y _ { \mathrm { p u l s e } } )$ with pulse magnitude P = A∕T, or area/pulse duration

$$y _ {\text { pulse }} (t) = \frac {A b}{T} \left(1 - e ^ {- t / \tau}\right) - \frac {A b}{T} \left(1 - e ^ {- (t - T) / \tau}\right) U (t - T) \tag {7.43}$$

If we allow pulse duration T to go to zero in the limit to produce an impulse input, then the delayed unit step $U ( t - T )$ in Eq. (7.43) becomes U(t), which leads to

$$\frac {A b}{T} \left(1 - e ^ {- t / \tau}\right) - \frac {A b}{T} \left(1 - e ^ {- (t - T) / \tau}\right) = \frac {A b}{T} e ^ {- t / \tau} \left(e ^ {T / \tau} - 1\right) \tag {7.44}$$

The first-order system’s response to impulse A??(t) is obtained by taking the limit of Eq. (7.44) as T approaches zero

$$y _ {\text { impulse }} (t) = \lim _ {T \rightarrow 0} \frac {A b}{T} e ^ {- t / \tau} \left(e ^ {T / \tau} - 1\right) \tag {7.45}$$

Applying l’Hopital’s rule to evaluate the limit in Eq. (7.45), we obtain the impulse response

$$y _ {\text { impulse }} (t) = \lim _ {T \rightarrow 0} \frac {A b}{\tau} e ^ {- t / \tau} e ^ {T / \tau} = \frac {A b}{\tau} e ^ {- t / \tau} \tag {7.46}$$

Equation (7.46) shows that the impulse response of a first-order system exhibits a discontinuous step output at time t = 0, which then decays to zero in approximately four time constants. The magnitude of the impulse response at $t = 0 { \mathrm { i s } } A b / \tau$ , which makes sense intuitively, as A is the weight or strength of the impulse input, b is the coefficient that multiplies the input (see Eq. (7.25) or Fig. 7.7), and ?? is the system’s time constant. A first-order system with a small ?? has a very short transient response (i.e., a rapid response), which tends to increase the initial magnitude of the impulse response. The reader should be able to use the basic form of Eq. (7.46) to easily sketch the impulse response of a first-order system. All that is required is knowledge of the basic parameters of the first-order model (constants ?? and b) and the strength of the impulse input, A.
