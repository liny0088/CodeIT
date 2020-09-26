import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

@app.route('/social_distancing', methods=['POST'])



def get_answer():

    def incr_by_one(ls, base, limit):
        last_index = len(ls)-1
        no_add = True
        while no_add:
            cur_num = ls[last_index] 
            if cur_num<limit:
                ls[last_index]+=1
                break
            elif cur_num == limit:
                ls[last_index]=base
                last_index-=1
        return ls

    def get_plan(seats,ppl,space):
        max_of_space = seats - ppl ## <=max
        run = True
        answer_list = []
        space_before_person = [0]
        if ppl==1:
            return [], seats
        elif space*(ppl-1)+ppl > seats:
            return [], 0    

        for i in range(ppl-1):
            space_before_person.append(space)
            
        pace_before_person = space_before_person[0:-1]

        while run:
            if space_before_person[0] == max_of_space:
                break
            if sum(space_before_person)<= max_of_space:
                answer_list.append(space_before_person.copy())
            space_before_person = incr_by_one(space_before_person,space,max_of_space)

        return answer_list, len(answer_list)

    inpu = request.get_json()
    tests = inpu.get("tests")
    ans = {}
    for key, value in tests.items():
        test = value
        seats = test.get("seats")
        ppl = test.get("people")
        space = test.get("spaces")
        ls, num = get_plan(seats,ppl,space)
        ans[key] = num
    return jsonify({"answers":ans})