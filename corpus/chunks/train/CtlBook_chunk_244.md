# Simulate step responses from every input to every output: 2x2=4 responses
stepResponseData = ctl.step_response(sys, t)  # note py.ctl generates its own input
t = stepResponseData.time
y1 = stepResponseData.outputs
