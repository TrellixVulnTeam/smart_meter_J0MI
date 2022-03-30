# smart_meter

## Remote Web Server Installation/Setup:
- 1. Clone repo ( https://github.com/jennythakkar/smart_meter )
- 2. cd into the expressjs-backend directory
  - Delete node_modules folder and package-lock.json file
  - Run "npm install" to get project dependencies
- 3. Run node index.js - This begins running the Web Server backend
  - " Listening on port 3001" should appear in terminal
- 4. In a separate terminal window, cd into the reactjs-frontend directory, then into testapp
  - run npm install for front-end dependencies
- 5. Run npm start - launches front end interface
  - Check first terminal window for console log statements to verify connection

### Additional Setup - Google API Key
- Get an API Key from a Google account and make sure MAps is turned on for the API key settings
- In testapp -> src -> components -> GoogleMapContainer.js -> line 117. There should be a comment that said /* INSERT ACTUAL API KEY */ - insert here in the double quotes to active Google Maps heatmap in interface.

## Interface Guide:
- To create an account, go to Create Account tab and enter username, password
  - 0 for consumer, 1 for utility, 2 for admin ( not functioning )
### Utility interface:
- Use information on the right side of the top of the page to operate Google Maps heatmap. Use Start Playback and Stop Playback buttons to control heatmap animation.
- Below Google Maps heatmap, The four buttons can be used to Add a Simulated Meter, Add a Physical Meter (smart meter is hard coded to be represented by Meter ID 6), Update the Data, or Delete all the meters in the system.
- In the chart below the buttons in (b), clicking the buttons in the Meter ID column change which meter is displayed in the measurement display chart at the very bottom of the Utility Interface. The buttons in the State column change Meter between running and stopped for data collection.
- Under the “Meter Assignments” title, the left-hand Update Meter Assignment tab allows for assigning a meter to a specific user in the system as well as giving the meter a geographical location for the heatmap.
- At the very bottom of the page, meter information with each timestamp, real power, reactive power, … is displayed in pages of 25 values. Step © mentions how to change which meter’s information is displayed.

### Consumer Interface:
- The interface simply displays power and energy consumption for the customer to see from their own meter
- Data displayed on pages of 25 entries

## Raspberry Pi Flask Server Setup
- In main.py and flask_server.py, change the IP address and port value to the values shown on the wifi menu (wlan0)

- Run sudo python3 with flask_server.py file

- Click on IP address URL to display data
