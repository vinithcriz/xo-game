XO-Game  which is a Tkinter GUI-based Python game. ✅


To allow Docker to access xserver:
 xhost +

To Run a Container:
 docker run -it --rm   -e DISPLAY=$DISPLAY   -v /tmp/.X11-unix:/tmp/.X11-unix   vinithcriz/xo-game:latest

To Exit:
 xhost -
