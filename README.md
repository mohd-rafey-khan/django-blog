# django-blog
Project Setup:

  We’ll assume you have Django installed already. You can tell Django is installed and which version by running the following command in a shell prompt (indicated by the $ prefix):
  
  $ python -m django --version
  
  if Not Installed:
  
      Step 1 – Installing Python and Pip
      
      If you have launched a new server,
      Then we recommend to update the server with below command

   $ sudo apt-get update
   
      By default, Python 3 is installed on your, but if your system doesn’t have Python installed, 
      Execute the below commands to install it

   $ sudo apt-get install python3 
   
      To install pip,Use below command

   $ sudo apt-get install python3-pip
   
      To check the version

   $ pip3 -V
      
      Step 2 : Installing Django
      Django source code is available as Github repository. 
      You can also use pip to install Django on Ubuntu systems

   $ pip3 install Django
   
      After Django is installed,You can verify the version

   $ django-admin –version
  



Creating a project

      If this is your first time using Django, you’ll have to take care of some initial setup. 
      Namely, you’ll need to auto-generate some code that establishes a Django project– 
      a collection of settings for an instance of Django, 
      including database configuration, Django-specific options and application-specific settings.
      From the command line, cd into a directory where you’d like to store your code, 
      then run the following command:

  $ django-admin startproject mysite
  
  Otherwise you Should simply git project by using command:
   
    $ git clone https://github.com/mohd-rafey-khan/django-blog.git
    
  To Run:
    using cd go into the project folder where manage.py is present and then run
  
   $ python3 manage.py runserver
          
        it will provide link where site is displayed (localhost) 
   
It Look Like This:

![1](https://user-images.githubusercontent.com/63442338/113502499-443e8a80-954a-11eb-829f-114e33492bdd.png)

Feature:
    Search any word into searchbar it will display some information about it. 
    Such as search (ice cream)
    
 ![2](https://user-images.githubusercontent.com/63442338/113502579-ce86ee80-954a-11eb-845f-db5962a9c34e.png)

     Banner slider image Will also change in every search
    
