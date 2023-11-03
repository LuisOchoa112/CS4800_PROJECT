import account_page as ap
import favorites_page as fp
import home_page
import login

if __name__ == "__main__":
    user_id = login.login()
    
    while(user_id != None):
        fp.list_favorite_meals(user_id)
        ap.account_page(user_id)
    