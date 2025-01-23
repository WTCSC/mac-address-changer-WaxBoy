[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/tp86o73G)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17754591)



## What is a MAC address? 
 - **MAC address** stands for ***M**edia **A**ccess **C**ontrol Address*
 - One is uniquely assigned to each NIC (Network Interface Card) at production.
 - It holds six 8-bit numbers (*base 16 number pairs*), formatted like so: 

    *`02:46:8A:CE:15:F9`* (Case insensitive)
 - They are neccessary for communication on the local network.
---
### There are limitations, however. 

When spoofing a MAC address, the first 8-bit number (**00**:00:00:00:00:00) is highly regulated.

To keep safe, it may not end in:
* An odd number (ending in 1,3,5,7,9,B,D, or F)
* Either a 0 or an 8 (58, F0, A8, 10, etc.)

## Usage

1. First use `ip link show` in the command line to see the Network Interfaces detectable by your system.

2. Once you have determined which Interface you are currently connected to, you can move to the bash terminal.

3. You can run the function using `./mac.h 'Interface' 'NewMacAddress'`, the new Mac address being whatever you want to spoof it to.

4. If you replace your 'NewMacAddress' input with `default`, your MAC address will be set back to factory default.

5. **Similary**, you can use `random` to generate a random MAC address, which you can choose to use or not. The first digits will always be `02` in order to comply with limitations.

## System Feedback



An ERROR will occur when:

1. Inputting an **interface** that is **not detected** on your local newtork.

2. Trying to use the **`default` function** while the MAC address is **already factory default**.

3. Inputting a **MAC address** that **does not follow standard format**: *`XX:XX:XX:XX:XX:XX`* (case insensitive)

4. Using the **`random` function**, but **not correctly confirming** with either Y or YES (case insensitive)

### Address Record:
When switching to a **New MAC Address**, the **Initial MAC Address**, is automatically recorded along with its **Interface** in the *`./history.txt`*  file.

### Final:
If a command follows through completely, you should see your selected *Interface*, the *Initial Address*, and a *Success!* message showing your *New Address*

---

Happy spoofing!