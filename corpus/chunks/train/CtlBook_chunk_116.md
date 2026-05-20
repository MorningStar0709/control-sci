# Example 4.1

Consider the car suspension Example 2.1 and Example 2.10. Derive the state space representation.

The EOMs were:

$$M _ {w} \ddot {x} _ {2} + B _ {s} (\dot {x} _ {2} - \dot {x} _ {3}) + K _ {s} (x _ {2} - x _ {3}) + K _ {t} (x _ {2} - x _ {1}) = 0M _ {v} \ddot {x} _ {3} + B _ {s} (\dot {x} _ {3} - \dot {x} _ {2}) + K _ {s} (x _ {3} - x _ {2}) = 0$$

Note that the input to this system is $x _ { 1 } ,$ , the displacement of the road. We can re-write the EOMS to put the input on the RHS:

$$M _ {w} \ddot {x} _ {2} + B _ {s} (\dot {x} _ {2} - \dot {x} _ {3}) + K _ {s} (x _ {2} - x _ {3}) + K _ {t} x _ {2} = K _ {t} x _ {1}M _ {v} \ddot {x} _ {3} + B _ {s} (\dot {x} _ {3} - \dot {x} _ {2}) + K _ {s} (x _ {3} - x _ {2}) = 0$$

Let the state vector be:

$$X = [ x _ {2} \dot {x} _ {2} x _ {3} \dot {x} _ {3} ] ^ {T}$$

(where T indicates transpose to make X a column vector) and its derivative is

$$\dot {X} = [ \dot {x} _ {2} \quad \ddot {x} _ {2} \quad \dot {x} _ {3} \quad \ddot {x} _ {3} ] ^ {T}$$

Rearranging the EOMS:

$$\ddot {x} _ {2} = \frac {1}{M _ {w}} \left[ - (K _ {T} + K _ {s}) x _ {2} - B _ {s} \dot {x} _ {2} + K _ {s} x _ {3} + B _ {s} \dot {x} _ {3} \right] + \frac {1}{M _ {w}} K _ {t} x _ {1}\ddot {x} _ {3} = \frac {1}{M _ {v}} \left[ + K _ {s} x _ {2} + B _ {s} \dot {x} _ {2} - K _ {s} x _ {3} - B _ {s} \dot {x} _ {3} \right]$$

We will treat the variable $x _ { 1 }$ in the ${ \ddot { x } } _ { 2 }$ EOM as our system input:

$$U = [ x _ {1} ]$$

We then have the 4x4 matrix state equations:

$$
\dot {X} = A X + B U
\dot {X} = \left[ \begin{array}{c} \dot {x} _ {2} \\ \ddot {x} _ {2} \\ \dot {x} _ {3} \\ \ddot {x} _ {3} \end{array} \right] = \left[ \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ \frac {- (K _ {T} + K _ {s})}{M _ {w}} & \frac {- B _ {s}}{M _ {w}} & \frac {K _ {s}}{M _ {w}} & \frac {B _ {s}}{M _ {w}} \\ 0 & 0 & 0 & 1 \\ \frac {K _ {s}}{M _ {v}} & \frac {B _ {s}}{M _ {v}} & \frac {- K _ {s}}{M _ {v}} & \frac {- B _ {s}}{M _ {v}} \end{array} \right] \left[ \begin{array}{c} x _ {2} \\ \dot {x} _ {2} \\ x _ {3} \\ \dot {x} _ {3} \end{array} \right] + \left[ \begin{array}{c} 0 \\ \frac {K _ {t}}{M _ {w}} \\ 0 \\ 0 \end{array} \right] [ x _ {1} ]
$$

Where we have set the dimensions of A, B according to the scheme above with

$$p = \text { number of states } = 4q = \text { number of inputs } = 1r = \text { number of outputs } = 1$$
