INTRODUCTION:

This is a simple server for assignment 3.
You may change the source code as you see fit, so long that running it remains the same.

In order to run the server you must have python 2.x installed (Information Systems' labs have it installed)
The command to run the server whilst in the directory containing it is:
python server.py

In order to get to the website - open your browser (chrome, preferably) and type in the address box the following:
localhost:8080

You will be automatically directed to the index.html appropriate to your device (desktop or mobile)
------------------------------
WEBSITE STRUCTURE:

The desktop version of your website must be in the desktop directory, while the mobile version in the mobile directory.
Each one of those directories must contain an index.html so that it may run properly.

*The example website does not contain an index.html for the mobile version.

The shared directory is for files shared between both versions. There are examples for using it - go over them.
For your convenience, AngularJS is already installed under shared/js/angular.min.js
------------------------------
DATA:

You can change the data-set as you see fit in the data.py file.

API calls for data are through the /data/ and you must specify a data collection:
Example for getting the "dogs" collection from the server:
Make an HTTP GET request to "/data/?_collection=dogs"

You can ask for all of the dogs from index 1 (index begins at 0!):
"/data/?_collection=dogs&_index=1"

If you specify and index that is too big you will get an empty list

You can ask for only 2 dogs:
"/data/?_collection=dogs&_length=2"
If the length is too big you will simply get the rest of the items.

Combining the two:
"/data/?_collection=dogs&_index=1&_length=2"

You can filter with specific values:
"/data/?_collection=dogs&name=Australian Shepherd"

Or category:
"/data/?_collection=dogs&size=small"

Just remember - by specifying a small list, the index might be too big!
------------------------------
MOBILE:

By using the Google Chrome device simulator you can see the mobile version of your website.
The server automatically picks the files from the mobile directory when the User Agent indicates a mobile device.