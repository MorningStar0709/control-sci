# 10.4 Solving Design Problems

Here is the procedure to use these tools to solve a design problem. First, collect your information:

 Plant model (as in previous chapters). (Know the gain, poles, and zeros of your plant)   
 Required step response specs: % Overshoot, Settling Time (2%), SSE (usually 0), and Gain Margin.   
 For Control eort, you need the Actuator Eort normalization constant, umax (sometimes also called cumax. If you don't care about actuator eort, set the constant to a really huge number.

Then follow these steps:

1. Copy the le userSetup.py to a new le such as setup\_problem5.py.   
2. Open the new le in a text editor or jupyter notebook.   
3. Set the simulation time where it says tmax = . This is how long the step response will be simulated and it should be about 5 times your desired settling time: tmax ≈ 5Tsd.   
4. Enter the transfer function of the system you wish to control (plant) (not your PID controller) under the comment #plant transfer function.   
5. Identify the highest frequency pole or zero in your plant. Multiply it by 20 and set the pp variable to that value. This is the controller normalization pole, pp.   
6. Edit the desired performance specs below their comment. Note that 5% overshoot should be entered 1.05, and gain margin should be entered in dB.   
7. Enter nvals. This is the number of values which will be tried of each parameter. Note that the total search time will be proportional to nvals3 so keep this below 10 until you get a feel for how long the searches take.   
8. Enter scale\_range. This is the range, r, from Equation 10.1.   
9. Save your le.   
10. Within python environment start setup\_problem5.py to initiate the search.
