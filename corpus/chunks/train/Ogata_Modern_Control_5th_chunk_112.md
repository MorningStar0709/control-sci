from which we get the transfer function $E _ { o } ( s ) / E _ { i } ( s )$ to be

$$\frac {E _ {o} (s)}{E _ {i} (s)} = - \frac {Z _ {4} Z _ {2} - Z _ {3} Z _ {1}}{Z _ {3} \left(Z _ {1} + Z _ {2}\right)} \tag {3-41}$$

To find the transfer function $E _ { o } ( s ) / E _ { i } ( s )$ of the circuit shown in Figure 3–26, we substitute

$$Z _ {1} = \frac {1}{C s}, \quad Z _ {2} = R _ {2}, \quad Z _ {3} = R _ {1}, \quad Z _ {4} = R _ {1}$$

into Equation (3–41). The result is

$$\frac {E _ {o} (s)}{E _ {i} (s)} = - \frac {R _ {1} R _ {2} - R _ {1} \frac {1}{C s}}{R _ {1} \left(\frac {1}{C s} + R _ {2}\right)} = - \frac {R _ {2} C s - 1}{R _ {2} C s + 1}$$

which is, as a matter of course, the same as that obtained in Problem A–3–6.

A–3–8. Obtain the transfer function $E _ { o } ( s ) / E _ { i } ( s )$ of the operational-amplifier circuit shown in Figure 3–28.

Solution. We will first obtain currents $i _ { 1 } , i _ { 2 } , i _ { 3 } , i _ { 4 }$ , and $i _ { 5 }$ .Then we will use node equations at nodes A and B.

$$i _ {1} = \frac {e _ {i} - e _ {A}}{R _ {1}}; \quad i _ {2} = \frac {e _ {A} - e _ {o}}{R _ {3}}, \quad i _ {3} = C _ {1} \frac {d e _ {A}}{d t}i _ {4} = \frac {e _ {A}}{R _ {2}}, \quad i _ {5} = C _ {2} \frac {- d e _ {o}}{d t}$$

At node A, we have $i _ { 1 } = i _ { 2 } + i _ { 3 } + i _ { 4 }$ , or

$$\frac {e _ {i} - e _ {A}}{R _ {1}} = \frac {e _ {A} - e _ {o}}{R _ {3}} + C _ {1} \frac {d e _ {A}}{d t} + \frac {e _ {A}}{R _ {2}} \tag {3-42}$$

At node B, we get $i _ { 4 } = i _ { 5 }$ , or

$$\frac {e _ {A}}{R _ {2}} = C _ {2} \frac {- d e _ {o}}{d t} \tag {3-43}$$

By rewriting Equation (3–42), we have

$$C _ {1} \frac {d e _ {A}}{d t} + \left(\frac {1}{R _ {1}} + \frac {1}{R _ {2}} + \frac {1}{R _ {3}}\right) e _ {A} = \frac {e _ {i}}{R _ {1}} + \frac {e _ {o}}{R _ {3}} \tag {3-44}$$

From Equation (3–43), we get

$$e _ {A} = - R _ {2} C _ {2} \frac {d e _ {o}}{d t} \tag {3-45}$$

By substituting Equation (3–45) into Equation (3–44), we obtain

$$C _ {1} \left(- R _ {2} C _ {2} \frac {d ^ {2} e _ {o}}{d t ^ {2}}\right) + \left(\frac {1}{R _ {1}} + \frac {1}{R _ {2}} + \frac {1}{R _ {3}}\right) \left(- R _ {2} C _ {2}\right) \frac {d e _ {o}}{d t} = \frac {e _ {i}}{R _ {1}} + \frac {e _ {o}}{R _ {3}}$$

Taking the Laplace transform of this last equation, assuming zero initial conditions, we obtain

$$- C _ {1} C _ {2} R _ {2} s ^ {2} E _ {o} (s) + \left(\frac {1}{R _ {1}} + \frac {1}{R _ {2}} + \frac {1}{R _ {3}}\right) (- R _ {2} C _ {2}) s E _ {o} (s) - \frac {1}{R _ {3}} E _ {o} (s) = \frac {E _ {i} (s)}{R _ {1}}$$

from which we get the transfer function $E _ { o } ( s ) / E _ { i } ( s )$ as follows:
