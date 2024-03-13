from flask import Flask, request, jsonify
def convert_to_json(notices):
    # 목록을 json으로 변경 반환
    result = jsonify(error_code=0, error_msg='OK', data=notices)
    # result.headers["Access-Control-Allow-Origin"] = "*"
    return result
