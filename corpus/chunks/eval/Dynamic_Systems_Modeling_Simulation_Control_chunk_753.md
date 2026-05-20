Let us begin the Simulink model construction by opening a new working template and dragging and dropping two Integrator blocks from the Continuous library.
The reader should note that the integrator-block icon is 1/s, which is the Laplace transform representation of integration (Simulink does not use Laplace-transform methods to obtain the response).
First, we must insert a summing junction Sum block (from the Math Operations library) to the left of the ẏ integrator.
This summing junction is used to create the signal $0 .
4 z - 3 y$ , which is needed for the $\dot { y }$ integrator.
Double clicking the Sum block opens a dialog box that allows the user to set the number of input ports and their associated signs for summation.
For example, setting the string $\because { } + { } + { } - { } ^ { \prime } { }$ in the List of signs dialog entry will create a summing junction where the top two input ports have positive signs and the bottom port has a negative sign.
In this case, we enter ‘+ −’ for the first summing junction because we wish to create the signal 0.4z − 3y.
Next, we feed back signal paths for y and z and send these new feedback paths to the summing junction.
Figure C.8 shows a partially completed Simulink model where the block diagram to synthesize Eq.
(C.8) has been constructed.
A feedback signal for y is created by “picking off” a signal from the integrator block output signal path.
This signal “pick-off” is performed by right-clicking the original path, and holding and dragging the new path backward to the left.
Picking off a new signal results in the junction point (dot) after the integrator block, as shown in Fig.
C.8 (the reader should note that junction points share the same signal-path data, whereas crossing signal paths do not).
A feedback signal path for z is performed in the same manner and a junction point is shown after the ż integrator in Fig.
C.8.
The two feedback signals must be multiplied by constants (or “gained”) before they are summed in order to create the signal 0.4z − 3y.
Therefore, the user must drag and drop two Gain blocks (from the Math Operations library) to the Simulink model (note that the Gain block has a triangle shape which is analogous to an op amp for boosting electrical signals).
The Gain blocks show one input and output port and the default orientation is left-to-right.
Because our feedback signals are from right-to-left, we need to “flip” the block.
