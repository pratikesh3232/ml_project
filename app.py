from flask import Flask
from src.logger import logging
import os,sys
from src.exception import CustmeException

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("testing exception")
    except Exception as e:
        abc = CustmeException(e,sys)
        logging.info(abc.error_message)
        return "WLECOME BUDDY"


if __name__ == "__main__":
    app.run(debug = True)