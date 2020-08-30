# [One-Stop-Stunt_Shop](https://stunt-lounge.herokuapp.com/)

One Stop Stunt Shop is a website that i've been thinking about creating since the begging of this course. The reason why I wanted to create this website was because there are not so many stunt stores out there currently, and the few that are out there are starting to look old, are complicated and not user friendly. This site is for people who are looking to buy stunt parts for their motorbikes that are not always in the market. The goal of this website is to be able to cater to those who are looking to start stunting and don't know what parts their bike needs. Therefore this site is able to grow what we sell along with growing in size, based on information. With this website you can create a user to save your shipping information and you can place full payments in the database and use’s Stripe to do card payments for the products you would like to use.


 
## UX

My main goal was to create a simple website to allow users to view and buy products for their stunt bikes easily. The UX of this website is straight forward with big clear buttons that drag the users eyes towards to make payments along with pop up toasts. With this is started to think about what is the main thing that a user will use on a website and that is a navbar. With this I started to create a simple to use navbar from bootstrap and then I started to color connect it with the website tone that i was going for. This ended up being a nice red, white and black vibe that went well with the home image. The user is guided in a clean path to the store from the home page with a “Shop Now” button. Along with the shop now button on the home page there is also a “Products” button on the navbar to help lead the user to the “main goal” which is the shop. The next part of the user interface was to simplify the shopping process and with the help of the boutique_ado lessons we followed I was able to create this website. The admin of the site also has the ability to do CRUD in the management section on the Accounts page. 

- As a user, i want to View all products , so i can See what i want to purchase.

- As a user, I want to View product details, so that I can see products info, price, options and models.

- As a user, i want to be able to Swap between shopping and page info, Click out of products and be able to use other parts of the website.

- As a user, I want to be able to see what i have added to my shopping cart, 
 so that i can view previuse orders and see my total price of my cart.

- As a user, I want to make an account for my user, so that i can save details and get a subscription. 

- As a user , I want to edit info on my account and change details, so that i can switch my billing/shipping inforomation.

- As a user, I want to be able to reset my password , so i can still access my account incase i forget my password.

- As a user, I want to be able to Search products by catagory or name , so that i can find what product i want easier and quicker.

- As a user, I want to be able to , so that i can.

- As a user, I want to Sort products by price/date, and more, so that i can find the product with the lowest price or that suits my needs.

- As a user, I want to be able to sort products by the model of the bike , so that i can find parts that suit my bike.

- As a user, I want to be able to pick the product i want and pick the color if avaible, so that i can better choose my products and customise them to my needs.

- As a user, I want to be able to custom make an order form , so that i can make a customise my order for my bike.

The wireframes are found inside the wireframe directory, here you will find my mockup designs that i created on google slides.

## Features
 
### Existing Features

- CRUD functionality 

- Create - The user has the ability to create and add new products into the database via the "Add products" button. This then sends the information
that the user put into the form and creates a new file within the database with all the information about this products. Then the user is redirected back to the home 
screen where the info they filled in is displayed on the screen. 

- Read - The user has the ability to search for a file through the sort by... seaction. This organized all the videos and creates a new page with only 
products of the brand selected.

- Update - The user has the ablilty to update products from the database via the management page for the admin user.

- Delete - The user can also delete products from the database by clicking on the delete button inside of the products details page for the admin.

- Athentication - The users of this site are aloud to create users and login on their accounts to save data and have a smoother time next time in the store.

- Shopping Bag - The user can add products they want to the shopping cart. This will also automaticly update the total of the users order. They can then go from here to the checkout button and their bag item will be saved into the checkout and once payed the user will be able to see their order. While the order informstion is sent to the database.

- Products amount and color option - The user can not only add products to their bag they can also pick how many of each item they want and also pick the color of the product for some items.

- Checkout - The user is able to use the checkout app to pay for their products they added to their bag, along with being sent the order to their profiles.

- Stripe - This site uses Stripe inorderr to secure payment with card. 



### Features Left to Implement

- 

## Technologies Used

- [HTML](https://en.wikipedia.org/wiki/HTML) 
    - to create the framework of my website.
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
    - to design the look of the website and colors.
- [Javascript](https://en.wikipedia.org/wiki/JavaScript)
    - for getting bootstrap navbar
- [python](https://www.python.org/) 
    - to change the layout of the website using base.html
- [Font-awsome](http://fontawesome.com/)
    - to add some nice fonts
- [fonts.googleapis](https://fonts.google.com/)
    - add some nice text to my page
- [Bootstrap](https://getbootstrap.com/)
    - Used for navbar and other functionality
- [MongoDB](https://www.mongodb.com/)
    - to store all the data [image here](static/images/Mongodb.png)
- [Stripe](https://stripe.com/en-gb-nl)
    - for secure payments
- [Django](https://www.djangoproject.com/)
    - To create the website and the layout and framework

## Testing

- Authentications - Testing the authentactions took some time and i found that the django alluth profiles is super helpful in ordering this. I started to just customise the login html files as they were but i then remembered back to the boutique_ado lessons that we could just change around the block content eliments and then it worked with just one layout.

- database Testing - This testing involved creating multiple products and multiple sorts of failures. i had to force failures to see how the forms would react in order to catch any bugs. what i found in the end was that when i would upload a new product without an image when i clicked on thats products image on the all products view it would lead to a error. This was later fixed when i created a "no image" div and a if statement to catch this out.

- Screen sizing for mobile devices - As usual a lot of my time testing was spent making sure that the website was equally attractive on all mobile devices and screen sizes. This involved shrinking the Products title, images, and prices to move and shrink for more narrow devices. I also had to spend time to make sure that each product card had an acceptable amount of breathing space around the product while not created to much wasted space.

### Bugs

One quite interesting bug that you may notice is the footer, iv had to ask the totors many times how to fix it but i never got an outcome to work. It seems to have somthing to do with the forloop or the block content blocks. This is quite anoying to deal with however it seems to work on some pages and at some sizes while not on others. To me atleast it seems alittle random but nothing in coding is random so im sure im not understanding it enough and will hope to learn in the future how to fix this bug.

## Deployment

This site is hosted using [Heroku](https://stunt-lounge.herokuapp.com/) pages, deployed directly from the master branch. 

- Local Deployment:
 1. To run the code locally you can go to [Github repository](https://github.com/mauroindigne/one_stop_stunt_shop).
 2. There you can download a a copy/Duplacate file that includes all of the files used to create this website.
 3. Then run it as your own! 


## Credits

- Images

- Bootstrap Navbar


### Media

- The background photo is my own

### Acknowledgments

- Using the boutique_ado lessons really helped me make this project happen, there are so many parts to django and it helped me understand the layout and how to make pages work and how to get information from one app to the other using imports.