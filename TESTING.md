Many of the podcast providers don't provide easy downloading on their episodes.
Some require the user to navigate through their website, pressing buttons and whatnot.
Some don't even offer downloading at all, only streaming their content in real-time.
In order to circumvent these restrictions, the scripts in this project rely on certain assumptions on how the podcast audio is accessible.
For instance, one podcast might only be accessed by navigating to an episode's webpage and press the play button.
This would open a window, which would load a flash player, which would then begin streaming the audio.
In order to acquire the audio and store it persistently, the code in this project relies on this progression of steps to remain unchanged.
If, for example, the podcast were to change its website appearance, the code that downloads that podcast's audio might break when it is next executed.
This can't be prevented, but what can be done is to probe the podcast's website to verify that it has not been changed so as to cause this application to break.

More info will be outlined on how these tests are structured and executed.
