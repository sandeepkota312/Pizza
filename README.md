This procedure is determined to only windows users. I would recommend to use pycharm to run this application.

1. Install Python 3.9.5 version - https://www.python.org/downloads/
2. Create a new project in your pycharm and open that project.
3. Clone this git repository to your system and place them in the project folder.
4. Open the terminal and then install the dependencies using command 'pip install -r requirements.txt'.
5. Then go to pizza/pizza directory and create a folder named 'migrations', similarly do the same in pizza/orders directory.
6. In the terminal go to pizza repository using the command 'cd pizza'.
7. Then type the following commands in sequence as follows:
      1. python manage.py makemigrations
      2. python manage.py migrate
      3. python manage.py createsuperuser - Then add a username, email and password in the following steps as mentioned in the terminal
      4. python manage.py runserver 
             
