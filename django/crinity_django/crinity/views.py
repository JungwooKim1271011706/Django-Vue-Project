import json

from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect


# .통합테스트를 할 때 엑셀파일을 자동으로 만들어주는 프로그램의 View
def crinity(request):
    return render(request, 'crinity/crinity_testdata.html', {})

@csrf_protect
def getTestData(request):
    # 요청 객체에서 데이터 바인딩하기
    print("통신 성공")
    data = json.loads(request.body)
    row = data["row"]
    print("row >>> ", row)
    data = {"row" : row}

    return JsonResponse(data)

# 지도 API를 가지고 와서 즐겨찾기처럼 기록할 수 있는 함수
def jeilRequest():
    return ""

# 법제처 테스트용 html view 매핑
def crinity_moleg(request):
    return render(request, 'crinity/crinity_moleg.html', {})
