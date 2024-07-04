  
![Featured Image - Python Flask MongoDB REST API Server](https://user-images.githubusercontent.com/69466026/229530573-a7762815-af49-4c99-86e1-c46cb20ace00.jpg)
# Prerequisites  
1.  Create a MongoDB Atlas cluster.
2.  Create a database called users_db with a collection users  
3.  Add the following JSON objects which we will use as references in this project. These are sample records for users that we want to control from our database.
4.  Open your MongoDB Compass and connect to your MongoDB Atlas database and then insert the two JSON documents above.
   
![Featured Image](https://i.postimg.cc/SR7jqdtm/Screenshot-271.png)
  
# Steps on how to run  
1)  Clone the repository using the below command  
```
git clone https://github.com/Karti01kay/flask-API.git
```  
2) Change into the project directory
```
cd rest-api-server
```
3) Open the project in Visual Studio Code and then open a new terminal. Create a virtual environment using the below command
```
# Windows
py -m venv .venv
# Linux
python -m venv .venv
```
4) Activate the virtual environment
```
# Windows
.\.venv\Scripts\activate
# Linux
source .venv\bin\activate
```
5) Install the dependencies
```
pip install -r requirements.txt
```  
6) Rename the .env.local to .env
```
mv .env.local .env
```  
7) Replace the value of the .env file to your MongoDB Atlas  
```
MONGO_DB_CONN_STRING=mongodb+srv://<DB_USER_NAME>:<DB_PASSWORD>@<MONGO_DB_ATLAS_ENDPOINT>/users_db
```
8) Run the Flask server
```
flask run
```
9) Open your browser and type the following URL
```
http://localhost:5000
```
