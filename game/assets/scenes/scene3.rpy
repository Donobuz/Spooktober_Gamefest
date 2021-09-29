label scene3:
    scene car with Fade(2.0,0.0,4.0)
    "You all pile in Jesse’s minivan, which is covered in a disturbing amount of yellow fur." with text_dissolve
    "Jesse is driving with Camilla next to him in the passenger seat while you squeeze in between Sequinn’s huge costume and Tanner’s huge angst." with text_dissolve

    mc "It's ummm... bright in here Jesse." with text_dissolve

    show t_neutral at right
    with moveinright

    t_right "Why does your car look like you skinned Big Bird?" with text_dissolve

    show j_annoyed at left
    with moveinleft

    j_left "Ruuude! Yellow is my happy color!" with text_dissolve

    t_right "It's a terrible color, so it makes sense why you like it" with text_dissolve

    show t_neutral at offscreenright
    show j_annoyed at offscreenleft
    with dict_emotion_change
    # with dissolve

    hide t_neutral
    hide j_annoyed

    show c_neutral at right
    with moveinright

    c_right "HEY! Let's just listen to the radio okay?" with text_dissolve

    "Camilla clicks the radio on and changes it to a station."
    play sound "<from 2 to 4>../game/assets/music/radiostatic.mp3" fadeout 1.0
    play music "../game/assets/music/chugjug.mp3" fadein 15.0 loop
    pause(10.0)
 
    show j_neutral at left
    with moveinleft

    j_left "Actually I don't like this song. Can you change it?" with text_dissolve

    c_right "Yeah, sure babe" with text_dissolve

    show j_neutral at offscreenleft
    with ease
    # with dissolve

    "She switches to a different station." with text_dissolve
    stop music
    play sound "<from 2 to 4>../game/assets/music/radiostatic.mp3" fadeout 1.0
    play music "../game/assets/music/nyancat.mp3" fadein 10.0 loop
    pause(10.0)

    show s_annoyed at left
    with moveinleft

    s_left "Ughhhhh... This is the worst song ever! Please change it..." with text_dissolve

    c_right "Alright, alright." with text_dissolve

    show s_annoyed at offscreenleft
    with ease

    stop music
    # play sound "<from 2 to 4>../game/assets/music/radiostatic.mp3" fadeout 1.0
    # play music "../game/assets/music/nyancat.mp3" fadein 10.0 loop
    # pause(10.0)

    show t_annoyed at left
    with moveinleft

    t_left "Oh hell no. Not this lame music!" with text_dissolve

    show c_annoyed at right
    with dict_emotion_change

    hide c_neutral

    c_right "Kay, that's it! No more music." with text_dissolve

    show t_annoyed at offscreenleft
    show c_annoyed at offscreenright
    with ease

    "A period of awkward silence rushes over the group" with text_dissolve

    mc "{i} We've been friends for so long that we bicker like siblings. I should say something to cut the tension..." with text_dissolve

    mc "Since it's Halloween, how about we share scary stories?" with text_dissolve

    "After a moment of consideration, everyone agrees; however, Camilla was very hesitant." with text_dissolve

    show s_neutral at left
    with moveinleft

    s_left "Oh, I have a scary story!" with text_dissolve

    # $renpy.movie_cutscene("../game/assets/movie/phonebooth.mpeg")

    show my_movie:
        zoom 0.5
    with Fade(0.0, 0.0, 4.0)
    pause 98
    hide s_neutral
    hide my_movie


    show c_scared at right
    with moveinright

    c_right "Quinn, you horrible monster! Why would you tell me that story!"

    show s_happy at left
    with moveinleft

    s_left "Hey, it’s a pretty cool ghost story. I’ve heard the ringing too! All the way from my dorm!"

    c_right "Stooooop!"
    
    menu:
        "That's more sad than scary...":
            jump more_sad_than_scary
            hide text
            
        "Okay, yeah {i}never{/i} visiting your dorm again...":
            jump never_visit_dorm
            hide text

