# 1.4 THE DESIGN PROCESS

In general terms, the objective of a control system is to maintain the vector of outputs $\mathbf{y}(t)$ close to the vector of desired values $\mathbf{y}_{d}(t)$ , in spite of the disturbances. The design of a control system is divided into two distinct portions that deal respectively with the abstract and physical levels.

The end product of the design at the abstract level is the specification of the mathematical operator C, which acts on the measurements $y_{m}$ and the desired inputs $y_{d}$ to produce the command signals u. In order to carry this out, the following information is required:

1. An approximation of $\mathcal{P}$ , the plant operator; this approximation is called a mathematical model.   
2. Characterizations of the functions $\mathbf{y}_d(t)$ and $\mathbf{w}(t)$ , the desired values and disturbances. These functions may be described in the time domain as specific functions (e.g., steps) or as sets of functions. They are often characterized in the frequency domain according to properties of their spectra.   
3. A set of performance specifications.   
4. Mathematical models for the actuators and sensors. The latter include the characterization of the noise variables $\mathbf{v}(t)$ , if such are used to represent measurement errors.   
5. Restrictions on the structure of $\mathcal{C}$ . For example, analog proportional, integral, derivative (PID) controllers have the mathematical structure

$$u (t) = \frac {1}{T _ {I}} \int (y _ {d} - y _ {m}) d t + k (y _ {d} - y _ {m}) + T _ {D} \frac {d}{d t} (y _ {d} - y _ {m})$$

and the design is reduced to the choice of the constants $T_{I}$ , k, and $T_{D}$ . Digital systems may also be limited as to structure; in many turnkey systems, control algorithms must be built from certain given software “building blocks.”

At the physical level, one is concerned with the following:

1. The choice of actuators and sensors.   
2. The selection of the control elements. In most cases, the control system includes a computer, which raises issues of both hardware and software.   
3. The design of the man-machine interface. This includes the definition of alarm conditions and backup procedures as well as the selection of display devices.
