# Xmeme

# App Live on
https://xmemesstream.herokuapp.com/

## Project Description
A Meme Stream Page where users can post memes by providing their name, a caption for the meme and the URL for the meme image as input. The page retrieves and displays the latest 100 posted Memes (names + meme images + caption).

## Tech/framework used
This project is built using Django framework where users can post memes and view all of them. The api is built using django REST framework.

## Prerequisites
Run "install.sh" to deal with all the dependencies

## Serving the App : 
Run "server_run.sh" to get your backend server up and running

## Flows
1. Users will post Memes by providing these inputs<br />
   -- Name of the person posting the meme<br />
   --Caption for the Meme<br />
   --URL of the Meme image

2. Users will view the latest 100 memes posted<br />
  -- If they post a new meme, it will get listed. Note that these submitted memes will be shown one below the other.<br />
  -- Each meme should display the name of the meme maker, the caption for the meme and the image pulled from the meme URL.<br />
  
##  Project Overview
1. The backend shall be capable of receiving the posted meme inputs from the frontend and store them in a database.
2. The backend shall be capable of fetching the list of memes from the database and send them to the frontend.
3. The interaction between the frontend and backend shall be based on a REST API with support for the below 3 endpoints.
4. Endpoint to send a meme to the backend

  -- HTTP Method - POST

  -- Endpoint - /memes

  --Json Body contains these inputs:
    - name, url, caption

  --The backend should allocate a unique id for the meme and return it as a json response.

  --Example request:
  
  `curl --location --request POST 'http://localhost:8081/memes' --header 'Content-Type: application/json' --data '{"name": "varun kumar","caption": "Is this a meme ?","url":     "https://urlme.me/hello/typed_a_url/made_a_meme.jpg"}'`

Endpoint to fetch the latest 100 memes created from the backend
HTTP Method - GET
Endpoint - /memes
Error:
If there are no memes available, an empty array shall be returned.
Example request: <br />
`curl --location --request GET 'http://localhost:8081/memes'`


Endpoint to specify a particular id (identifying the meme) to fetch a single Meme.
HTTP Method - GET
Endpoint - /memes/<id>
Error:
If a meme with that Id doesn’t exist, a 404 HTTP response code should be returned.
Example request:<br />
`curl --location --request GET 'http://localhost:8081/memes/<id>'`
