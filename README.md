# Project 3 for Code Institute - Fintopicsnet
## Introduction

This project is a **social entrepreneurship network** that allows for the exchange of business ideas –*an online meeting point for entrepreneurs and funders*-. It has been built with [Python] (https://www.python.org/) using [Django] (https://www.djangoproject.com/) and a relational database. 

## Structure

It contains an **account management which deals with user registrations and authentication, and integrates two payment systems**: **Stripe** (for membership subscriptions) and **Paypal** (for training services acquisitions). 

*Once registered and/or logged in*, the user accesses to the profile page which shows his/her basic account information and subscription details. As from that moment, he/she can navigate though all content of the site. Below are the main parts:

**Forum with polls**
* Members can engage in discussion about different types of business topics within the membership community.
* There are several **subjects** (like finance, marketing, strategy, etc.). Only a superuser can create them. Non-members can see them but they can’t access to their content.
* **Each subject has several threads** that any member can create. 
* **Each thread**, in turns, **contains a poll and posts**. Again, only members can create, edit and delete a post, and vote on the poll.
* The poll is created by the owner of the thread. And it will only record a vote per member.
* Threads and posts show their author. **Members can access to their detailed information** clicking on the link. 

**Member list with a detailed view of each one**
* Only members can access to this list and detailed information.
* These details (like first name, last name, educations, city, etc.) come from the register form. 
* Optionally **a profile picture can be loaded**. 

**About**
* It explains useful information about the site and the company.
* It also includes Google maps for showing where offices are located. 

**Contact**
* A **form** that allows any member or potential member **to ask any kind of question to the staff**. 

**Blog for articles**
* This blog enables members to **share articles** where they can explain business ideas, experiences, etc.
* Any member can create an article and add a topic picture.
* Other members can **contribute commenting those articles using Disqus system**.
* Articles show their **author with a link to access to their detailed information**.

**Training services list** 
* There is a list of training services (seminars, workshops, etc.) where **users can purchase them by means of PayPal**. 
* It also includes a link to another page (flatpage) which contains details about a summit (another project named Fintopics).  
	 

## Style
The aim was to create a **totally responsive website which keeps a minimal and functional design** focused on information. For that purpose it has been used a clean, sober and subtle style - with very few decorative elements-, keeping simplicity at all times. 

## Main features
* Member functionalities: log in, log out, member list, member detailed info, etc.
* User registration
* Custom user 
* Email authentication
* Stripe payment system for subscriptions
* Paypal payment system for single purchases
* Forum 
* Poll
* Forms: registration, contact, posts, etc.
* Blog
* Disqus for blog comments
* Google maps
* Contact
* Flatpages

## Technology stack
* Non relational database: MySQL/SQLite
* [Django] (https://www.djangoproject.com/)
* [Angular.js] (https://angularjs.org/)
* [Bootstrap] (https://www.http://getbootstrap.com//)
* Python
* JavaScript
* jQuery
* HTML5
* CSS3
