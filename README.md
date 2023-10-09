# DRF_assignment
# My Project

Welcome to my assignment, here are some images to guide you to figure out how it works

![I have created 2 apps, a product app and a cart app. As you can see these are their URL patterns. I used DRF routers to automatically route the views](https://i.imgur.com/lF4Xodb.png)

### I have added 2 apps, one being the products app and the other being the carts app. I routed both the apps through drf routers.


![Image 2](https://i.imgur.com/7Ek8gS0.png)

### We can send a post request to create products, a delete request to delete products, list all the products and also by their UUID

### If we try to send a request, where the parameters dont match. For example a request like this 

    {
        "id": "fa8dd73a-7b5a-4dbe-b10a-cd5c10dc6e43",
        "name": "Polo Tshirt",
        "image": "/media/images/Untitled.jpeg",
        "quantity": 1,
        "category": "clothing",
        "size": "",
        "weight": "1kg"
    }
### The request wont be accepted ad clothing is a category where the parameter should be size and not weight.
![Image 3](https://i.imgur.com/kuk1Jp0.png)

### In the cart list endpoint we can see the list of all the users (In hindset this is not a good practice as users should ideally be stored in a seperate app). I have created a seperate model for users with one to one relationship with the cart. 

![Image 3](https://i.imgur.com/PpzXlUd.png)
### A new item can simply be added by passing a parameter of the items UUID. 


