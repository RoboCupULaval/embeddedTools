#Infrared sensors calibration#

You can find the parameters that best calibrate the ball sensor on a robot.
The robot has two ir sensors that detect the ball.
To calibrate:
- Connect to a robot via bluetooth when the 'debug' switch is at on
- Use the calibration command `calib-start` to start data acquisition.
- When you place the ball at a not kicking position enter the command `calib-sample-bad`, otherwise `calib-sample-good`
- When you have enough sample enter `calib-stop` to have a list of your samples
- Copy the output to a file and call the calibration script with `python3 calibration.py path/to/your/output`
- It should output the three weight parameters, you can test via bluetooth this output using `calib-test w0 w1 w2`
- If you are happy with the results, you can set the calibration parameters in `Robot_stm32f4discovery/Src/robocup/ball_detector.c` and flash the robot
