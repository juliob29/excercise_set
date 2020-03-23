import time 
import simpleaudio as sa

def play_ding():
    wave_obj = sa.WaveObject.from_wave_file("ding.wav")
    wave_obj.play()

# If this is the last_set, we do not do rest.
def exercise_set(speed_time, rest_time, last_set):
    play_ding()
    
    print(speed_time, " SECOND SET, STARTING NOW!")
    time.sleep(speed_time)
    
    play_ding()
    if not last_set:
        print("OK ", rest_time, " SECOND REST STARTING NOW!")
        time.sleep(rest_time)

def speed(sets):
    print("WELCOME! This will do the normal speed workout from practice. This will be done", sets, "time(s)!")
    
    
    for _ in range(sets):
        input("To start this set, press any key!")
        print("NEW SET, STARTING NOW!")
        #speed, then rest
        speed_time = 15
        rest_time = 15
        
        # Increasing section
        for i in range(5):
            exercise_set(speed_time, rest_time, False) 
            
            # Do not increase if on last round. 
            if i != 4:
                speed_time += 15
                rest_time += 15
        
        # Decreasing section
        for j in range(4):
            # Here, we decrease first so that we don't have to do the high interval again. 
            speed_time -= 15
            rest_time -= 15

            # Handle the logic for the final set (no rest on final)
            if j != 3:
                exercise_set(speed_time, rest_time, False)
            else:
                exercise_set(speed_time, rest_time, True)
        
        play_ding()
        print("Set complete!")
    
            
def main():
    sets = ""
    while (not sets.isdigit()):
        sets = input("How many sets would you like to run this program with? (insert number) ")
    speed(int(sets))
        
if __name__ == "__main__":
    main()