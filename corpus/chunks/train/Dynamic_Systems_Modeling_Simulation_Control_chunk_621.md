# Digital Controller Algorithms

In the previous subsection, we described the digital controller as an algorithm that resides in the computer or microprocessor. The reader might ask how a PID or lead controller transfer function is converted into an algorithm that exists as software. As a first example, consider the basic PI control logic

$$u (t) = K _ {P} e (t) + K _ {I} \int e (t) d t \tag {10.58}$$

Equation (10.58) involves two continuous-time (analog) signals: error $e ( t )$ and control signal $u ( t )$ . Therefore, we must obtain a discrete-time representation of Eq. (10.58) for use in a digital PI algorithm. To begin, let us assume that the feedback error is a digital signal (note that the output of the summing junction in Fig. 10.57 is a digital signal). The digital error signal can be denoted as $e ( k T _ { s } )$ , where k is the sample index and $T _ { s }$ is the sample period (or step size) in seconds. Hence, the digital error signal only exists at times $t = k T _ { s }$ , k = 1, 2, … , etc. For convenience, let us omit the sample period $T _ { s }$ in the notation for the digital signal with the understanding that $e ( k ) = e ( k T _ { s } )$ ; therefore, $e ( k - 1 )$ ) is the digital error signal one sample period before $e ( k )$ . Using this notation, a digital representation of the PI algorithm (10.58) is

$$u (k) = K _ {P} e (k) + K _ {I} w (k) \tag {10.59}$$

where the digital signal w(k) is the numerical integral of the digital signal $e ( k )$ as computed by rectangular-rule integration:

$$w (k) = w (k - 1) + T _ {s} e (k) \tag {10.60}$$

Clearly, the product $T _ { s } e ( k )$ is the rectangular area associated with the time step $T _ { s } ,$ , as shown by Fig. 10.59. Of course, when the algorithm is initiated and processes the first sample $( k = 1 )$ , the initial value of the integral is $w ( 0 ) = 0$ . Equations (10.59) and (10.60) are the discrete-time equations that represent the PI control logic (10.58). Implementing the PI controller in the digital computer requires two lines of computer code: Eq. (10.60) computes the numerical integral of the digital error signal, and Eq. (10.59) computes the digital control signal u(k) using the PI gains $K _ { P }$ and $K _ { I }$ . Remember that the digital control signal $u ( k )$ must be converted into a continuous (analog) signal $u ( t )$ for use by the physical actuator and this D/A conversion is typically performed by a zero-order hold as shown in Fig. 10.58.
