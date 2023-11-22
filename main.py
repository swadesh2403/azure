from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def default():
	return{"success":True,"message":This the default page"}

@app.get("/home)
def home():
	return{"success":True,"message":"This is the home page"}