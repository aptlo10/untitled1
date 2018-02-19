import pyprog
from time import sleep

# Create Object
prog = pyprog.ProgressBar(" ", "", 34)
# Update Progress Bar
prog.update()

for i in range(34):
    # Do something
    sleep(0.1)
    # Set current status
    prog.set_stat(i + 1)
    # Update Progress Bar again
    prog.update()

# Make the Progress Bar final
prog.end()