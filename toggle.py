from machine import Pin
import time

# Set up the LEDs and buttons
led1 = Pin(18, Pin.OUT)
sw5 = Pin(22, Pin.IN, Pin.PULL_DOWN)
led2 = Pin(20, Pin.OUT)
sw3 = Pin(12, Pin.IN, Pin.PULL_DOWN)

# Initial states for LEDs and buttons
led1_state = False
led2_state = False
sw5_prev_state = False
sw3_prev_state = False

while True:
    # Read the current state of the buttons
    sw5_current_state = sw5.value()
    sw3_current_state = sw3.value()
    
    # Check for a button press (transition from not pressed to pressed) for sw5
    if sw5_current_state and not sw5_prev_state:
        led1_state = not led1_state  # Toggle the LED1 state
        led1.value(led1_state)  # Update LED1

    # Check for a button press (transition from not pressed to pressed) for sw3
    if sw3_current_state and not sw3_prev_state:
        led2_state = not led2_state  # Toggle the LED2 state
        led2.value(led2_state)  # Update LED2
    
    # Update previous button states
    sw5_prev_state = sw5_current_state
    sw3_prev_state = sw3_current_state

    # Small delay to debounce the button
    time.sleep(0.05)
            
    
