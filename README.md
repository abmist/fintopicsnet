# Project 3 for Code Institute - Fintopicsnet
## Introduction

This project is a **social entrepreneurship network** that allows for the exchange of business ideas –*an online meeting point for entrepreneurs and funders*-. It has been built with [Python] (https://www.python.org/) using [Django] (https://www.djangoproject.com/) and a relational database. 

## Description
It was given to students a basic and plain skelenton of the project. The goal was using the elements learnt in the course (and any other which could add value) to get a full stack membership site with these components: 
* An account app
* A forum with a poll
* A blog
* A payment system
* A contact form   

## Useful comments on the structure and some of the main components added

*__Account model, register and authentication__*
* This project includes a **custom user model**.
* The email acts as username. 
* It contains **custom attributes** necessary to use Stripe (payment system) and there were also added other custom attributes to collect members' information. One of them is an optional **profile picture**.
* It is used **Stripe** payment system (for membership subscriptions). 
*Once registered and/or logged in*, the user accesses to the profile page which shows his/her basic account information and subscription details. You need to be registered and logged in to see most of the content.

*__Member list with a detailed view of each one__*
* Only members can access to this **list of members** and to a **page with detailed information of each one**.
* These details (like first name, last name, education, city, etc.) come from the register form. 
* The page with those details of each member is **linked to every post and blog-article they write and to every forum-thread they create**.  

*__Forum with polls__*
* Members can engage in discussion about different types of business topics within the membership community.
* There are several **subjects** (like finance, marketing, strategy, etc.). Only a superuser can create them. Non-members can see them but they can’t access to their content.
* Any member can create a **thread** in a subject.  
* Each thread, in turns, **contains a poll and posts**. Again, only members can *create, edit and delete* a post, and vote on the poll.
* The poll is created by the owner of the thread. And it will only record a vote per member.
* Threads and posts show their author. It's possible to access to their detailed information clicking on the link. 

*__About__*
* It explains useful information about the site and the company.
* It also includes **Google maps with markers** for showing where offices are located. 

*__Contact__*
* A **form** that allows any member and/or potential member **to ask any kind of question to the staff**. 

*__Blog__*
* This blog enables members to **share articles** where they can explain business ideas, experiences, etc.
* Any member can create an article and add a topic picture.
* Other members can contribute commenting those articles using Disqus system.
* Articles show their **author with a link to access to their detailed information**.

*__Training services list__* 
* There is a list of training services (workshops, etc.) where **users can purchase them by means of PayPal payment system**. 
* It also includes a link to another page (flatpage) which contains details about a summit (another project named Fintopics).  


## Style
The aim was to create a **totally responsive website which keeps a minimal and functional design** focused on information. For that purpose it has been used a clean, sober and subtle style - with very few decorative elements-, keeping simplicity at all times. 


**Gif home**:

![Home_in_motion](https://github.com/abmist/fintopicsnet/blob/master/static/images/README_screenshots/fintopicsnet_home_in_motion.gif)

**Some screenshots**:

Home:

![Home](https://github.com/abmist/fintopicsnet/blob/master/static/images/README_screenshots/project_3_home.jpg)

Login:

![Log_in](https://github.com/abmist/fintopicsnet/blob/master/static/images/README_screenshots/project_3_log_in.jpg)


Profile:

![Profile](https://github.com/abmist/fintopicsnet/blob/master/static/images/README_screenshots/project_3_profile.jpg)

Member list:

![Member_list](https://github.com/abmist/fintopicsnet/blob/master/static/images/README_screenshots/project_3_member_list.jpg)



Member detail info:

![Member_details](https://github.com/abmist/fintopicsnet/blob/master/static/images/README_screenshots/project_3_member_details.jpg)

Blog:

![Blog](https://github.com/abmist/fintopicsnet/blob/master/static/images/README_screenshots/project_3_blog.jpg)



Blog article:

![Blog_article](https://github.com/abmist/fintopicsnet/blob/master/static/images/README_screenshots/project_3_blog_article.jpg)


About:

![About](https://github.com/abmist/fintopicsnet/blob/master/static/images/README_screenshots/project_3_about.jpg)



Subjects (forum):

![Subjects](https://github.com/abmist/fintopicsnet/blob/master/static/images/README_screenshots/project_3_subjects.jpg)



Threads (forum/subject):

![Threads](https://github.com/abmist/fintopicsnet/blob/master/static/images/README_screenshots/project_3_forum_threads.jpg)



Thread (forum/subject/thread):

![Thread](https://github.com/abmist/fintopicsnet/blob/master/static/images/README_screenshots/project_3_forum_thread_and_posts.jpg)



Posts (forum/subject/thread):

![Posts](https://github.com/abmist/fintopicsnet/blob/master/static/images/README_screenshots/project_3_posts.jpg)



New thread (forum/subject/thread):

![New_threads](https://github.com/abmist/fintopicsnet/blob/master/static/images/README_screenshots/project_3_forum_new_thread.jpg)



## Technology stack
* Relational database: MySQL/SQLite
* [Django] (https://www.djangoproject.com/)
* [Angular.js] (https://angularjs.org/)
* [Bootstrap] (https://www.http://getbootstrap.com//)
* Python
* JavaScript
* jQuery
* HTML5
* CSS3


## Improvements for the next stage

This project is an exercise. It doesn't intend to be in a production stage. The goal was just to put into practice some of the concepts learnt in the course. If you were interested in continuing it, below you can find some improvements that could be added: 
* Message system between members.
* Make possible to update members' information.
* Make possible to sort/filter threads, members, etc.
* Display user name in the navbar.
* Improve UI/UX.
* Pagination.  
* Tooltips. 
* Summary of threads, posts, articles, etc. of a member.


## Instructions

Open your terminal and use the git clone command:

`git clone https://github.com/abmist/fintopicsnet.git`

Once the project is cloned, enter in fintopicsnet directory:

`cd fintopicsnet`

It's recommended to use a virtual environment (to keep isolated the dependencies required by this project). If you don't have it installed, you can do it using *pip*:

`pip install virtualenv`

Here you have the instructions: [Virtual Environment - The Hitchhiker's Guide to Python] (http://docs.python-guide.org/en/latest/dev/virtualenvs/)

Create a virtual environment for this project and activate it. 

Install the dependencies:

`pip install -r requirements.txt`

Set the database: 

`python manage.py migrate`

Run the project:

`python manage.py runserver`

Now you can open up your browser and in the URL bar enter `http://127.0.0.1:8000`

Create a superuser:

`python manage.py createsuperuser`

Access to admin panel to create subjects for the forum:

`http://127.0.0.1:8000/admin/`

If you want to test the register, use the following credit card data:

* Credit card number: *4242424242424242*
* CVV: *123*
* Expiration month: *9*
* Expiration year: *2033*

*Note*: In the event that you can't see the pages *Fintopics Summit* and *Terms and Conditions*, you'll need to configure the flat pages in the admin panel to run it locally:

* Go to *Sites* and add localhost as a site. 
* You'll have to enter "localhost" in *Domain name* and *Display name*. Then click on *Save*.
* Go to *Flat Pages*. 
* Click on "Add". Entering the following for the page *Fintopics Summit*: 
	* URL: */pages/summit/*
	* Title: *Summit*
	* Sites: *localhost*
	* Advance options (show) > Template name: *flatpages/summit.html*
	* Then click on *Save*.
* Click on "Add". Entering the following for the page *Terms and Conditions*: 
	* URL: */pages/terms/*
	* Title: *Legal*
	* Sites: *localhost*
	* Advance options (show) > Template name: *flatpages/legal.html*
	* Then click on *Save*.
* Go to *fintopicsnet/settings.py* and *settings/base.py* and change the `SITE_ID`. 
