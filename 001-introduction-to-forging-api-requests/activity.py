"""
To check if your implementation is correct run test.py


*NOTE: Don't change the method names, as that's what's used in the tester.
        but, feel free to add anything else to test and debug your code.
"""
import requests
import json


def extract_feed():
    """
        Return an array of all the post objects on the feed page.
    """
    pageNumber = 0
    hasMorePosts = True
    totalPosts = []

    while hasMorePosts:
        try:
            response = requests.get(f'http://lesson-001-server:8080/feed/{pageNumber}')
            if response.status_code != 200:
                print(f"Failed to fetch page {pageNumber}. Status code: {response.status_code}")
                break

            data = response.json()
            postsList = data.get("posts", [])

            if len(postsList) > 0:
                #print(f"Fetched {len(postsList)} posts from page {pageNumber}")
                totalPosts.extend(postsList)  # <-- Correct way to add multiple posts
                pageNumber += 1
            else:
                hasMorePosts = False  # No more posts to fetch
        except Exception as e:
            print(f"An exception occurred on page {pageNumber}: {e}")
            hasMorePosts = False  # Stop on failure

    return totalPosts

def extract_emails():
    """
        Return an array of all the emails on the discover page.
    """
    pageNumber = 0
    hasMoreProfiles = True
    totalProfiles = []
    while hasMoreProfiles:
        try:
            response = requests.get(f'http://lesson-001-server:8080/discover/profiles/{pageNumber}')
            if response.status_code != 200:
                print(f' Failed to fetch page with pageNumber {pageNumber} status code : {response.status_code}')
                break
            data = response.json()
            profilesList = data.get("profiles", [])
            if len(profilesList) > 0:
                #print(f'Fetched {len(profilesList)} profiles from page {pageNumber}')
                totalProfiles.extend(profilesList)
                pageNumber += 1
            else:
                hasMoreProfiles = False
        except Exception as e:
              print(f"An exception occurred on page {pageNumber}: {e}")
              hasMorePosts = False  # Stop on failure
    #print("Total profiles")
    #print(totalProfiles)
#     for profile in totalProfiles:
#         print(f"email: {profile['email']}")
    emails = [profile['email'] for profile in totalProfiles if 'email' in profile]



    return emails

def username_exists(username):
    """
        username - The username to check if exists,  without @ (ex: username="davidteather")
        This function will return True if the provided username already exists, and false if it doesn't
    """
    pageNumber = 0
    hasMoreProfiles = True
    totalProfiles = []
    while hasMoreProfiles:
        try:
            response = requests.get(f'http://lesson-001-server:8080/discover/profiles/{pageNumber}')
            if response.status_code != 200:
                print(f' Failed to fetch page with pageNumber {pageNumber} status code : {response.status_code}')
                break
            data = response.json()
            profilesList = data.get("profiles", [])
            if len(profilesList) > 0:
                #print(f'Fetched {len(profilesList)} profiles from page {pageNumber}')
                totalProfiles.extend(profilesList)
                pageNumber += 1
            else:
                hasMoreProfiles = False
        except Exception as e:
              print(f"An exception occurred on page {pageNumber}: {e}")
              hasMorePosts = False  # Stop on failure
    usernames = [profile['username'] for profile in totalProfiles if 'username' in profile]
    if username in usernames:
        return True
    else:
        return False

if __name__ == "__main__":
    # Optional: You can call your methods here if you want to test them without running the tester
    print("MAIN FUNCTION HERE: --->>~~~")
    feed = extract_feed()
    print("EXTRACT FEED: ", feed)
    pass