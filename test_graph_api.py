import json
import facebook
from push_to_mongodb import *
from credential import token # create a python file name credential and assign your Facebook Access Token to a variable token there
import logging

def main():
    graph = facebook.GraphAPI(token)
    for i in range(210):
        print("\n")
        iden = get_one_uid_api()
        try:
            print(f"Working on {iden}")
            respond = graph.get_object(iden, fields='name, first_name,middle_name,last_name,gender,hometown,'
                                                    'significant_other,albums, feed, likes, music, meeting_for, '
                                                    'birthday,email,languages, picture,age_range,favorite_athletes, '
                                                    'favorite_teams')
            print(respond)
            push_one_user_profile_api(respond)
        except BaseException as e:
            print(e)
            print(f"Error, uid not exist or ranout of request per hour")
            push_one_uid_api(iden)
            print(f"{iden} pushed error uid to database")
            continue


if __name__ == '__main__':
    main()
