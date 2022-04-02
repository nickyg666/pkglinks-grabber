# pkglinks-grabber
python script to grab PKG links encoded in base64, decode them and parse out links to a text file

would like to build a simple tkinter gui to learn about FEs with py but also it's not very usable with tkinter ( ooooh but we'd have a button to click! Or maybe a button for each step to ruin user experience! ), a gui will probably just get in the way. plus tkinter looks janky I'm sure I could go bananas with it and I reserve the right to
this is my first actual python project "worth" sharing (the other was a simple custom filename cleaner), so my apologies that the first few editions are very inefficient code wise, I was only focused on using python for the task so when I learned a sloppy way I pushed along just to get the script running. Of course the latest edition,
#  *v1.1 out*
is a bit shorter lines wise, takes a cleaner and different approach (using .json extension on feed, using json module in script), and still parses all comment data correctly. It does appear to miss some b64 strings occasionally, but it will still print them to the file as an archival feature. (it's a feature, not a bug lol). I know it's not the best fake feature to deal with but hey it's something for now. You can always submit a PR if you're ready to teach me something neat!
pro-tip: if you would like silent output, you can comment out: 
  print(title)
  print(entry)
  print(link)
at the bottom of my for loop. I would advise against it though as you can just put it on your clipboard from the shell window, and not have to open the generated .txt. I still have to add in the bit where it won't just overwrite the whole file everytime you run it.

#  roadmap
#  immediate waiting to commit
two functions main() and next() to gui-ize and pull next links, next() has problem where it doesn't actually update (or at least maybe requests/json lines are not reading the right version of url variable). so I have to learn a bit more about global, nonlocal keywords and their functions as well as scope of functions before I can submit.
after I figure that out it should be able to go back all the way, but will probably limit to 1000 entries.
# depends (trying to use popular/built-ins)
feedparser (first two uploads only), json, base64, re, requests
