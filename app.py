from flask import Flask, render_template, Response, redirect
import gunicorn
from camera import *
import webbrowser
app = Flask(__name__)



@app.route('/')
def index():
    
    return render_template('index.html')
@app.route('/run-my-function', methods=['POST'])
def my_function():

    if age>=0 and age<=6:
        if emotion=="Angry":
            return redirect(f"https://youtube.com/playlist?list=PLZs7DrwFP74CfASViKUxceaiDPsCoUe-o&si=eZmLq9GPmlZLLhu0")
        elif emotion=="Fearful":
             return redirect(f"https://www.youtube.com/playlist?list=PLZs7DrwFP74BIz5wgOrJ_KVeMgSlL8n3r")
        elif emotion=="Happy":
             return redirect(f"https://www.youtube.com/playlist?list=PLZs7DrwFP74CZKwMEv7JaXi1Zg8So4jV5")
        elif emotion=="Neutral":
             return redirect(f"https://www.youtube.com/playlist?list=PLZs7DrwFP74D3OkeJ9ajDoKNmykubPbr_")
        elif emotion=="Sad":
             return redirect(f"https://www.youtube.com/playlist?list=PLZs7DrwFP74B0B9ggogf1OWnDZd90FpAi")
        else:
             return redirect(f"https://www.youtube.com/playlist?list=PLZs7DrwFP74A-KS-zE-12cBIBBPxp68X7")
    elif age>6 and age<=12:
        if emotion=="Angry":
            return redirect(f"https://www.youtube.com/playlist?list=PLZs7DrwFP74COsG2JQ9AbG1X-AfQTPTx-")
        elif emotion=="Fearful":
             return redirect(f"https://www.youtube.com/playlist?list=PLZs7DrwFP74AAhVlZFlD5hIUuX3YwXYew")
        elif emotion=="Happy":
             return redirect(f"https://www.youtube.com/playlist?list=PLZs7DrwFP74AohRGlD67Qhm3nKoUnvcvk")
        elif emotion=="Neutral":
             return redirect(f"https://www.youtube.com/playlist?list=PLZs7DrwFP74BxjpiAv4RNuBpOZ_wCIvTb")
        elif emotion=="Sad":
             return redirect(f"https://www.youtube.com/playlist?list=PLZs7DrwFP74D5RDN3vDAKkEKFP-8Dp2k_")
        else:
             return redirect(f"https://www.youtube.com/playlist?list=PLZs7DrwFP74Bdr78WI-4O5RtzRlPIlGvE")
    elif age>12 and age<=20:
        if emotion=="Angry":
            return redirect(f"https://www.youtube.com/playlist?list=PLZs7DrwFP74Colubf_po-mhPokhsFwU-I")
        elif emotion=="Fearful":
             return redirect(f"https://www.youtube.com/playlist?list=PLZs7DrwFP74B3VYYeKHkT6pVPY12g6axR")
        elif emotion=="Happy":
             return redirect(f"https://www.youtube.com/playlist?list=PLZs7DrwFP74Ae3z_-XkfqpWFWahiZExZY")
        elif emotion=="Neutral":
             return redirect(f"https://www.youtube.com/playlist?list=PLZs7DrwFP74BuUqYtJJsNzy92RmG6mHT3")
        elif emotion=="Sad":
             return redirect(f"https://www.youtube.com/playlist?list=PLZs7DrwFP74AOcrUl6RmWTR3qk28meyNW")
        else:
             return redirect(f"https://www.youtube.com/playlist?list=PLZs7DrwFP74Cmmi8rrT8Eu6lXRwuqxFzC")
    elif age>20 and age<=30:
        if emotion=="Angry":
            return redirect(f"https://www.youtube.com/playlist?list=PLZs7DrwFP74CjyapB_gMG4rl_M55joBE_")
        elif emotion=="Fearful":
             return redirect(f"https://www.youtube.com/playlist?list=PLZs7DrwFP74Co2_P9Hd9XqcoxCNwCWe9g")
        elif emotion=="Happy":
             return redirect(f"https://www.youtube.com/playlist?list=PLZs7DrwFP74AEBBbRHaC3VAWA9l4yEQ44")
        elif emotion=="Neutral":
             return redirect(f"https://www.youtube.com/playlist?list=PLZs7DrwFP74CPfmkPBdf5mUyMZ1P6MD6G")
        elif emotion=="Sad":
             return redirect(f"https://www.youtube.com/playlist?list=PLZs7DrwFP74CheVcviGSeoyPGJm-y4WRc")
        else:
             return redirect(f"https://www.youtube.com/playlist?list=PLZs7DrwFP74AhQZOyEki65B7Pf3j-cdOi")
    elif age>30 and age<=40:
        if emotion=="Angry":
            return redirect(f"https://www.youtube.com/playlist?list=PLZs7DrwFP74DJP4vxrJHjrYP2U9Uad3gr")
        elif emotion=="Fearful":
             return redirect(f"https://www.youtube.com/playlist?list=PLZs7DrwFP74A3yIBVz5t215LvqcSfjajB")
        elif emotion=="Happy":
             return redirect(f"https://www.youtube.com/playlist?list=PLZs7DrwFP74DmNm95LK9AFQyu2i851JnC")
        elif emotion=="Neutral":
             return redirect(f"https://www.youtube.com/playlist?list=PLZs7DrwFP74DZiVuFFtdMs0ct2qWqVVRM")
        elif emotion=="Sad":
             return redirect(f"https://www.youtube.com/playlist?list=PLZs7DrwFP74DHapCKt0BRNR7vWGAX5v1P")
        else:
             return redirect(f"https://www.youtube.com/playlist?list=PLZs7DrwFP74Ad1eQP_s8GMFRfanGckKSA")
    elif age>40 and age<=50:
        if emotion=="Angry":
            return redirect(f"")
        elif emotion=="Fearful":
             return redirect(f"")
        elif emotion=="Happy":
             return redirect(f"")
        elif emotion=="Neutral":
             return redirect(f"")
        elif emotion=="Sad":
             return redirect(f"")
        else:
             return redirect(f"")
    elif age>50 and age<=60:
        if emotion=="Angry":
            return redirect(f"")
        elif emotion=="Fearful":
             return redirect(f"")
        elif emotion=="Happy":
             return redirect(f"")
        elif emotion=="Neutral":
             return redirect(f"")
        elif emotion=="Sad":
             return redirect(f"")
        else:
             return redirect(f"")
    else:
        if emotion=="Angry":
            return redirect(f"")
        elif emotion=="Fearful":
             return redirect(f"")
        elif emotion=="Happy":
             return redirect(f"")
        elif emotion=="Neutral":
             return redirect(f"")
        elif emotion=="Sad":
             return redirect(f"")
        else:
             return redirect(f"")
    
         
    return "invalid"
    

def gen(camera):
    global age,emotion
    while True:
        
        frame,age,emotion = camera.get_frame()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == '__main__':
    app.debug = True
    app.run()
