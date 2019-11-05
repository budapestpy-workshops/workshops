# Plotly Express and Python and SQL

## SQLite and Python
The idea came from a pydata meetup, where someone presented a Python project with the BKK vehicles routes. I simplified it, and got all the stops from BKK's page (it's called GTFS). For practicing reasons, we made a table in the SQLite database from Python, where we inserted the previously readed csv-s values. Then the table was brought back to pandas, and visualise with Folium. The problem was that there are ~5000 stops, which kills the computer when it tries to draw every piece of it one by one. We used the markercluster function of folium to compress the pins. This notebook aims to show you the basic SQL commands, such as SELECT / INSERT INTO / DELETE, the connection with Python, and a brief intorduction to the folium package.
As always, there are two notebooks, the one with the "ws" ending is the emptier one, which we filled up together on the workshop.
