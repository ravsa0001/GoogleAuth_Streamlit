## _Google Authentication within Streamlit web page_

This project provides a simple example of integrating google authenication with a Streamlit web application. Users can log in using their Google accounts to access specific features or data within the Streamlit app.

## Prerequisites
- python(>3.9)
- pip(package manager)


## Installation/SetUp
**clone the repo**
```sh
git clone https://github.com/ravsa0001/GoogleAuth_Streamlit.git
cd GoogleAuth_Streamlit
```
**Install the dependecies**
```sh
pip install -r requirements.txt
```

After that, you need to do some necessary things for code to work properly
- Go to [Google Console](https://console.cloud.google.com/?pli=1) webpage
- After log-In, select or create a project
- Then, from **API and services** go to **Enabled API and services**
- Search for People.googleAPI and **Enable** it
- Then, go to **OAuth consent screen** and select external user
- Fill the **App information** and **Developers contact information**. Then, Save and continue
- After that, add **Scopes**(./auth/userinfo.email and ./auth/userinfo.profile). Then, Save and continue
- After that, add **test users** and continue 
- Now, go to **Credentials** and in **Create Credentials** select **OAuth Cliend ID**
- Select the **web application** as **Application type** and fill **Name and authorized redirect URIs** and continue
- After filling details you'll get a json file and details(Client_ID, Client_secret)
- Fill these details and your redirected URI in your .env file
- After that run main.py by the code given below
```sh
streamlit run main.py
```
