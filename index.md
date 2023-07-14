# Smart Glasses
This project is a compact wearable computer, in the form of glasses. It will have a few simple functions such as displaying time, date, or documents, and voice commands using text recognition. It will utilize a Raspberry Pi 0 W for the "brains" of the glasses, since the model has built-in bluetooth and wifi capabilities. It will use a reflection from a .96 inch OLED screen to display information in front of the wearer's eyes. The Pi will control the other components and run all the required code, including the OLED screen, a discreet earpiece, and software function. 

| **Engineer** | **School** | **Area of Interest** | **Grade** |
|:--:|:--:|:--:|:--:|
| Jamie L | Archbishop Mitty | Programming, Mechanical/Electrical Engineering | Sophomore

<!---**Replace the BlueStamp logo below with an image of yourself and your completed project. Follow the guide [here](https://tomcam.github.io/least-github-pages/adding-images-github-pages-site.html) if you need help.**

![Headstone Image](logo.svg)--->
  
# Final Milestone
I programmed some basic functions into my glasses at my third milestone. These include a simple boot screen, time function with a clock diagram, and image/file display. Since I usually do not program in Python and therefore had to get introduced to a completely new language, it took me a little to learn the fundamental keywords and their respective syntaxes. Additionally, I had to use many different libraries and modules. I also set up SSH and VNC on my Raspberry Pi so that I could access its screen and terminal on the monitor of my laptop without having to use an external monitor and keyboard/mouse. Howver, the Wifi settings at the school seem to be made so that it blocks the signals, so unfortunately it did not work. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/8OlgK4KyGKg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

# Second Milestone
By the end of the second milestone, I had finished all hardware design and assembly, and enabled the headless setup on my Raspberry Pi. With Onshape, I made the componenets that would attatch the Raspberry Pi, OLED screen, and reflector to an arm that would extend out of the glasses. For the arm, I had to go through three iterations due to faulty printing as well as some design issues, such as durability and arm length. I then assembled the printed parts and adjusted the angle of the reflector so that the user could properly see the image. My next goal would be to program the glasses for its functions.

<iframe width="560" height="315" src="https://www.youtube.com/embed/AWz9-APTujE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

# First Milestone

<iframe width="560" height="315" src="https://www.youtube.com/embed/QWJzpe3_Zj4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

For my first milestone, I set up a desktop environment on my Raspberry Pi, and soldered all of my componenets and ensured that they work properly. I had a lot of trouble with the initial transparent screen that I was using for the display, and I eventually had to switch to an alternative design, which used a smaller screen and its reflection to show the user information. I also had to transition from a SPI connection to I2C. In my future milestones, I will CAD and 3D-print a casing for the Pi to rest in next to the glasses, then get started with the code. I have only basic skills on CAD and programming, so those would be my next main challenges.

# Starter Project

<iframe width="560" height="315" src="https://www.youtube.com/embed/zXdnlKfFbyw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Links: <a href = "https://www.makershed.com/products/the-useless-machine-kit-soldering"> Product page, </a> <a href = "http://www.spikenzielabs.com/Downloadables/uselessmachine/Useless-Machine-Soldering-Edition.pdf"> Instructions </a> <br>
I chose the 006 Useless Box as my starter project since it involved multiple aspects of engineering; it required soldering, motor control, and physical assembly. A useless box is, as demonstrated above, a device that turns itself off when activated. When the lever on the box is flipped, the servo with an arm attatched is powered, coming up to the top of the box and flipping the lever so that the servo turns the other way instead. When it goes back to its original position inside the box, it hits a switch that turns itself off. 

<!--# Schematics 
Here's where you'll put images of your schematics. [Tinkercad](https://www.tinkercad.com/blog/official-guide-to-tinkercad-circuits) and [Fritzing](https://fritzing.org/learning/) are both great resoruces to create professional schematic diagrams, though BSE recommends Tinkercad becuase it can be done easily and for free in the browser. 

# Code
Here's where you'll put your code. The syntax below places it into a block of code. Follow the guide [here]([url](https://www.markdownguide.org/extended-syntax/)) to learn how to customize it to your project needs. -->

<!---```python
print("Hello World!")
```--->

# Bill of Materials

| **Part** | **Note** | **Price** | **Link** |
|:--:|:--:|:--:|:--:|
| Raspberry Pi Zero W | Brains of the glasses | $15.00 | <a href="https://www.pishop.us/product/raspberry-pi-zero-w/"> Link </a> |
|:--:|:--:|:--:|:--:|
| Bluetooth Earbuds | Audio information | $11.99 | <a href="https://www.amazon.com/BEBEN-Wireless-Bluetooth-Headphones-Waterproof/dp/B09SFZ7JZ8/"> Link </a> |
|:--:|:--:|:--:|:--:|
| .96in OLED Display | Visual information | $7.29 | <a href="https://www.amazon.com/HiLetgo-Serial-128X64-Display-Color/dp/B06XRCQZRX/ref=asc_df_B06XRBTBTB/?tag=&linkCode=df0&hvadid=312232463708&hvpos=&hvnetw=g&hvrand=18168632221262009846&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9032171&hvtargid=pla-563271619351&ref=&adgrpid=57656765450&th=1"> Link </a> |
|:--:|:--:|:--:|:--:|
| Battery Bank | Power Source | $17.99 | <a href="https://www.amazon.com/Anker-PowerCore-Ultra-Compact-High-Speed-Technology/dp/B01CU1EC6Y"> Link </a> |
|:--:|:--:|:--:|:--:|
| Power Supply Cable | RasPi Power | $9.95 | <a href="https://www.amazon.com/CanaKit-Raspberry-Supply-Adapter-Listed/dp/B00MARDJZ4"> Link </a> |
|:--:|:--:|:--:|:--:|
| HDMI Cable (Mini to Full) | RasPi to monitor | $8.79 | <a href="https://www.amazon.com/AmazonBasics-High-Speed-Mini-HDMI-Adapter-Cable/dp/B014I8UEGY/"> Link </a> |
|:--:|:--:|:--:|:--:|
| Micro SD Card | RasPi OS | $5.60 | <a href="hhttps://www.amazon.com/Center-Memory-Adapter-Mobile-Storage/dp/B09MC3MKYS"> Link </a> |
|:--:|:--:|:--:|:--:|
| Keyboard and Mouse | Navigate RasPi on desktop | $15.19 | <a href="https://www.amazon.com/Rii-Ultra-slim-Wireless-Multimedia-Raspberry/dp/B07BF3LFN3"> Link </a> |
|:--:|:--:|:--:|:--:|
| Non-prescription Glasses | Base of project | $10.99 | <a href="https://www.amazon.com/GQUEEN-201512-Fashion-Rectangular-Glasses/dp/B00ZRD1MEI/"> Link </a> |

# Documents Referenced

<a href = "https://www.instructables.com/Smart-Glasses-V2/"> Initial Idea, </a> <a href = "https://www.raspberrypi-spy.co.uk/2018/04/i2c-oled-display-module-with-raspberry-pi/"> Screen Configuration, </a> <a href = "https://www.hackster.io/petewarden/recognizing-speech-with-a-raspberry-pi-50b0e6"> Speech Recognition Library </a>

<!---# Other Resources/Examples
One of the best parts about Github is that you can view how other people set up their own work. Here are some past BSE portfolios that are awesome examples. You can view how they set up their portfolio, and you can view their index.md files to understand how they implemented different portfolio components.
- [Example 1](https://trashytuber.github.io/YimingJiaBlueStamp/)
- [Example 2](https://sviatil0.github.io/Sviatoslav_BSE/)
- [Example 3](https://arneshkumar.github.io/arneshbluestamp/)

To watch the BSE tutorial on how to create a portfolio, click here.--->
