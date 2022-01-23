from fastapi import FastAPI, Depends, status, HTTPException
from . import schemas, models
from .database import SessionLocal, engine
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.post("/blog", status_code= status.HTTP_201_CREATED)
def create(blog: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title= blog.title, body= blog.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get("/blog")
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get("/blog/{id}", status_code= status.HTTP_200_OK)
def show(id, db: Session = Depends(get_db)):
    blog =  db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail=      f"Blog with the id {id} is not available")
    return blog

@app.delete("/blog/{id}", status_code= status.HTTP_200_OK)
def delete(id, db: Session = Depends(get_db)):
    db.query(models.Blog).filter(
        models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return { "data": f"blog {id} has been deleted" }

@app.put("/blog/{id}", status_code= status.HTTP_202_ACCEPTED)
def update(id, blog: schemas.Blog, db: Session = Depends(get_db)):
    updated_blog = {"title": blog.title, "body": blog.body}  # turn around : I can' understand why blog does not work in update
    db.query(models.Blog).filter(models.Blog.id == id).update(updated_blog, synchronize_session=False)
    db.commit()
    return blog




