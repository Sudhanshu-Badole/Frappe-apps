# # # import calendar


# # # def append_dates_to_doctype(selected_month, year):
# # #     week_day = {
# # #         6:'Sunday',
# # #         0:'Monday',
# # #         1:'Tuesday',
# # #         2:'Wednesday',
# # #         3:'Thursday',
# # #         4:'Friday',
# # #         5:'Saturday'
# # #     }
# # #     month_index = list(calendar.month_name).index(selected_month)
# # #     print(month_index)
# # #     doc = []
# # #     cal = calendar.monthcalendar(year, month_index)
# # #     print(cal)
# # #     # dates_in_month = [day for week in cal for day in week if day != 0]
# # #     a = []
# # #     for week in cal:
# # #         for day in week:
# # #             if day !=0:
# # #                 d = week.index(day)
# # #                 print(day,week_day[d])
# # #     # print(dates_in_month)

# # #     # day_list = [day for week in cal for day in week if day != 0]
# # #     # for day in week:
        
# # # 	# weekday_names = [calendar.day_name[calendar.weekday(self.year,month_index, day)] for day in day_list]

# # #     # for date in dates_in_month:
# # #     #     doc.append(date)

# # # # Example usage:
# # # # Assuming 'selected_month' is a variable containing the selected month (e.g., 'May')
# # # selected_month = 'June'
# # # selected_year = 2024  # Adjust the year as needed


# # # res = append_dates_to_doctype(selected_month, selected_year)
# # # # print(res)
# # # print(calendar.day_name[calendar.weekday(2023,12, 15)] )



# # """email valid code"""

# # import re

# # # Make a regular expression
# # # for validating an Email
# # regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

# # # Define a function for
# # # for validating an Email
# # def check(email):

# # 	# pass the regular expression
# # 	# and the string into the fullmatch() method
# # 	if(re.fullmatch(regex, email)):
# # 		print("Valid Email")

# # 	else:
# # 		print("Invalid Email")

# # # Driver Code
# # if __name__ == '__main__':

# # 	# Enter the email
# # 	email = "ankitrai326@gmail.com"

# # 	# calling run function
# # 	check(email)

# # 	email = "my.ownsite@our-earth.org"
# # 	check(email)

# # 	email = "ankitrai326.com"
# # 	check(email)


# # import frappe
# # from frappe import _

# # @frappe.whitelist()
# # def upload_file(file_data):
# #     file_doc = frappe.get_doc({
# #         "doctype": "FileUpload",
# #         "file": file_data
# #     })


# #     if file_doc.file.lower().endswith('.jpg'):
# #         file_doc.insert(ignore_permissions=True)
# #         frappe.db.commit()
# #         return _("File uploaded successfully and it is a JPG file.")
# #     else:
# #         return _("Please upload a file with a .jpg extension.")


# # num = 123
# # x = num
# # rev = 0
# # while x!=0:
# #     digit = x%10

# #     rev = rev*10 +digit
# #     x//=10
# #     print('x',x)
# # print(rev)








# import requests

# def get_access_token(client_id, client_secret, code):
#     token_url = 'https://github.com/login/oauth/access_token'
#     payload = {
#         'client_id': client_id,
#         'client_secret': client_secret,
#         'code': code
#     }
#     headers = {'Accept': 'application/json'}
    
#     response = requests.post(token_url, data=payload, headers=headers)
    
#     if response.status_code == 200:
#         return response.json().get('access_token')
#     else:
#         print(f"Failed to retrieve access token. Status code: {response.status_code}")
#         return None

# def fetch_user_repositories(access_token):
#     repositories_url = 'https://api.github.com/user/repos'
#     headers = {
#         'Authorization': f'Bearer {access_token}',
#         'Accept': 'application/json'
#     }
    
#     response = requests.get(repositories_url, headers=headers)
    
#     if response.status_code == 200:
#         return response.json()
#     else:
#         print(f"Failed to fetch repositories. Status code: {response.status_code}")
#         return None

# def main():
#     # GitHub OAuth App credentials
#     client_id = 'YOUR_CLIENT_ID'
#     client_secret = 'YOUR_CLIENT_SECRET'
#     authorization_code = 'AUTHORIZATION_CODE_FROM_GITHUB'
    
#     # Exchange authorization code for an access token
#     access_token = get_access_token(client_id, client_secret, authorization_code)
    
#     if access_token:
#         # Fetch repositories using the access token
#         repositories = fetch_user_repositories(access_token)
        
#         if repositories:
#             print("Repositories:")
#             for repo in repositories:
#                 print(repo['name'])
#         else:
#             print("Failed to fetch repositories.")
#     else:
#         print("Access token retrieval failed.")

# if __name__ == "__main__":
#     main()

# nums1 = [1,2]
# nums2 = [3,4]
# n=[]
# nums1.extend(nums2)
# nums1.sort()
# i=len(nums1)//2
# if i==1:
#    nums1[i]
# elif i>1:
#     for x in range(i):
#         n.append(nums1[x+1])


# res=sum(n)/len(n)
# print("sss",res)

import subprocess

command = "bench --version"

try:
    output = subprocess.check_output(command.split(), text=True)
    print('output:\n'+output)
except subprocess.CalledProcessError as e:
    print("Error executing command:", e)


#*********************************************************
    """To get all repo"""
import requests

def get_repository_names(username):
    url = f"https://api.github.com/users/{username}/repos"
    headers = {"Accept": "application/vnd.github.v3+json"} 
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            repositories = response.json()
            repository_names = [repo['name'] for repo in repositories] 
            
            return repository_names
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Request Exception: {e}")
        return None

username = 'Sudhanshu-Badole'
repository_names = get_repository_names(username)

if repository_names:
    print(f"Repositories for {username}:")
    for name in repository_names:
        print(name)
else:
    print("Failed to fetch repository names.")


#****************************************************
    """to get branch"""

import requests

owner = username
repo = 'Sales_Insight'

url = f'https://api.github.com/repos/{owner}/{repo}/branches'
headers = {'Accept': 'application/vnd.github.v3+json'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    branches = response.json()
    for branch in branches:
        print(branch['name'])
else:
    print(f"Failed to fetch branches. Status code: {response.status_code}")

# Fetch releases
url_releases = f'https://api.github.com/repos/{owner}/{repo}/releases'
response_releases = requests.get(url_releases, headers={'Accept': 'application/vnd.github.v3+json'})

if response_releases.status_code == 200:
    releases = response_releases.json()
    print("Releases:")
    for release in releases:
        print(release['tag_name'], release['name'])
else:
    print(f"Failed to fetch releases. Status code: {response_releases.status_code}")

# Fetch tags
url_tags = f'https://api.github.com/repos/{owner}/{repo}/tags'
response_tags = requests.get(url_tags, headers={'Accept': 'application/vnd.github.v3+json'})

if response_tags.status_code == 200:
    tags = response_tags.json()
    print("\nTags:")
    for tag in tags:
        print(tag['name'])
else:
    print(f"Failed to fetch tags. Status code: {response_tags.status_code}")
