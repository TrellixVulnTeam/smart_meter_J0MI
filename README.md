# smart_meter

## Remote Web Server Installation/Setup:
- 1. Clone repo
- 2. cd into WebServer directory
  - Delete node_modules folder and package-lock.json file
  - Run "npm install" to get project dependencies
- 3. Run node index.js - This begins running the Web Server backend
  - " Listening on port 3001" should appear
- 4. In a separate terminal window, cd into the WebServer, then into testapp
  - run npm install
- 5. Run npm start - launches front end interface
  - Check first terminal window for console log statements to verify connection

### Additional Setup - Google API Key
- Get an API Key from a Google account and make sure MAps is turned on for the API key settings
- In testapp -> src -> components -> GoogleMapContainer.js -> line 117. There should be a comment that said /* INSERT ACTUAL API KEY */ - insert here in the double quotes to active Google Maps heatmap in interface.

## Interface Guide:
- To create an account, go to Create Account tab and enter username, password
  - 0 for consumer, 1 for utility, 2 for admin
### Utility interface: 
