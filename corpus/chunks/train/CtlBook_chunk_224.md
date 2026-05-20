# Create the root locus plot
plt.figure(figsize=(10, 8))
control.root_locus(sys, grid=True)
