Creating a virtual environment (venv) is a good practice on both macOS and Windows. The purpose of a virtual environment is to isolate project dependencies, ensuring that each project has its own set of packages and versions, which helps avoid conflicts between projects.

Here are some key reasons for using a virtual environment:

Isolation: Keeps dependencies for different projects separate, preventing version conflicts.
Reproducibility: Makes it easier to recreate the project environment on another machine by using a requirements file (e.g., requirements.txt).
Control: Allows you to manage package versions more effectively, ensuring your project runs with the versions it was developed with.

To create a virtual environment on macOS, you can use the following command in your terminal:
--> python3 -m venv myenv
Replace myenv with the name you want for your environment. To activate it, run:
--> source myenv/bin/activate
Once activated, you can install packages using pip, and they will only be available in that environment. When you're done, you can deactivate it by simply running:
--> deactivate
Using virtual environments helps keep your development process clean and organized!


INSTALLING FASTAPI  
pip install "fastapi[standard]"
pip freeze --> it helps us see all the installed dependencies.


fastapi dev main.py || uvicorn main:app --> this is to run the app with uvicorn server.


Docker compose postgres and php myadmin
 //https://www.youtube.com/watch?v=qECVC6t_2mU

 Find ip 
 docker container ls - LIST ALL CONTAINER
 docker inspect <CONTAINER ID> - FIND THE DETAILS ABOUT THAT CONTAINER