FROM python:3.11-slim

RUN apt-get update && apt-get install -yq wget

# download and install the specific version of Chromium
RUN wget --no-verbose -O /tmp/chrome.deb http://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_104.0.5112.79-1_amd64.deb 
RUN apt-get install -yf /tmp/chrome.deb

# set display port to avoid crash
ENV DISPLAY=:99

# copy the script
COPY . /app/

# set the working directory
WORKDIR /app

# install selenium
RUN pip install -r requirements.txt

# run the script
ENTRYPOINT ["python", "main.py"]