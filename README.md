Problem scenario:

As asmr enjoyers and big content consumers ourselfs, we came across a challenge that didn't quite have a solution yet,
let's imagine you are not being able to fall asleep and fancy some asmr to help you with it, but at the same time you would 
like to be hearing about a certain topic, or podcast or just any video in general. Well our objective with this project
is to make that possible, you just insert the yt link for the video you want to transform to a more relaxing and asmr like
content, and with the help of the ai models we used, make it happen.




The background process:

1- Download the video using the pytubefix

2- Convert it to .wav using moviepy

3- Extract the text using the whisper ai model

4- Convert from text to speech using elevenlabsSe ai model

5- Add asmr like affects (tapping) and ambience background sound (rain) with pydub

6- Merge video with new audio 

7- Send the masterpiece to the user





Ai models used:

whisper (from open-ai, speech to text)
elevenlabs (text to speech)





Future implementations we would like to add:

 -Give user the option to choose the type of asmr to add (tapping, scratching, ear eating, etc...)
 -Give user the option to choose ambience background sounds (rain, wind, lo-fi music, etc...)
 -Give user the option to choose the voice model
