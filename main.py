from fastapi import FastAPI

app = FastAPI()

@app.get('/')        #add decocator from fastapi app objectg
def index():
    return 'heyy'