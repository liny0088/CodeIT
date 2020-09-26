import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;
from math import factorial

@app.route('/social_distancing', methods=['POST'])



def get_answer():
    def nCr (n,r):
        return int(factorial(n)/(factorial(r)*factorial(n-r)))
    
    inpu = request.get_json()
    tests = inpu.get("tests")
    ans = {}
    for key, value in tests.items():
        test = value
        seats = test.get("seats")
        ppl = test.get("people")
        space = test.get("spaces")
        spare_seats = seats - ( ppl+(ppl-1)*space  )
        if spare_seats<0:
            num = 0
        else:
            num = nCr(ppl+spare_seats, ppl)
        # ls, num = get_plan(seats,ppl,space)

        ans[key] = num
    return json.dumps({"answer":ans})