class Users:
    STANDARD = "standard_user"
    LOCKED = "locked_out_user"
    PROBLEM = "problem_user"
    GLITCH = "performance_glitch_user"
    ERROR = "error_user"
    VISUAL = "visual_user"
    INVALID = "hello"


class Password:
    VALID = "secret_sauce"
    INVALID = "12345"


class Products:
    BACKPACK = "Sauce Labs Backpack"
    BIKE_LIGHT = "Sauce Labs Bike Light"
    T_SHIRT = "Sauce Labs Bolt T-Shirt"
    FLEECE = "Sauce Labs Fleece Jacket"
    ONESIE = "Sauce Labs Onesie"
    ALL_THINGS = "Test.allTheThings() T-Shirt (Red)"


class ProductsID:
    BACKPACK = "backpack"
    BIKE_LIGHT = "light"
    T_SHIRT = "bolt"
    FLEECE = "fleece"
    ONESIE = "onesie"
    ALL_THINGS = "test.allthethings()"


class ProductsImages:
    BACKPACK = "/static/media/sauce-backpack-1200x1500.0a0b85a3.jpg"
    BIKE_LIGHT = "/static/media/bike-light-1200x1500.37c843b0.jpg"
    T_SHIRT = "/static/media/bolt-shirt-1200x1500.c2599ac5.jpg"
    FLEECE = "/static/media/sauce-pullover-1200x1500.51d7ffaf.jpg"
    ONESIE = "/static/media/red-onesie-1200x1500.2ec615b2.jpg"
    ALL_THINGS = "/static/media/red-tatt-1200x1500.30dadef4.jpg"


class PagesTitle:
    PRODUCTS_PAGE = "Products"
    CART_PAGE = "Your Cart"
    INFO_PAGE = "Checkout: Your Information"
    OVERVIEW = "Checkout: Overview"
    COMPLETE = "Checkout: Complete!"


class Sort:
    AZ = "Name (A to Z)"
    ZA = "Name (Z to A)"
    LOHI = "Price (low to high)"
    HILO = "Price (high to low)"


class Social:
    TWITTER = "Twitter"
    FACEBOOK = "Facebook"
    LINKEDIN = "LinkedIn"


class SocialTitle:
    TWITTER = "X \ Sauce Labs‏ (‎@saucelabs)"
    FACEBOOK = "Sauce Labs | San Francisco CA | Facebook"
    LINKEDIN = "Sauce Labs: Overview | LinkedIn"


class ErrorMsgs:
    NO_MATCH = "Epic sadface: Username and password do not match any user in this service"
    NO_USER = "Epic sadface: Username is required"
    NO_PASSWORD = "Epic sadface: Password is required"
    LOCKED_OUT = "Epic sadface: Sorry, this user has been locked out."
    ALERT = "Sorting is broken! This error has been reported to Backtrace."
    NO_FIRST = "Error: First Name is required"
    NO_LAST = "Error: Last Name is required"
    NO_POSTAL = "Error: Postal Code is required"
