from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#   '/blog?limit=10&published=true'        #we want handle parameters into the query
@app.get("/blog")                          # parameters are handle with funtion parameter
def index(limit: Optional[int] = 10, published:bool = True, sort: Optional[str] = None):
    if published:
        return {'data': 
                    f'{limit} published blogs from the db'
        }
    else:
        return {'data': 
                    f'{limit} blogs from the db'
        }

@app.get('/blog/unpublished')
def unpublished():
    # fetch all unpublished blog
    return {'data': 'All unpublished blogs'}
    
@app.get('/blog/{id}')
def show(id: int):       #parameter form decorator need to be pass to the function
    # fetch blog with id = id
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id: int):
    # fetch comments of blog with id = id
    return {'data': {id, "my comments"}}

class Blog(BaseModel):            # this object will define a Type thanks to BaseModel from Pydantic
   title: str
   body: str
   published: Optional[bool]

@app.post('/blog')
def create_blog(request: Blog):    #object request received has a Blog type.
    return {'data': f'Post has been create with title : {request.title}'}
