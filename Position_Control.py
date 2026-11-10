import time

# 1. Clear any active error flags
odrv0.axis0.error = 0

# 2. Set control mode to Position Control with Trapezoidal Trajectory
odrv0.axis0.controller.config.control_mode = CONTROL_MODE_POSITION_CONTROL
odrv0.axis0.controller.config.input_mode = INPUT_MODE_TRAP_TRAJ

# 3. Configure motion profile limits (smooth acceleration to protect 12V supply)
odrv0.axis0.trap_traj.config.vel_limit = 10.0      # Max speed: 10 turns/sec
odrv0.axis0.trap_traj.config.accel_limit = 5.0     # Accel: 5 turns/sec²
odrv0.axis0.trap_traj.config.decel_limit = 5.0     # Decel: 5 turns/sec²

# 4. Enter Closed-Loop FOC
odrv0.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL


#IDLE
# Disarm Axis 0 (Put into IDLE state)
#odrv0.axis0.requested_state = AXIS_STATE_IDLE

# Disarm Axis 1 (Optional safety sweep)
#odrv0.axis1.requested_state = AXIS_STATE_IDLE

# Verify current state (1 corresponds to AXIS_STATE_IDLE)
#print("Axis 0 State:", odrv0.axis0.current_state)

# Move to 5.0 turns forward
#odrv0.axis0.controller.input_pos = 5.0

# Move to 10.5 turns
#odrv0.axis0.controller.input_pos = 10.5

# Move back to origin (0.0 turns)
#odrv0.axis0.controller.input_pos = 0.0

# Move 2.5 turns in reverse
#odrv0.axis0.controller.input_pos = -2.5