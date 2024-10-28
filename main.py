from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
import psycopg
from pydantic import BaseModel
from typing import Optional
from random import randrange
from psycopg.rows import dict_row



app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    

    
def connect_to_db():
    try:
        # Connect to the existing database
        conn = psycopg.connect(
            host='localhost',
            dbname='fastapi',  # Change 'database' to 'dbname'
            user="postgres",
            password="Abinash@2413",
            row_factory=dict_row
        )
        print("Connecting to database Successful`")
        cursor = conn.cursor()
        
        return conn, cursor
    except Exception as e:
        print(f"An error occurred while connecting to the database: {e}")
        print("Connecting to database failed")

# Establish the database connection
db_connection, cursor = connect_to_db()
        
    

        
    
my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {
"title": "favorite foods", "content": "I like pizza", "id": 2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p
        
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

@app.get("/")
def get_helloWorld(): # function doesnot have to be root.
    return {"message": "Hello World"}

@app.get("/welcome")
def get_welcomeMessage():
    return {"message": "welcome to my API page"}

@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts""")
    my_posts=cursor.fetchall()
    db_connection.commit()
    return {"data": my_posts}

@app.post("/createposts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """, (post.title, post.content, post.published))
    post_dict = cursor.fetchone()
    return {"data": post_dict}

@app.get('/posts/{id}')
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'message': f"post with id: {id} was not found"}
    return {"post_details": post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} doesnot exist")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put('/posts/{id}')
def update_post(id: int, post: Post):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {"data": post_dict}