label more_sad_than_scary:
    show s_neutral at left
    with dict_emotion_change
    hide s_happy

    s_left "Hey, that's why I just stay single." with text_dissolve

    show c_scared at offscreenright

    show t_neutral at right
    with dict_emotion_change
 
    t_right "I doubt it's actually an option for you." with text_dissolve

    show s_annoyed at left
    with dict_emotion_change
    hide s_neutral

    s_left "You are unbearable!" with text_dissolve

    mc "Hey, you don't need to do that right now..." with text_dissolve

    show s_annoyed at offscreenleft
    hide s_annoyed

    show j_annoyed at left
    with dict_emotion_change

    j_left "[main_char] is right. You two stop before I turn around and we all go home!" with text_dissolve

    show t_annoyed at right
    with dict_emotion_change
    hide t_neutral

    t_right "What are you? My mom?" with text_dissolve

    "Jesse growls at them through the rearview mirror." with text_dissolve


    show j_annoyed at offscreenright
    hide j_annoyed

    show s_neutral at left
    with dict_emotion_change

    "Both Tanner and Jesse are startled by the manly growl"

    t_and_s "Sorry, Jesse." with text_dissolve
    jump scene3continue


label never_visit_dorm:
    show c_scared at offscreenright
    hide c_scared

    show j_neutral at right
    with dict_emotion_change

    j_right "Ohhh... is the big, brave [main_char] afraid of a ghost story?" with text_dissolve

    show s_neutral at left
    with dict_emotion_change
    hide s_happy

    s_left "It's definitely the way I told the story. I have a knack for this kind of stuff." with text_dissolve

    show j_neutral at offscreenright
    show t_neutral at right
    with dict_emotion_change

    t_right "I'll admit it... the story wasn't too bad. Color me impressed." with text_dissolve

    show s_happy at left
    with dict_emotion_change
    hide s_neutral
    
    s_left "We should color you any color besides grey and black." with text_dissolve

    show t_annoyed at right
    with dict_emotion_change
    hide t_neutral

    t_right "It's a slimming color!" with text_dissolve

    mc "It's a shade."

    t_right "Shut it!"

    jump scene3continue

