Project structure:

 - `wsgi/` - web application root
   - `static` - all static content
     - `css/` - styles, including external
     - `img/` - images, including sprites and icons
     - `js/` - scripts, including external
     - `fonts/` - fonts in svg
   - `templates/` - html files
     - index.html - current site root


Site impressions
================

About
-----
* Nice color
* Need to think about more useful content (main page is main impression)
  * 2 Degrees
  * Full-time work experience


Career
------
* Nice color
* Make all logos readable


Education
---------
* Too acid color
* Add more info
* Stress on 2 Master degrees


Certificates
------------
* If decide to change this section completely, candidates:
  * References
  * Online profiles
  * Services
* Color looks great with IBM certificates

Hobby
-----
* Color is OK, but photos like gray/dark background
* Add more stories:
  * Photos
  * Technology (put stuff that makes geeks happy: Ubuntu, Git, Web, Telecoms)
  * Travel (Map? Locations? Favorite-list?)
  * Sport?
  * Maybe, "other": home design, books

Contact
-------
* Color is fantastic
* Maybe embed google-map
* Remove unnecessary styles, keep it simple

API notes
=========
* `contact` – send a message to my private email
  * URL: `/api/contact`
  * Method: `POST` 
  * Data: `{"email": "test@trash-mail.com", "name": "Testman", "text": "Hey there"}`

Backend
=======
Backend is running on:
- Flask web-framework
  - Python
  - Jinja2 templates
- uWSGI web server
- Openshift hosting


Openshift
=========
Openshift uses git-based commits, new version is deployed just after push.

Git authentication is done by sharing the ssh public key through web interface.
