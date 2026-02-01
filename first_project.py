from flask import Flask, render_template_string

app = Flask(__name__)

HER_NAME = "Dai"  # 👈 change this

HTML = f"""
<!DOCTYPE html>
<html>
<head>
    <title>mero lado chusnus 💖</title>
    <style>
        body {{
            font-family: 'Comic Sans MS', cursive;
            background: linear-gradient(to bottom, #ff9a9e, #fad0c4);
            text-align: center;
            padding-top: 40px;
            overflow: hidden;
        }}
        h1 {{
            font-size: 42px;
            color: #b30059;
        }}
        img {{
            width: 300px;
            margin: 20px;
        }}
        button {{
            font-size: 24px;
            padding: 15px 30px;
            border: none;
            border-radius: 12px;
            cursor: pointer;
            position: absolute;
        }}
        #yes {{
            background-color: #ff3366;
            color: white;
            left: 40%;
            top: 60%;
        }}
        #no {{
            background-color: gray;
            color: white;
            left: 55%;
            top: 60%;
        }}
    </style>
</head>
<body>

<h1>💘 {HER_NAME}, Please mero lado chusnus na hunxa? 💘</h1>

<img src="https://media.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif">

<button id="yes" onclick="yesClick()">YES 😍</button>
<button id="no" onmouseover="moveNo()">NO 😢</button>

<script>
    let yesSize = 24;

    function moveNo() {{
        let noBtn = document.getElementById("no");
        let x = Math.random() * (window.innerWidth - 100);
        let y = Math.random() * (window.innerHeight - 100);
        noBtn.style.left = x + "px";
        noBtn.style.top = y + "px";

        yesSize += 4;
        let yesBtn = document.getElementById("yes");
        yesBtn.style.fontSize = yesSize + "px";
        yesBtn.style.padding = (yesSize / 2) + "px";
    }}

    function yesClick() {{
        document.body.innerHTML = `
            <h1>💖 Gha gha gha gha majja aayo 💖</h1>
            <h1>{HER_NAME}, you made me the happiest person 😍</h1>
            <img src="https://media.giphy.com/media/l4FGpPki5v2Bcd6Ss/giphy.gif">
        `;
    }}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

