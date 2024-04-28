# About This Project
A fun side project I initially started in second year, and eventually went back to deploy properly after upskilling!
Uses an API written in Flask (Python). Uses googlesearch-python to find a player's FBRef page, and ScrapeOps to safely scrape for player data, then uses pandas & matplotlib to create a player chart based on important metrics for players.
Once this is done, the image data is encoded and returned in a JSON response to a Next.js web-app and displayed to the user.

API Repo: https://github.com/worldofchami/ChartPlotterBackend (Deployed on Google Cloud Run)
