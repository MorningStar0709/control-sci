# 4.2 Control-System Design

Many different factors have to be considered in the design of a control system, for example:

- Attenuation of load disturbances   
- Reduction of the effect of measurement noise   
• Command signal following   
- Variations and uncertainties in process behavior

Load disturbances are disturbances that drive the process away from its desired behavior. Measurement noise is a disturbance that corrupts the information about the process obtained from the sensors. Process disturbances can enter the system in many different ways. It is convenient to consider them as if they enter the system in the same way as the control signal; in this way they will excite all modes of the system. For linear systems it also follows from the superposition principle that the assumption is not very critical. The measurement noise will be injected into the process through the control law. The command signal following expresses the property of the system to respond to command signals in a specified way.

Control problems can broadly speaking be classified into regulation problems and servo problems. The major issue in the regulation problem is to compromise between reduction of load disturbances and the fluctuations created by the measurement noise that is injected in the system due to the feedback. The command signal following is the major issue in servo problems. The major ingredients of a design problem are

- Purpose of the system   
- Process model   
• Model for disturbances   
- Model variations and uncertainties   
- Admissible control strategies   
- Design parameters
