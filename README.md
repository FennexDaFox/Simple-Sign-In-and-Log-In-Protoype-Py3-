# Simple Sign-In and Log-In Prototype (Py3)

Greetings! Welcome to my very first project on my Python journey!

I've been learning [Python3](https://www.python.org/downloads/release/python-3123/) for just 3 days now, and honestly, it has been a really fun ride so far. This isn't my first time dealing with code, though. Before this, I spent some time messing around with scripts in **Lua and Luau** (mainly in Roblox Studio). While I am definitely not a pro scripter, that experience gave me a solid grasp of basic programming logic.

Because of that, switching over to Python wasn't a total nightmare—especially since it's known as one of the easiest programming languages to learn. Right now, my main focus is getting used to the new syntax, learning how Python handles data, and building small projects like this to test my limits. We all start somewhere, right? :)

# So What It Can Do?
- **Temporary RAM Storage:** Saves usernames and passwords in the RAM. No heavy databases here, so everything resets once you close the program.
- **Fast Login Validation:** Utilizes Python's built-in dictionary methods to instantly cross-check credentials.
- **Admin Control Gate:** Features a restricted Admin Menu that requires a specific hardcoded username and password to view the registered users list.

# How It Works?
Since I'm only 3 days into Python, I'm not an expert yet and haven't dived into building a fancy Graphical User Interface (GUI). Instead, I kept it text-based and interactive! Here is how the logic flows:

- **The Core Loop:** The system boots up using a `while True` loop to keep a clean, text-based menu running continuously in the background.
- **Handling User Input:** I used Python's built-in `input()` function to actively capture everything you type, whether you are selecting a menu option, registering a name, or entering a password.
- **In-Memory Storage:** When logging in, the system collects your login attempts and instantly compares them against the dictionary's keys and values to grant or deny access.
  
# What's Next?
Right now, everything wipes out when you close the script. I am currently learning how to connect Python 3 with JSON files so I can actually save this data permanently! Maybe my next project post will feature a JSON database? Or even crazier... Hashing! One of the most important things you can't miss when doing something like this is security! But who knows!

That's all from me! Thanks for dropping by and checking out my code. Any suggestions and feedback will be really appreciated!
