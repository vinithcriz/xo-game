FROM python:3.10-slim

# Install dependencies for GUI (Tkinter and X11)
RUN apt-get update && apt-get install -y python3-tk x11-apps && apt-get clean

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# GUI display setup
ENV DISPLAY=:0

CMD ["python", "xo_game.py"]
