wkt_type = input("What type of workout equipment do you have? (Bodyweight or Weights): ")

if wkt_type == 'Bodyweight' or wkt_type == 'bodyweight':
    wkt_target = input("What muscles do you want to workout?: ")
    if wkt_target == 'Chest' or wkt_target == 'chest':
        print('''For hitting chest here are some workouts with increasing intensity:
        
        Knee Pushups:
            1) Begin in a push-up position on your knees. Break at the elbow and shoulder joint.
            2) Lower your body, keeping elbows close.
            3) Push back up to the starting position.
                    
        Incline Pushups:
            1) Stand facing bench or sturdy elevated platform.
            2) Place hands on edge of bench or platform, slightly wider than shoulder width.
            3) Slowly lower your body until your chest almost touches the bench.
            4) Push body up until arms are extended.
        
        Push Ups:
            1) Place your hands firmly on the ground, directly under shoulders.
            2) Flatten your back so your entire body is straight and slowly lower your body
            3) Draw shoulder blades back and down, keeping elbows tucked close to your body
            4) Exhale as you push back to the starting position.
        
        Dips:
            1) Hold your body with arms locked above the equipment
            2) Lower your body slowly while leaning forward, flare out your elbows
            3) Raise your body above the bars until your arms are locked.
       
        Decline Pushups:
            1) Use a bench to elevate your feet.
            2) Put your hands slightly wider than shoulder-width.
            3) Slowly lower your body until your chest almost touches the ground
            4) Raise your body until you almost lock your elbows.

        ''')

    if wkt_target == 'Quads' or wkt_target == 'quads' or wkt_target == 'Quadriceps' or wkt_target == 'quadriceps':
        print(''' Here are some workouts to hit your Quads:
        
        Squats:
            1) Stand with your feet shoulder width apart.
            2) flex your knees and hips and sit back into the squat while lowering your body
            3) Continue down to full depth
            4) Return to starting position.
        
        Forward Lunges:
            1) Step forward with one leg.
            2) Lower your body until your rear knee nearly touches the ground.
            3) Ensure you remain upright, and your front knee stay above the front foot.
            4) Push off the floor with your front foot
               until you return to the starting position. Switch legs.
              
        Jump Squats:
            1) Stand with your feet shoulder-width apart.
            2) Start by doing a regular squat, then engage your core and jump up explosively.
            3) When you land, lower your body back into the squat position.
        
        Bulgarian Split Squats:
            1) Stand with your back to a bench (or raised surface) and place one of your feet on the bench.
            2) Squat down until your front leg is about parallel to the floor.
            3) Go back to the starting position. After completing the desired amount of reps, 
               switch legs and repeat.
        ''')
        
        
if wkt_type == 'Weights' or wkt_type == 'weights':
    wkt_target = input("What muscles do you want to workout?: ")
    if wkt_target == 'Biceps' or wkt_target == 'biceps':
        print('''For hitting biceps here are some workouts with increasing intensity:
        
        Dumbell Curl:
            1) Stand up straight with a dumbbell in each hand at arm's length.
            2) Raise one dumbbell and twist your forearm until it is vertical and your palm faces the shoulder.
            3) Lower to original position and repeat with opposite arm
              
        Dumbell Hammer Curl:
            1) Hold the dumbbells with a neutral grip (thumbs facing the ceiling).
            2) Slowly lift the dumbbell up to chest height
            3) Return to starting position and repeat.
                    
        Dumbell Reverse Curl:
            1) Grab the dumbbells with a pronated (overhand) grip. 
               You can do this exercise thumbless if it's more comfortable on your wrists.
            2) Flex at the elbows until your biceps touch your forearms. 
               Try not to let your elbows flair outward.
        
        Dumbell Real Delt Row:
            1) Hinge forward at the hips while maintaining a flat back. 
               Try to get your torso as close to parallel with the ground as your mobility will allow for.
            2) Let your arms hang in front of you. Pull your elbows back towards the ceiling 
               while flaring your elbows outward
                
        ''')
    
    if wkt_target == 'Triceps' or wkt_target == 'triceps':
        print('''For hitting biceps here are some workouts with increasing intensity:
        
        Dumbell Bench Press:
            1) Start by lying flat on a bench with a dumbbell in each hand.
            2) Hold the dumbbells at chest level with your palms facing forward.
            3) Engage your core and press the dumbbells upward until your arms are fully extended.
        
        Dumbell Skullcrusher:
            1) Lay flat on the floor or a bench with your fists extended to the ceiling and a neutral grip.
            2) Break at the elbows until your fists are by your temples. 
              Then extend your elbows and flex your triceps at the top. 
              
        Dumbell Seated Overhead Tricep Extension:
            1) Sit on the bench and hold a dumbbell with both hands. Raise the dumbbell overhead at arms length,
               holding the weight up with the palms of your hands.
            2) Keep your elbows in while you lower the weight behind your head, your upper arms stationary.
            3) Raise the weight back to starting position.
            
        Dumbell Tricep Kickback:
            1) Start by standing with your feet shoulder-width apart and holding a dumbbell in one hand.
            2) Bend at the waist and place your opposite hand on your knee for support.
            3) From this starting position, extend your arm backwards so that the dumbbell is behind your body.
            4) Make sure to keep your elbow close to your body and your core engaged throughout the movement.

        ''')