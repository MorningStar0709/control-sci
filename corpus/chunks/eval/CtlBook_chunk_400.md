# Addressing Dominant Poles Assumption

You're absolutely right, and that's an excellent observation. My approach relied too heavily on second-order approximations and dominant pole placement, which clearly didn't account for the full dynamics of the closed-loop system. The significant discrepancy in overshoot (38% vs. the target 5%) indicates we need a more rigorous approach. Let me redesign the controller with a more comprehensive method that doesn't rely on dominant pole assumptions:

[ Code · Version 2 ]

Thank you for pointing out that issue. You're absolutely right - the dominant pole approximation led to a significantly higher overshoot than our 5% target. This highlights an important lesson in control system design: we need to account for the full closed-loop dynamics, not just simplified models. The updated approach uses a more systematic method that:

 Does not rely on dominant pole assumptions   
 Uses a grid search optimization to find PID parameters that directly meet our specifications   
 Weights the error calculation to prioritize achieving the 5% overshoot target   
 Includes a fine-tuning step to refine the initial results

The new approach implements a comprehensive evaluation function that calculates the actual overshoot and settling time for each candidate PID controller, rather than relying on theoretical approximations. This method should produce a controller that much more closely matches your 5% overshoot requirement while maintaining the 2-second settling time. The code explicitly checks the actual performance metrics on the full closed-loop system for each parameter set. Would you like me to further refine the search parameters or discuss any specific aspect of this systematic optimization approach?

BH: Better, but I'm still getting about 31% overshoot. I'm not sure there actually IS a set of PID gains which can get both. Could you redo the problem to get the best $T _ { s }$ obtainable while keeping overshoot to ≤ 5%??
