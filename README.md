# Animal Farm - Code Institute Milestone Project 4

## Animal Farm - Domesticated Animals Database
The inspiration for this project came from living on a farm. The overall concept of the website was to have a place where people can go to to see simple information about different animals, with a focus being animals that have been domesticated. 

The benefit of this is that a user can come to the website, find out what animals are out there that they can own, and also see their needs, for example where they need to live and what they need to eat. This is helpful, because the information for a variety of animals is in one place, and the user doesn’t need to search lots of different places on the web. 

Another advantage is that the website can be constantly updated, so the users can combine their knowledge to constantly update and improve the quality of the information.
### UX
Wireframes can be found [here]()

This website is built mainly for people who are involved in or are interested in farming or owning a domesticated animal as a pet. The website intends to inform a user of simple information about domesticated animals, to give them some knowledge of what is required to take care of the animal, such as where it should live and what it should eat.

It is a community space, where users with more experience and knowledge of these animals can update and improve the information for a better overall user experience. The ability to add animals gives users with rare breeds or species of animals the chance to share little known information about them, to inform the wider community.


As a farming enthusiast, I want to:
-   Visit a website to find out more information about animals
-   Contribute my own knowledge about certain animals that I have acquired over years of farming experience.
-   Delete or update information that I believe another user has added that is incorrect or misleading

###  User Story
-   I am looking into going into the farming industry, and would like to farm animals, so I am looking for a website to give me a simple understanding of which animals I can farm, and what they require.
    1. Upon loading the website, I don’t want it to be complicated to find this information
    2. I see on the homepage some cards, which have images of the animals, their names and basic information about where they need to live and what their diet should include.

-   I am someone who has just discovered some exciting new information about a Horse’s diet, and want to be able to share it.
    1. When on the website, I want to see an obvious place to edit information
    2. I see there’s a button on the Horse’s card that has a pencil icon, which I can tell symbolises the ability to edit the information.
    3. I click on it, and I am taken to a page with a form to edit the current information.
    4. I can then submit it via a button, and the information will be updated on the database and rendered on the website

-   I have just discovered a new animal that can be domesticated and want the ability to share this information with others who may be interested.
    1. When on the website, I want to see an obvious place to add information.
    2. Immediately I see in the header that there is a button to ‘Add Animal’.
    3. I follow this link to a page with a form, where I can submit my data
    4. I can then post it to the database via another ‘Add Animal’ button, and then be redirected back to the homepage where I can see my data rendered.


### Animal Farm - UX Brief
#### Strategy:

-   I am aiming to produce a simple and intuitive site for my users to navigate and create, read, update and delete information

-   It will be responsive to all devices and browsers


#### Scope:

-   It will showcase:
    1. Individual cards to present information about domesticated animals
-   Users will be able to:
    1. Read information about domesticated animals
    2. Create their own cards to add new animals to the database.
    3. Edit and update information of pre-existing animals
    4. Delete cards for animals if they think they are inaccurate or don’t belong with this particular dataset.


#### Structure / Skeleton:

The website will include 3 pages:
-   Home
    1. Showcasing the cards with the animals info
    2. Very simple layout. On desktop: 2x2 cards. Mobile: Single column
- Add Animal
    1. Form to add information about a new animals to the database
    2. Ability to upload a picture of that animal
- Edit Animal
    1. Form to update the pre-existing information about an animal. The fields will be pre-populated with the pre-existing information.

The website will have the same header on every page, but no footer, as I don’t believe it is necessary for this project. 

Header will include:
-   Website name/logo
-   Menu with buttons to return a user to the homepage and to add an animal.
On a mobile this will be hidden in a responsive burger menu from Materialise


#### Surface:
Color Scheme:
The colour scheme is based on the green of a grassy field, to give it that farm feel.

Font Family:
‘Ubuntu’ (Google Fonts)


Images will be photos that users link to from external resources, such as Google images.

#### Features

#### Existing Features
-   The Header - allows the users to navigate the website by having clear links to the other pages within the website. 

-   The homepage shows all the animals on the website.

-   Add Animal page - This allows a user to add their own information about an animal that isn’t yet on the website in the database.

