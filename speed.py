import time 
import simpleaudio as sa

def play_ding():
    wave_obj = sa.WaveObject.from_wave_file("ding.wav")
    wave_obj.play()

def exercise_set(speed_time, rest_time):
    play_ding()
    
    print(speed_time, " SECOND SET, STARTING NOW!")
    time.sleep(speed_time)
    
    play_ding()
    
    print("OK ", rest_time, " SECOND REST STARTING NOW!")
    time.sleep(rest_time)

def speed(sets):
    print("WELCOME! This will do the normal speed workout from practice. This will be done", sets, "time(s)!")
    input("To start, press any key!")
    
    for _ in range(sets):
        print("NEW SET, STARTING NOW!")
        #speed, then rest
        speed_time = 15
        rest_time = 15
        
        # Increasing section
        for i in range(5):
            exercise_set(speed_time, rest_time) 
            
            # Do not increase if on last round. 
            if i != 4:
                speed_time += 15
                rest_time += 15
        
        # Decreasing section
        for j in range(5):
            # Here, we decrease first so that we don't have to do 90 again. 
            speed_time -= 15
            rest_time -= 15
            exercise_set(speed_time, rest_time)
            
def main():
    sets = ""
    while (not sets.isdigit()):
        sets = input("How many sets would you like to run this program with? (insert number) ")
    speed(int(sets))
        
if __name__ == "__main__":
    main()