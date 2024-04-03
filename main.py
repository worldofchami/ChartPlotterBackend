import get_link as gl
import pandas_scraping as ps
import radar_from_arrs as ra
import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/chart/<name>", methods=["GET"])
def generate(name):
    url = gl.getFBRefLink(name)
    arrs = ps.player(url)
    res = ra.radar(arrs[0], arrs[1])
    
    try:
        return jsonify({
            "ok": True,
            "message": res
        })
    
    except Exception as e:
        print(e)
        return jsonify({
            "ok": False,
            "message": "Error generating chart. Please try again!"
        })

def create_app():
   return app

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)