-   Edit Animal page - This allows a user to update and add any information about animals that they think is incorrect or missing.
Delete button - This gives a user the power to delete animals from the database that they don’t believe belong there.

#### Features Left to Implement
-   Ideally, I would create user authentication, so that only registered users can update, add or delete information.

-   Links to places to purchase these animals, or for suppliers of food and other equipment needed for raising these animals.

-   A newsletter would be helpful for those who want to be notified when information on the website is updated.
#### Technologies Used

**HTML5**

-   I used HTML5, as it is the base of every website.

**CSS**

-   I used CSS to style my HTML code, to create a global design scheme, and make the website visually appealing for users.

**JavaScript**

-   A minimal amount of JavaScript was used in combinatio with the Materialize classes.

**[Flask](https://flask.palletsprojects.com/en/1.1.x/)**
-   I used Flask as the framework to build my project.

**[Materialize](https://materializecss.com/)**
-   I used Materialize to create the cards to display my information, for my responsive navigation and grid layout.

**[Material Icons](https://material.io/resources/icons/?style=baseline)**

### Testing

-   Home (Animals listing page):
    1.  I loaded the website homepage.
    2.  Checked that the buttons on the cards took me to the pages they were supposed to:
        1. Edit button successfully took me to the edit page of the card I clicked on.
        2. Delete button then successfully deleted only that one card.

    When taken to the ‘Edit Animal’ page after clicking on the edit button on the card, the information that was already in the database for that animal was pre-populated In the form, and I was able to replace only the data that I wanted, and successfully update it on the database. I tried changing every field, and all data rendered as I hoped

-   Add Animal Button
    1. I clicked on the ‘Add Animal’ button that is in the header.
        1. This successfully took me to a form where I was able to add a new animal to the database, and I was returned to the homepage as expected, where I could then see my data rendered as a card.

        An interesting bug that the website has, but only on Google Chrome is that the first time a user clicks on the dropdown select for ‘Animal Group’ the list flashes up and then disappears. It shows correctly after a second click though. I haven’t been able to understand where the root of the problem is.

I used some code validators to check my code:

[This HTML Validator](https://www.freeformatter.com/html-validator.html) Showed that the only errors were once where it couldn’t interpret Python, so I am confident that the HTML around it is valid.

[This CSS Validator](https://jigsaw.w3.org/css-validator/) Shows warnings, but only from the CSS in external libraries, such as Materialize.
[Responsinator](https://www.responsinator.com/) to check the site’s responsiveness. No issues detected.
### Responsiveness
Whilst developing the site I consistently used the chrome inspector tool to tested different screen sizes, to see how the cards would respond. Sometimes, when the animal information got too long, the cards would resize and the grid system was often very inconsistent. To fix this I attempted to use Bootstrap’s grid system, but this clashed with the other Materialize elements that I had on the site. In the end my way around this was to set a maxlength for text input. This way there cannot be any unexpected shifts in the card size. Following on from this, cards correctly transition from 2x2 on desktop to single column at the anticipated breakpoint when the screen size decreases.

The Materialize hamburger menu works as anticipated on mobile devices. Initially I had trouble with this, as when I set my desktop nav to ‘fixed’ positioning, it was rendering on top of the mobile menu and the items in my mobile menu were unaccessible. To fix this I changed the mobile menu’s Z-Index, and my problems were solved.

For the photos within the cards, I have added media queries at several breakpoints to keep them all a uniform size. I chose not to go for the background-image option and setting them the same dimensions that way because it left the cards having whitespace, and from a design perspective I think they look better this way.


**All tests were done individually on Firefox, Chrome, Safari on Mac and iOS, and returned the same results. I have been unable to test Edge and Internet Explorer, or any browsers on PC.**
### Deployment
I have deployed this site to Heroku, and you can find it deployed [here](https://pet-list-db.herokuapp.com/)

For more details on how to deploy a site to Heroku see this [video](https://www.youtube.com/watch?time_continue=4&v=XQcdS9mx97E&feature=emb_title)

Credits

Content
The information about each animal is currently my own, but the pictures have come from Google Images.

Media
The images for my site have come from links to images found on Google Images. I do not own the rights to any of them. No images are stored on the website, and are hosted solely from the location of the link.
