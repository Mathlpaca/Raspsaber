#import the adxl345 module
import adxl345

#create ADXL345 object 
accel = adxl345.ADXL345()

#get axes as g 
axes = accel.getAxes(True) 
#to get axes as ms^2 use axes = accel.getAxes(False)

#put the axes into variables 
x = axes['x'] 
y = axes['y'] 
z = axes['z']
iterations =  1  

	

	
if iterations >= 1: 
	print axes 
	print x 
	print y 
	print z
	iterations = iterations + 1
if iterations > 10 
	
