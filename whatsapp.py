from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/wa")
def wa_hello():
    return "Hello, World!"

@app.route("/wasms", methods=['POST'])
def wa_sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    Fetch_msg= request.form
    print("Fetch_msg-->",Fetch_msg)

    try: # Storing the file that user send to the Twilio whatsapp number in our computer
        msg_url=request.form.get('MediaUrl0')  # Getting the URL of the file
        print("msg_url-->",msg_url)
        msg_ext=request.form.get('MediaContentType0')  # Getting the extension for the file
        print("msg_ext-->",msg_ext)
        ext = msg_ext.split('/')[-1]
        print("ext-->",ext)
        if msg_url != None:
            json_path = requests.get(msg_url)
            filename = msg_url.split('/')[-1]
            open(filename+"."+ext, 'wb').write(json_path.content)  # Storing the file
    except:
        print("no url-->>")
    msg = request.form.get('Body').lower()  # Reading the message from the whatsapp
    print("msg-->",msg)
    resp = MessagingResponse()
    reply=resp.message()
    # Create reply

    # Text response
    if msg == "hi":
       reply.body("hey")

    # Image response
    elif msg == "image":
       reply.media('https://farm9.staticflickr.com/8295/8007075227_dc958c1fe6_z_d.jpg', caption="flower")
    
    # Audio response
    elif msg == "audio":
       reply.media('http://www.largesound.com/ashborytour/sound/brobob.mp3')
        
    # Video response
    elif msg == "video":
       reply.media('https://www.appsloveworld.com/wp-content/uploads/2018/10/640.mp4')
    
    # Document response
    elif msg == "file":
       reply.media('http://www.africau.edu/images/default/sample.pdf')
    
    else:
        reply.body("from you")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
