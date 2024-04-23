# googla_auth_django_react
Google-Auth react + Python Django

# Custom Google Authentication System Tutorial Code

This repository contains the code for building a custom Google authentication system using Django Rest Framework and ReactJS. The tutorial is divided into two parts: setting up the backend with Django and implementing the frontend with React.

## Key Features

- **Backend:** Django Rest Framework setup, custom user model, Google OAuth integration
- **Frontend:** React app, routing, Google login functionality


## Getting Started

1. Clone the repository: `https://github.com/cis-muzahid/googla_auth.git`

-  Follow the googleAuth/README.md file for backend setup -

-  Follow the web/README.md file for frontend setup -

# Setting up Google APIs
To enable Google login functionality in our application, we will need to set up an OAuth application through the Google Developers Console Follow the steps below.

1. Create a New Google APIs project- https://console.cloud.google.com/apis/dashboard
- Go to the Google Developer APIs Console and access the Dashboard.
- Create a new project by clicking on the “New Project” button.
- Provide a name for your project, preferably using your website or app name. This project name will be visible to users when   they are redirected to the Google login page.
- Click on “Create” to proceed.

2. Next Update the OAuth Consent Screen
- After creating the project, register your app by configuring the OAuth consent screen.
- You only need to provide the “App name,” “User support email,” and “Email addresses” under the “Developer contact information” section.
- Click on the “Save and Continue” button.

3. Create New API Credentials
- Go back to the “Dashboard” and select “Credentials” from the left panel.
- Click on the “Create Credentials” button at the top, and choose the “OAuth Client ID” option from the dropdown menu.
- Under ‘Authorized JavaScript origins’, add the following URIs:

- http://localhost:3000

Under ‘Authorized redirect URIs’, add the following URIs:

- http://localhost:3000/google

- On the same page, you will find your Client ID and Client secret under the “Credentials” section.
- Copy the Client ID and Client secret to use them in the next step of your application’s configuration.

## Refrence Link
-You can checkout on [Medium](https://onlygod.medium.com/building-a-custom-google-authentication-system-with-django-rest-framework-and-reactjs-i-925d2ba9258)
- step-by-step instructions: [Tutorial Guide](https://onlygod.medium.com/building-a-custom-google-authentication-system-with-django-rest-framework-and-reactjs-i-925d2ba9258)
