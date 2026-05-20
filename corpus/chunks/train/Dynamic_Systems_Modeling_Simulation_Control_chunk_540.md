Equation (10.6) is the closed-loop transfer function of the DC motor. We can use MATLAB’s feedback command to verify this result:

>> sysRL = tf(1, [L R])
>> sysMech = tf(1, [J b])
>> sysG = Km*sysRL*sysMech
>> sysH = Kb
>> sysT = feedback(sysG, sysH)
% create RL circuit transfer function
% create mechanical rotor transfer function
% create forward transfer function G(s)
% create feedback transfer function H(s) (gain)
% compute closed-loop transfer function T(s)

Of course, the user must enter numerical values for the system parameters $L , R , J , b , K _ { m } ,$ , and $K _ { b } .$ .

Given numerical values of the motor parameters, we could simulate the step response of the DC motor with Simulink using either the block diagram shown in Fig. 10.5 or the closed-loop transfer function shown in Fig. 10.6. Both simulations have advantages and disadvantages. Creating Fig. 10.5 using Simulink takes more effort but it provides complete system response information for current, motor torque, back-emf voltage, and motor velocity. A simulation using the closed-loop transfer function (Fig. 10.6) is easier to construct but it only provides the motor’s velocity response.
