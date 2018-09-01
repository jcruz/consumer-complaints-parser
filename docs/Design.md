# Simple Web App Design Doc

## Summary
Turn a command-line app that parses consumer complaints into a simple web app.

## Goals
The user can use a web application instead of the command-line app.

## Command-line app
The user runs the command-line app which starts a session that is active until the user exits. Every search, history, show (history item), and remove (history item) command is run in the corresponding session.

Data from the csv file is parsed into an in-memory Python dictionary at the beginning of the script. Since looking up keywords can be done in constant time, history is saved as a list of keywords.

## Web app

### Endpoints

#### GET /search
Takes in a session id and keywords string and returns a list of complaints. Saves the keywords to the history corresponding to a session id.

#### GET /history
Takes in a session id and returns a list of previous search keywords.

#### DELETE /history/:id
Takes in a session id and history item id (index in list) and deletes the history item.

### Diagram
<img width="762" alt="screen shot 2018-09-01 at 12 28 57 pm" src="https://user-images.githubusercontent.com/8571671/44948145-83325f80-ade6-11e8-90d0-8ecd1d738cb3.png">

The client generates a session id (uuid preferred) when the webpage is opened. This id will be sent in all api requests (in http header or in payload).

The user can now make search requests, display search history, show history item results, and delete history items.

Why generate session id in the client? Doing so in the backend requires a separate /session endpoint to generate and delete session ids. To make the web app as simple as possible, we can omit this additional endpoint by generating a uuid in the client. The tradeoff is that sessions are not deleted and this can be solved by having a script to clean up sessions over a day old.

Data from the csv file is parsed into an in-memory Python dictionary when the server is first run. The expectation is that the input csv file is not updated frequently since new data requires a restart of the server.

History is a key-value store or database which can be used to get the history (list of keywords) for a specific session id.
