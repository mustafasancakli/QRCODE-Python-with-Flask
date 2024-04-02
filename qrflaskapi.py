from flask import Flask, request, send_file
import qrcode

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def generate_qr():
    if request.method == "GET":
        return """
        <form method="post">
            <label for="input_data">Input Data:</label><br>
            <input type="text" id="input_data" name="input_data"><br>
            <label for="image_format">Image Format:</label><br>
            <select id="image_format" name="image_format">
                <option value="png">PNG</option>
                <option value="jpeg">JPEG</option>
                <option value="gif">GIF</option>
            </select><br>
            <input type="submit" value="Generate QR">
        </form>
        """
    elif request.method == "POST":
        input_data = request.form["input_data"]
        image_format = request.form["image_format"]
        qr = qrcode.make(input_data)
        file_name = "qr_code." + image_format
        qr.save(file_name)
        return send_file(file_name, mimetype="image/" + image_format)

if __name__ == "__main__":
    app.run()
