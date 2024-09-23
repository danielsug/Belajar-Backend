from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

app= Flask(__name__)

api =Api(app)

CORS(app)

identitas ={}


class ContohResource(Resource):

    def get(self):
    #    response = {'msg':'Hallo Dunia'}
    #    return response  
        return identitas
    
    def post(self):
        nama = request.form["nama"]
        umur = request.form["umur"]
        print("POST/FORM:",umur)
        identitas["nama"] = nama
        identitas["umur"] = umur
    #    nama = request.args.get("nama")
    #    umur = request.args.get("umur")
    #    print("GET:",umur)
        response = {"msg": "Data berhasil di post"}
        return response
    


api.add_resource(ContohResource,"/api",methods=['get','post'])

if __name__ == "__main__":
    app.run(debug=True,port=5005)


