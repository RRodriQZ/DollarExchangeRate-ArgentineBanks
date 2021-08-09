# Dollar-Values-of-Banks #

Web Scraping dollar values of Argentine Banks

* **Banco Nacion**
* **Banco Ciudad**
* **Banco Provincia**
* **Banco Santander Rio**
* **Banco Galicia**
* **BBVA Banco Frances**
* **Banco Comafi**
* **Banco Patagonia**
* **Banco ICBC**
* **Banco Supervielle**
* **Banco Hipotecario**

# Pre Requirements 📋

* **Python 3**-**Pipenv** / **Docker**

# Setup Python Virtual Environment 🔧 #
```cmd
pip install pipenv
```
**Windows** CMD:
```cmd
python -m venv venv
.\venv\Scripts\activate
pip install -e .
```
**Linux / MAC** command:
```cmd
python -m venv venv
source venv/bin/activate
python -m pip install -e .
```
# Running Python Script 🐼 #
```cmd
python main.py
```
**Unittest:**
```cmd
python test.py -v
```
# Running Docker 🐳
```cmd
docker build -t dollar_exchange .
docker run -it dollar_exchange
```
# Author 🖋

* Rodrigo Quispe - Developer - [RRodriQZ]
 
[RRodriQZ]: https://github.com/RRodriQZ