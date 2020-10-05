## happy path 1 (/var/folders/33/d47d12xx51ngkzv0f3fc0wbr0000gn/T/tmp1sy_q7nd/3782ca8e23394a2fbf11134652cdda68_conversation_tests.md)
* greet: hello there!
    - utter_greet
* mood_great: amazing   <!-- predicted: no: amazing -->
    - utter_happy   <!-- predicted: utter_regist_failed -->


## happy path 2 (/var/folders/33/d47d12xx51ngkzv0f3fc0wbr0000gn/T/tmp1sy_q7nd/3782ca8e23394a2fbf11134652cdda68_conversation_tests.md)
* greet: hello there!
    - utter_greet
* mood_great: amazing   <!-- predicted: no: amazing -->
    - utter_happy   <!-- predicted: utter_regist_failed -->
* goodbye: bye-bye!
    - utter_goodbye


## sad path 1 (/var/folders/33/d47d12xx51ngkzv0f3fc0wbr0000gn/T/tmp1sy_q7nd/3782ca8e23394a2fbf11134652cdda68_conversation_tests.md)
* greet: hello
    - utter_greet
* mood_unhappy: not good   <!-- predicted: no: not good -->
    - utter_cheer_up   <!-- predicted: utter_regist_failed -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* affirm: yes   <!-- predicted: yes: yes -->
    - utter_happy   <!-- predicted: utter_regist_success -->


## sad path 2 (/var/folders/33/d47d12xx51ngkzv0f3fc0wbr0000gn/T/tmp1sy_q7nd/3782ca8e23394a2fbf11134652cdda68_conversation_tests.md)
* greet: hello
    - utter_greet
* mood_unhappy: not good   <!-- predicted: no: not good -->
    - utter_cheer_up   <!-- predicted: utter_regist_failed -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: not really   <!-- predicted: no: not really -->
    - utter_goodbye   <!-- predicted: utter_regist_failed -->


## sad path 3 (/var/folders/33/d47d12xx51ngkzv0f3fc0wbr0000gn/T/tmp1sy_q7nd/3782ca8e23394a2fbf11134652cdda68_conversation_tests.md)
* greet: hi
    - utter_greet
* mood_unhappy: very terrible   <!-- predicted: goodbye: very terrible -->
    - utter_cheer_up   <!-- predicted: utter_goodbye -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: no   <!-- predicted: no: no -->
    - utter_goodbye   <!-- predicted: utter_regist_failed -->


## bot challenge (/var/folders/33/d47d12xx51ngkzv0f3fc0wbr0000gn/T/tmp1sy_q7nd/3782ca8e23394a2fbf11134652cdda68_conversation_tests.md)
* bot_challenge: are you a bot?   <!-- predicted: thanks: are you a bot? -->
    - utter_iamabot   <!-- predicted: utter_goodbye -->


