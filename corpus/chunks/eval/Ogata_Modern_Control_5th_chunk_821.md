# 10–9 ROBUST CONTROL SYSTEMS

Suppose that given a control object (i.e., a system with a flexible arm) we wish to design a control system. The first step in the design of a control system is to obtain a mathematical model of the control object based on the physical law. Quite often the model may be nonlinear and possibly with distributed parameters. Such a model may be difficult to analyze. It is desirable to approximate it by a linear constant-coefficient system that will approximate the actual object fairly well. Note that even though the model to be used for design purposes may be a simplified one, it is necessary that such a model must include any intrinsic character of the actual object. Assuming that we can get a model that approximates the actual system quite well, we must get a simplified model for the purpose of designing the control system that will require a compensator of lowest order possible. Thus, a model of a control object (whatever it may be) will probably include an error in the modeling process. Note that in the frequency-response approach to control systems design, we use phase and gain margins to take care of the modeling errors. However, in the state-space approach, which is based on the differential equations of the plant dynamics, no such “margins” are involved in the design process.

Since the actual plant differs from the model used in the design, a question arises whether the controller designed using a model will work satisfactorily with the actual plant. To ensure that it will do so, robust control theory has been developed since around 1980.

Robust control theory uses the assumption that the models we use in designing control systems have modeling errors. We shall present an introduction to this theory in this section. Basically, the theory assumes that there is an uncertainty or error between the actual plant and its mathematical model and includes such uncertainty or error in the design process of the control system.

Systems designed based on the robust control theory will possess the following properties:

(1) Robust stability. The control system designed is stable in the presence of perturbation.   
(2) Robust performance. The control system exhibits predetermined response characteristics in the presence of perturbation.
