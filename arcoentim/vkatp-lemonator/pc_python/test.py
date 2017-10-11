import lemonator
import time

print( "Python interface demo running" )
hw = lemonator.lemonator( 2 )
distance = hw.distance
print(distance.read_mm())
