import re
str = """"
facebook
twitter
instagram
pinterest
tiktok
youtube
linkedin
Logo
Home
About Us
Programs
Life at Sunway College
Student Clubs
Career & Placements
Admission
about image
icon
Welcome To Sunway College.
Why Sunway College? Sunway College is one of the best IT College in Nepal. Since its establishment in the year 2010, we have been providing academic excellence to produce highly skilled human resources. We are an IT College in Nepal dedicated to mint academic and professional standards in our students...

Our Bachelor Degrees And Programs

BA (Hons) Marketing with Digital Communication
arrow

BSc (Hons) Computer and Data Science
arrow

Apply for November Intake

Apply for Scholarship
Upskilling For Starters
Upskilling is a Value Added Program for Sunway Students
Upskilling Images
icon
Upskilling Images
News And Events























About Birmingham City University.
University Ranking
UK	World	 	 
#64	#83	The Good University Guide	The Times - September 2021
#52	#67	The Guardian The Best UK Universities - League Table	- September 2021
#74	#89	CUG The Complete University Guide - UK	- June 2022
#48	#501	The World University Rankings - Times Higher Education	- September 2021
#65	#1001	QS World University Rankings	- June 2022
#86	#521	Scimago Institutions Rankings Universities	- April 2021
#65	#1730	URAP World Ranking - University Ranking by Academic Performance	-December 2021
#65	#1730	StuDocu World University Ranking EMEA - Europe, the Middle East and Africa	- September 2021
#74	#1262	Webometrics Ranking Web of Universities	- January 2022
#68	#859	The China Subject Ratings Overall	- May 2022
birmingham-img
Image Gallery
Student Testimonials










Videos & Podcasts









Our Alliances
Subscribe To Our Newsletter.
Full Name
Email Address
Logo
Sunway College Kathmandu offers experience-oriented international Bachelor's degrees in Digital Marketing and Data Science.

Reach Out
pinBehind Maitidevi Temple, Maitidevi, Kathmandu
pininfo@sunway.edu.np
pin01-4423736
01-4431725 , 9823047066
pinadmission@sunway.edu.np
Quick Links
Blogs
Events
Sunway News
Admission
Life at Sunway College
Apply For Workshop
Contact
© 2023 Sunway College Kathmandu | All Right Reserved

Website designed & developed with # by Theme Nepal

arrow
Message us
"""
email = re.findall(r"[a-zA-Z0-9_.-]+@[a-zA-Z0-9_.-]+\.[a-zA-Z0-9_.-]+",str)
print(email)