# <p align="center">GlobalexamBot</p>
  
Bot for the website Globalexam. It helps to spend more than 20 hours on it by reading sheets.

## 🛠️ Install Dependencies    
```bash
python -m pip install -r requirements.txt
```
You also need to install google chrome v104.x, if you want to use the provided chromedriver.  
The provided chromedriver works only on a Linux system.   
You can replace it by another one by downloading it here : [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)
## 🧑🏻‍💻 Usage

```bash
python main.py -u <username> <password>
```
Without headless mode :
```bash
python main.py -u <username> <password> --noheadless
```
Run with docker :
```bash
docker build -t globalbot .
docker run --shm-size=1g -it globalbot -p <password> -u <test>
```
