wkt_type = input("What type of workout equipment do you have? (Bodyweight or Weights): ")

if wkt_type == 'Bodyweight' or wkt_type == 'bodyweight':
    wkt_target = input("What muscles do you want to workout?: ")
    if wkt_target == 'Chest' or wkt_target == 'chest':
        print('''For hitting chest here are some workouts with increasing intensity:
        
        Knee Pushups:
            1) Begin in a push-up position on your knees. Break at the elbow and shoulder joint.
            2)Lower your body, keeping elbows close.
            3)Push back up to the starting position.
                    
        Incline Pushups:
            1)Stand facing bench or sturdy elevated platform.
            2)Place hands on edge of bench or platform, slightly wider than shoulder width.
            3)Slowly lower your body until your chest almost touches the bench.
            4)Push body up until arms are extended.
        
        Push Ups:
            1) Place your hands firmly on the ground, directly under shoulders.
            2) Flatten your back so your entire body is straight and slowly lower your body
            3) Draw shoulder blades back and down, keeping elbows tucked close to your body
            4)Exhale as you push back to the starting position.
        
        Dips:
            1) Hold your body with arms locked above the equipment
            2)Lower your body slowly while leaning forward, flare out your elbows
            3) Raise your body above the bars until your arms are locked.
       
        Decline Pushups:
            1) Use a bench to elevate your feet.
            2) Put your hands slightly wider than shoulder-width.
            3) Slowly lower your body until your chest almost touches the ground
            4)Raise your body until you almost lock your elbows.

        ''')
        wkt_extend = input("Do you want more workouts?(Y or N): ")
        if wkt_extend == 'Y' or wkt_extend == 'y':
            print('''Here are some more workouts to hit chest:
            
                 
            ''')
        
        if wkt_target == 'Quads' or wkt_target == 'quads':
            
            if wkt_target == 'Quads' or wkt_target == 'quads' or wkt_target == 'Quadriceps' or wkt_target == 'quadriceps':
                print(''' Here are some workouts to hit your Quads:
        
        Squats:
            1)Stand with your feet shoulder width apart.
            2)flex your knees and hips and sit back into the squat while lowering your body
            3)Continue down to full depth
            4)Return to starting position.
        Forward Lunges:
            1) Step forward with one leg.
            2) Lower your body until your rear knee nearly touches the ground.
            3)Ensure you remain upright, and your front knee stay above the front foot.
            4)Push off the floor with your front foot
              until you return to the starting position. Switch legs.''')
        
        
if wkt_type == 'Weights' or wkt_type == 'weights':
    
    print(2)