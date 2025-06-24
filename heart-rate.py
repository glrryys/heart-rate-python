age = int(input("Enter your age: ")) # asking user for their age, int is helping the 
# the input be a number instead of text

MHR = 220 - age # processing MHR by subtracting 
moderate_low = 0.5 * MHR # processing mod low by multiplying  
moderate_high = 0.7 * MHR # processing mod high by multiplying  
intense_low = 0.7 * MHR # processing int low by multiplying  
intense_high = 0.85 * MHR # processing int high by multiplying  

print("Max Heart Rate:", MHR, "BPM") # spelling it out togtther (the commas used for separation)
print(f"Moderate Target: {moderate_low:.1f}-{moderate_high:.1f} BPM") # f is used for a string, it replaces it with the stated variables
# without it it would just print what we said
# .1f rounds the numbers 
print(f"Intense Target: {intense_low:.1f}-{intense_high:.1f} BPM") ## same here
