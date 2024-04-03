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

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))