label scene3continue:
    
    show s_happy at offscreenleft
    show s_neutral at offscreenleft
    show c_neutral at left
    with dict_emotion_change

    hide s_neutral
    hide s_happy

    c_left "Hey, let's try the whole music thing again." with text_dissolve
    
    show t_neutral at right
    with dict_emotion_change
    hide t_annoyed

    t_right "No way! It's my turn and I have a better one!" with text_dissolve

    mc "Go for it Tanner! I love a good scare." with text_dissolve

    t_right "Have you guys heard the story about where the party is this year?" with text_dissolve

    mc "Nope." with text_dissolve

    show j_neutral at right
    show t_neutral at offscreenright
    with dict_emotion_change

    j_right "There's a story?" with text_dissolve

    show c_scared at left
    with dict_emotion_change
    hide c_neutral

    c_left "Pleeeeease tell me it's not too spooky." with text_dissolve

    show j_neutral at offscreenright
    show s_neutral at right
    with dict_emotion_change
    hide j_neutral

    s_right "When Tanner tells a story, it's always too spooky." with text_dissolve

    show c_scared at offscreenleft
    show t_neutral at left
    with dict_emotion_change
    hide c_scared

    t_left "I eat spooky for breakfast, Camilly." with text_dissolve

    show s_neutral at offscreenright
    with dict_emotion_change
    hide s_neutral

    t_left "Now listen up! I'm only saying this once." with text_dissolve
    t_left "This year, the party is being held in the woods that used to be the hunting ground of a notorious serial killer." with text_dissolve
    t_left "He was known for the Scrappie Murders." with text_dissolve

    show s_neutral at right
    with dict_emotion_change

    s_right "I heard about him! Apparently he murdered people who had Scrappie Baby dolls that he couldn't get. They were all the rage at the time." 
    
    show s_neutral at offscreenleft
    with dict_emotion_change
    

    t_left "Exactly, but there was one murder that the cops tried to keep under the wraps." with text_dissolve
    mc "Then how do you know about it?" with text_dissolve
 
    t_left "My pop's a cop and I'm a genius who knows how to unlock filing cabinets." with text_dissolve

    show j_annoyed at right
    with moveinright
    j_right "Careful Tanner... your ass is showing." with text_dissolve

    show j_annoyed at offscreenright
    with dict_emotion_change

    hide j_annoyed

    t_left "Anyways, let me begin..." with text_dissolve

    show my_movie:
        zoom 0.5
    with Fade(0.0, 0.0, 4.0)
    pause 98
    hide my_movie

    show j_neutral at right
    with moveinright

    j_right "Oh that sounds ridiculous. We would have known about it." with text_dissolve

    t_left "It was in my dad's files! Besides that, they did catch the guy eventually." with text_dissolve
    t_left "Locked him up and threw away the key." with text_dissolve

    show j_neutral at offscreenright
    show c_neutral at right
    with dict_emotion_change
    
    hide j_neutral

    c_right "Okay that was disgusting but he's all locked up so that's good!" with text_dissolve

    t_left "Was." with text_dissolve

    c_right "Come again?" with text_dissolve

    t_left "There was a huge riot and breakout at the county prison. Guess who escaped?" with text_dissolve

    mc "THE SCRAPPIE KILLER!" with text_dissolve

    show c_scared at right
    with dict_emotion_change
    hide c_neutral

    c_right "..." with text_dissolve
    c_right "I... I don't know if I want to go to the party anymore." with text_dissolve
    
    show c_scared at offscreenright
    show j_annoyed at right
    with dict_emotion_change

    j_right "Oh come on... He's just trying to scare you. It's a made up story." with text_dissolve
    t_left "Or is it?" with text_dissolve

    show j_annoyed at offscreenright
    show c_annoyed at right
    with dict_emotion_change

    c_right "Quit it Tanner! It's not funny..." with text_dissolve

    show c_neutral at right
    with dict_emotion_change

    hide c_annoyed
    c_right "What do you think [main_char]?" with text_dissolve

    menu:
        "The story could be real...":
            t_left "Hah! [main_char] agrees with me!" with text_dissolve
            show t_neutral at offscreenleft
            show s_neutral at left
            with dict_emotion_change
            hide t_neutral
            
            s_left "Wow, you really think it's possible?" with text_dissolve
            show c_scared at right
            with dict_emotion_change
            hide c_neutral

            c_right "Fuck! If [main_char] think it's true... it probably is!" with text_dissolve


            show s_neutral at offscreenleft
            show c_scared at offscreenright
            hide c_scared
            hide s_neutral
            show j_happy at right
            with dict_emotion_change

            j_right "Real or not, that story won't stop us from having a good time!" with text_dissolve
            j_right "Oh! We're here!" with text_dissolve

            jump scene4

        "Nah, no way this story is real":
            show t_annoyed at left
            with dict_emotion_change
            hide t_neutral

            t_left "Hey! I'm telling y'all the truth! This shit is real." with text_dissolve

            if main_char_pronoun_singular == "They":
                c_right "I agree with [main_char]. [main_char_pronoun_singular] are smart like that."
            else:
                c_right "I agree with [main_char]. [main_char_pronoun_singular] is smart like that."
            
            show t_annoyed at offscreenleft
            show c_neutral at offscreenright
            show s_neutral at left
            with dict_emotion_change
            hide t_annoyed
            hide c_neutral

            s_left "{b}HMPH{/b}... my story was scarier." with text_dissolve

            show j_happy at right
            with dict_emotion_change

            j_right "Real or not, that story won't stop us from having a good time!" with text_dissolve
            j_right "Oh! We're here!" with text_dissolve

            jump scene4



    #Queue Cutscene










    