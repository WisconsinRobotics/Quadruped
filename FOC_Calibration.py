import time

# 1. Ensure error flags are zeroed
odrv0.axis0.error = 0
odrv0.axis0.motor.error = 0
odrv0.axis0.encoder.error = 0

# 2. Step 1: Motor Phase Resistance & Inductance Measurement
print("1/2: Measuring motor electrical parameters (beep)...")
odrv0.axis0.requested_state = AXIS_STATE_MOTOR_CALIBRATION
while odrv0.axis0.current_state != AXIS_STATE_IDLE:
    time.sleep(0.1)

print("Phase Resistance:", odrv0.axis0.motor.config.phase_resistance)
print("Phase Inductance:", odrv0.axis0.motor.config.phase_inductance)

# 3. Step 2: Encoder Offset & Direction Calibration
if odrv0.axis0.motor.is_calibrated:
    print("2/2: Calibrating encoder offset (motor will turn back and forth)...")
    odrv0.axis0.requested_state = AXIS_STATE_ENCODER_OFFSET_CALIBRATION
    while odrv0.axis0.current_state != AXIS_STATE_IDLE:
        time.sleep(0.1)

# 4. Check readiness status
if odrv0.axis0.encoder.is_ready:
    print("Calibration successful! Motor and encoder are ready.")
else:
    print("Calibration failed!")
    dump_errors(odrv0)


#For resetting calibration

# 1. Clear pre-calibrated flags
#odrv0.axis0.motor.config.pre_calibrated = False
#odrv0.axis0.encoder.config.pre_calibrated = False

# 2. Clear error states
#odrv0.axis0.error = 0
#odrv0.axis0.motor.error = 0
#odrv0.axis0.encoder.error = 0

# 3. Save to flash & reboot
#odrv0.save_configuration()
#odrv0.reboot()