from flask import Flask
from flask import request
import sys
from flask import jsonify
from ast import literal_eval
from enum import Enum
import requests
import json

application = Flask(__name__)

@application.route("/cal1", methods=['POST','GET'])
def cal1():
    req = request.get_json()
    print(req)
    res = {
     "version": "2.0",
     "template": {
      "outputs": [
        {
         "simpleText": {
          "text": "청약 통장 가입기간은 어떻게 되나요? (미성년자 가입기간은 2년 초과시 2년만 인정)"
            }
          },
      ],
      "quickReplies": [
             {
              "action": "block",
              "label": "6개월미만",
              "blockId": "61499051790c137823e1911b"
             },
             {
              "action": "block",
              "label": "6개월이상~1년미만",
              "blockId": "61499051790c137823e1911b"
             },
             {
              "action": "block",
              "label": "1년이상~2년미만",
              "blockId": "61499051790c137823e1911b"
             },
             {
              "action": "block",
              "label": "2년이상~3년미만",
              "blockId": "61499051790c137823e1911b"
             },
             {
              "action": "block",
              "label": "3년이상~4년미만",
              "blockId": "61499051790c137823e1911b"
             },
             {
              "action": "block",
              "label": "5년이상~6년미만",
              "blockId": "61499051790c137823e1911b"
             },
             {
              "action": "block",
              "label": "6년이상~7년미만",
              "blockId": "61499051790c137823e1911b"
             },
             {
              "action": "block",
              "label": "7년이상~8년미만",
              "blockId": "61499051790c137823e1911b"
             }
            ]
       }
    }
    return res

@application.route("/cal2", methods=['POST','GET'])
def cal2():
    req = request.get_json()
    print(req)
    res = {
      "version": "2.0",
      "template": {
        "outputs": [
          {
           "basicCard": {
            "title": "결혼하셧나요?",
            "description": "미혼/기혼중에 선택해주세요!",
            "thumbnail": {
            },
            "buttons": [
             {
              "action": "block",
              "label": "기혼",
              "blockId": "614990bee587ab407d64d952"
             },
             {
              "action":  "block",
              "label": "미혼",
              "blockId": "614990bee587ab407d64d952"
             }
            ]
           }
          }
        ]
      }
    }
    return res

@application.route("/cal3", methods=['POST','GET'])
def cal3():
    req = request.get_json()
    print(req)
    res = {
     "version": "2.0",
     "template": {
      "outputs": [
        {
         "simpleText": {
          "text": "만 30세부터의 무주택 기간을 입력하세요?"
            }
          },
      ],
      "quickReplies": [
             {
              "action": "block",
              "label": "유주택자",
              "blockId": "6151e2dcc43f766a52639539"
             },
             {
              "action": "block",
              "label": "1년미만",
              "blockId": "6151e2dcc43f766a52639539"
             },
             {
              "action": "block",
              "label": "1년이상~2년미만",
              "blockId": "6151e2dcc43f766a52639539"
             },
             {
              "action": "block",
              "label": "2년이상~3년미만",
              "blockId": "6151e2dcc43f766a52639539"
             },
             {
              "action": "block",
              "label": "3년이상~4년미만",
              "blockId": "6151e2dcc43f766a52639539"
             },
             {
              "action": "block",
              "label": "4년이상~5년미만",
              "blockId": "6151e2dcc43f766a52639539"
             },
             {
              "action": "block",
              "label": "5년이상~6년미만",
              "blockId": "6151e2dcc43f766a52639539"
             },
             {
              "action": "block",
              "label": "6년이상~7년미만",
              "blockId": "6151e2dcc43f766a52639539"
             },
             {
              "action": "block",
              "label": "7년이상~",
              "blockId": "6151e2dcc43f766a52639539"
             }
            ]
       }
    }
    return res

@application.route("/cal4", methods=['POST','GET'])
def cal4():
    req = request.get_json()
    print(req)
    res = {
     "version": "2.0",
     "template": {
      "outputs": [
        {
         "simpleText": {
          "text": "본인의 직계존속(부모/조부모)은 몇명인가요??"
            }
          },
      ],
      "quickReplies": [
             {
              "action": "block",
              "label": "0명",
              "blockId": "614991e395da9d3ef0d3f697"
             },
             {
              "action": "block",
              "label": "1명",
              "blockId": "614991e395da9d3ef0d3f697"
             },
             {
              "action": "block",
              "label": "2명",
              "blockId": "614991e395da9d3ef0d3f697"
             },
             {
              "action": "block",
              "label": "3명",
              "blockId": "614991e395da9d3ef0d3f697"
             },
             {
              "action": "block",
              "label": "4명",
              "blockId": "614991e395da9d3ef0d3f697"
             },
             {
              "action": "block",
              "label": "5명",
              "blockId": "614991e395da9d3ef0d3f697"
             },
             {
              "action": "block",
              "label": "6명",
              "blockId": "614991e395da9d3ef0d3f697"
             },
             {
              "action": "block",
              "label": "7명",
              "blockId": "614991e395da9d3ef0d3f697"
             },
             {
              "action": "block",
              "label": "8명",
              "blockId": "614991e395da9d3ef0d3f697"
             }
            ]
       }
    }
    return res

@application.route("/cal5", methods=['POST','GET'])
def cal5():
    req = request.get_json()
    print(req)
    res = {
     "version": "2.0",
     "template": {
      "outputs": [
        {
         "simpleText": {
          "text": "본인의 비직계존속은 몇명인가요"
          "(신청자와 동일한 주민등록등본에 등재된 미혼 자녀)"
            }
          },
      ],
      "quickReplies": [
             {
              "action": "block",
              "label": "0명",
              "blockId": "615f0fa0c78e3769ca99fbd0"
             },
             {
              "action":  "block",
              "label": "1명",
              "blockId": "615f0ef04687a505ab3bc4a2"
             },
             {
              "action": "block",
              "label": "2명",
              "blockId": "615f0df9fd9c5c5a547cc59b"
             },
             {
              "action": "block",
              "label": "3명",
              "blockId": "615f0d2bd693b414f1fbfd2d"
             },
             {
              "action": "block",
              "label": "4명",
              "blockId": "615dc5c8c8215d088c14fd9c"
             },
             {
              "action": "block",
              "label": "5명",
              "blockId": "615dbf10c8215d088c14fd9a"
             },
             {
              "action": "block",
              "label": "6명",
              "blockId": "615b20499adc8f4e0966c8fb"
             },
            ]
           }
          }
    return res

@application.route("/Map_01", methods=['POST','GET'])
def Map_01():

    req = request.get_json()
    print(req)
    res = {
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "listCard": {
          "header": {
            "title": "경기 북부"
          },
          "items": [
            {
              "title": "고양시 마이홈",
              "description": "경기도 고양시 일산서구 강성로 247",
              "link": {
                "web": "https://www.myhome.go.kr/hws/portal/gis/portalMap.do?mode=cnslr&brtc_code=41&signgu_code=287&legaldong_code=10400&inhbtnt_cnter_nm=%EA%B3%A0%EC%96%91%EA%B6%8C%20%EB%A7%88%EC%9D%B4%ED%99%88%EC%84%BC%ED%84%B0"
              }
            },
            {
              "title": "김포시 마이홈",
              "description": "경기도 김포시 김포한강4로 129",
              "link": {
                "web": "https://www.myhome.go.kr/hws/portal/gis/portalMap.do?mode=cnslr&brtc_code=41&signgu_code=570&legaldong_code=10400&inhbtnt_cnter_nm=%EA%B9%80%ED%8F%AC%EA%B6%8C%20%EB%A7%88%EC%9D%B4%ED%99%88%EC%84%BC%ED%84%B0"
              }
            },  
            {
              "title": "남양주시 마이홈",
              "description": "경기도 남양주시 다산중앙로 123번길 22-80",
              "link": {
                "web": "https://www.myhome.go.kr/hws/portal/gis/portalMap.do?mode=cnslr&brtc_code=41&signgu_code=310&legaldong_code=11200&inhbtnt_cnter_nm=%EB%82%A8%EC%96%91%EC%A3%BC%EA%B6%8C%20%EB%A7%88%EC%9D%B4%ED%99%88%EC%84%BC%ED%84%B0"
              }
            },
            {
              "title": "부천시 마이홈",
              "description": "경기도 부천시 길주로 281",
              "link": {
                "web": "https://www.myhome.go.kr/hws/portal/gis/portalMap.do?mode=cnslr&brtc_code=41&signgu_code=190&legaldong_code=10800&inhbtnt_cnter_nm=%EB%B6%80%EC%B2%9C%EA%B6%8C%20%EB%A7%88%EC%9D%B4%ED%99%88%EC%84%BC%ED%84%B0"
              }
            },
            {
              "title": "성남시 마이홈",
              "description": "경기도 성남시 분당구 서현로 192",
              "link": {
                "web": "https://www.myhome.go.kr/hws/portal/gis/portalMap.do?mode=cnslr&brtc_code=41&signgu_code=135&legaldong_code=10500&inhbtnt_cnter_nm=%EC%84%B1%EB%82%A8%EA%B6%8C%20%EB%A7%88%EC%9D%B4%ED%99%88%EC%84%BC%ED%84%B0"
              }
            },
            {
              "title": "수원시 마이홈",
              "description": "경기도 수원시 영통구 광교로 146",
              "link": {
                "web": "https://www.myhome.go.kr/hws/portal/gis/portalMap.do?mode=cnslr&brtc_code=41&signgu_code=117&legaldong_code=10300&inhbtnt_cnter_nm=%EC%88%98%EC%9B%90%EA%B6%8C%20%EB%A7%88%EC%9D%B4%ED%99%88%EC%84%BC%ED%84%B0"
              }
            },
            {
              "title": "시흥시 마이홈",
              "description": "경기도 시흥시 승지로 60번길 28",
              "link": {
                "web": "https://www.myhome.go.kr/hws/portal/gis/portalMap.do?mode=cnslr&brtc_code=41&signgu_code=390&legaldong_code=11800&inhbtnt_cnter_nm=%EC%8B%9C%ED%9D%A5%EA%B6%8C%20%EB%A7%88%EC%9D%B4%ED%99%88%EC%84%BC%ED%84%B0"
              }
            }
          ],
          "buttons": [
            {
              "label": "이전단계",
              "action": "block",
              "blockId": "김윤익-마이홈센터"
            }
          ]
        }
      }
    ]
  }
}
    return res

@application.route("/Map_02", methods=['POST','GET'])
def Map_02():

    req = request.get_json()
    print(req)
    res = {
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "listCard": {
          "header": {
            "title": "경기 남부 "
          },
          "items": [
            {
              "title": "안양시 마이홈",
              "description": "경기도 안양시 동안구 평촌대로 212번길 55",
              "link": {
                "web": "https://www.myhome.go.kr/hws/portal/gis/portalMap.do?mode=cnslr&brtc_code=41&signgu_code=173&legaldong_code=10200&inhbtnt_cnter_nm=%EC%95%88%EC%96%91%EA%B6%8C%20%EB%A7%88%EC%9D%B4%ED%99%88%EC%84%BC%ED%84%B0"
              }
            },
            {
              "title": "오산시 마이홈",
              "description": "경기도 오산시 경기대로 761번길 36",
              "link": {
                "web": "https://www.myhome.go.kr/hws/portal/gis/portalMap.do?mode=cnslr&brtc_code=41&signgu_code=370&legaldong_code=11300&inhbtnt_cnter_nm=%EC%98%A4%EC%82%B0%EA%B6%8C%20%EB%A7%88%EC%9D%B4%ED%99%88%EC%84%BC%ED%84%B0"
              }
            },
            {
              "title": "용인시 마이홈",
              "description": "경기도 용인시 기흥구 동백중앙로 225-6",
              "link": {
                "web": "https://www.myhome.go.kr/hws/portal/gis/portalMap.do?mode=cnslr&brtc_code=41&signgu_code=463&legaldong_code=11600&inhbtnt_cnter_nm=%EC%9A%A9%EC%9D%B8%EA%B6%8C%20%EB%A7%88%EC%9D%B4%ED%99%88%EC%84%BC%ED%84%B0"
              }
            },
            {
              "title": "의정부시 마이홈",
              "description": "경기도 의정부시 신흥로 251 구성타워 9층",
              "link": {
                "web": "https://www.myhome.go.kr/hws/portal/gis/portalMap.do?mode=cnslr&brtc_code=41&signgu_code=150&legaldong_code=10100&inhbtnt_cnter_nm=%EC%9D%98%EC%A0%95%EB%B6%80%EA%B6%8C%20%EB%A7%88%EC%9D%B4%ED%99%88%EC%84%BC%ED%84%B0"
              }
            },
            {
              "title": "파주시 마이홈",
              "description": "경기도 파주시 경의로 1004번길 33 월드타워 8차",
              "link": {
                "web": "https://www.myhome.go.kr/hws/portal/gis/portalMap.do?mode=cnslr&brtc_code=41&signgu_code=480&legaldong_code=10800&inhbtnt_cnter_nm=%ED%8C%8C%EC%A3%BC%EA%B6%8C%20%EB%A7%88%EC%9D%B4%ED%99%88%EC%84%BC%ED%84%B0"
              }
            },
            {
              "title": "하남시 마이홈",
              "description": "경기도 하남시 미사강변한강로 290-3 희망상가 2층",
              "link": {
                "web": "https://www.myhome.go.kr/hws/portal/gis/portalMap.do?mode=cnslr&brtc_code=41&signgu_code=450&legaldong_code=10900&inhbtnt_cnter_nm=%EC%84%9C%EC%9A%B8%EB%8F%99%EB%B6%80%EA%B6%8C%20%EB%A7%88%EC%9D%B4%ED%99%88%EC%84%BC%ED%84%B0"
              }
            },
            {
              "title": "화성시 마이홈",
              "description": "경기도 화성시 메타폴리스로 53",
              "link": {
                "web": "https://www.myhome.go.kr/hws/portal/gis/portalMap.do?mode=cnslr&brtc_code=41&signgu_code=590&legaldong_code=12700&inhbtnt_cnter_nm=%ED%99%94%EC%84%B1%EB%8F%99%EB%B6%80%EA%B6%8C%20%EB%A7%88%EC%9D%B4%ED%99%88%EC%84%BC%ED%84%B0"
              }
            }
          ],
          "buttons": [
            {
              "label": "이전단계",
              "action": "block",
              "blockId": "김윤익-마이홈센터"
            }
          ]
        }
      }
    ]
  }
}
    return res

@application.route("/Sche_01", methods=['POST','GET'])
def Sche_01():

    req = request.get_json()
    print(req)
    res = {
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "basicCard": {
          "title": "분양일정",
          "profile": {
            "imageUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4BJ9LU4Ikr_EvZLmijfcjzQKMRCJ2bO3A8SVKNuQ78zu2KOqM",
            "nickname": "분양신청"
          },
          "social": {
            "like": 1238,
            "comment": 8,
            "share": 780
          },
          "buttons": [
            {
              "action": "webLink",
              "label": "분양일정",
              "webLinkUrl": "https://www.gh.or.kr/supply/calendar/calendar_list.do"
            },
            {
              "action":  "webLink",
              "label": "분양 알리미 신청",
              "webLinkUrl": "https://www.gh.or.kr/info_sms/application.do"
            }
          ]
        }
      }
    ]
  }
}
    return res

@application.route("/Permission_01", methods=['POST','GET'])
def Permission_01():

    req = request.get_json()
    print(req)
    res = {
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "basicCard": {
          "title": "청약신청",
          "thumbnail": {
            "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
          },
          "profile": {
            "imageUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4BJ9LU4Ikr_EvZLmijfcjzQKMRCJ2bO3A8SVKNuQ78zu2KOqM",
            "nickname": "청약신청"
          },
          "social": {
            "like": 1238,
            "comment": 8,
            "share": 780
          },
          "buttons": [
            {
              "action":  "webLink",
              "label": "신청하러 가기",
              "webLinkUrl": "https://www.applyhome.co.kr/co/coa/selectMainView.do"
            }
          ]
        }
      }
    ]
  }
}
    return res

@application.route("/news1", methods=['POST', 'GET'])
def news1():
    req = request.get_json()  
    print(req)
    res = {
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "listCard": {
          "header": {
            "title": "부동산 뉴스"
          },
          "items": [
            {
              "title": "주택관련",
              "description": "최신 주택관련 뉴스",
              "link": {
                "web": "https://search.naver.com/search.naver?                           sm=tab_hty.top&where=news&query=%EB%B6%80%EB%8F%99%EC%82%B0+%EC%A3%BC%ED%83%9D&oquery=%EC%A3%BC%ED%83%9D&tqi=hi8XSsprvh8ssOEue9lssssssTl-235484"
              }
            },
            {
              "title": "청약관련",
              "description": "최신 청약관련 뉴스 ",
              "link": {
                "web": "https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%EB%B6%80%EB%8F%99%EC%82%B0+%EC%B2%AD%EC%95%BD&oquery=%EB%B6%80%EB%8F%99%EC%82%B0+%EC%A3%BC%ED%83%9D&tqi=hi8XTsprvhGssRWhllsssssstE8-359188"
              }
            },
          ],
          "buttons": [
            {
              "label": "전체 뉴스보기",
              "action": "webLink",
              "webLinkUrl": "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EB%B6%80%EB%8F%99%EC%82%B0"
            }
          ]
        }
      }
    ]
  }
 }
    return res

# 임차가구 자가진단 계산기
class Calaulator:
    def isConfirm(famNumber, revenu):
        if famNumber == 1 and revenu > 548349:
            return False
        elif famNumber == 2 and revenu > 926424:
            return False
        elif famNumber == 3 and revenu > 1195185:
            return False
        elif famNumber == 4 and revenu > 1462887:
            return False
        elif famNumber == 5 and revenu > 1727212:
            return False
        elif famNumber == 6 and revenu > 1988581:
            return False
        else:
            return True;
    def GetSupportAmount_Imcha(famNumber, district):
        dType = Calaulator.GetDistrictType(district)
        #서울 유형
        if famNumber == 1:
            return 310000
        if famNumber == 2:
            return 348000
        if famNumber == 3:
            return 414000
        if famNumber == 4:
            return 480000
        if famNumber == 5:
            return 497000
        if famNumber == 6:
            return 588000
            
            
    # 도시 지정
    def GetDistrictType(district):
        dType = "Seoul"
        return dType
        
# Enum
@application.route("/DataTest", methods=['POST', 'GET'])
def Start():
    content = request.get_json()

    content = content['action']
    params = content['params']
    param1 = params['inf_answer']
    
    userString = param1
    
    url = "	https://openapi.naver.com/v1/search/local.json"
    clientId = "cl6pp7a4QRobYp9K7e6z"
    clientSecret = "NJeUbiGR8x"
    
    characters = "<b>"
    characters2 = "</b>"

    
    queryString = "?query=" + userString + "경찰서"
    headers = {
        "X-Naver-Client-Id":clientId,
        "X-Naver-Client-Secret":clientSecret
    }
    r = requests.get(url + queryString, headers = headers).json()
    r1_1 = r["items"][0]["title"]
    for x in range(len(characters)):
        r1_1 = r1_1.replace(characters[x],"")
    for x in range(len(characters2)):
        r1_1 = r1_1.replace(characters2[x],"")
    
    queryString = "?query=" + userString + "역"
    
    r2 = requests.get(url + queryString, headers = headers).json()
    
    r2_1 = r2["items"][0]["title"]
    for x in range(len(characters)):
        r2_1 = r2_1.replace(characters[x],"")
    for x in range(len(characters2)):
        r2_1 = r2_1.replace(characters2[x],"")
        
    queryString = "?query=" + userString + "우체국"
    
    r3 = requests.get(url + queryString, headers = headers).json()
    
    r3_1 = r3["items"][0]["title"]
    for x in range(len(characters)):
        r3_1 = r3_1.replace(characters[x],"")
    for x in range(len(characters2)):
        r3_1 = r3_1.replace(characters2[x],"")
    
    datasend = {
      "version": "2.0",
      "template": {
        "outputs": [
          {
            "listCard": {
              "header": {
                "title": "다음 공공 시설이 설치되어 있습니다"
              },
              "items": [
                {
                  "title": r2_1,
                  "description": r2["items"][0]["address"],
                  "imageUrl": "http://k.kakaocdn.net/dn/APR96/btqqH7zLanY/kD5mIPX7TdD2NAxgP29cC0/1x1.jpg",
                  "link": {
                    "web": "https://namu.wiki/w/%EB%9D%BC%EC%9D%B4%EC%96%B8(%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%94%84%EB%A0%8C%EC%A6%88)"
                  }
                },
                {
                  "title": r1_1,
                  "description": r["items"][0]["address"],
                  "imageUrl": "http://k.kakaocdn.net/dn/N4Epz/btqqHCfF5II/a3kMRckYml1NLPEo7nqTmK/1x1.jpg",
                  "link": {
                    "web": "https://namu.wiki/w/%EB%AC%B4%EC%A7%80(%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%94%84%EB%A0%8C%EC%A6%88)"
                  }
                },
                {
                  "title": r3_1,
                  "description": r3["items"][0]["address"],
                  "imageUrl": "http://k.kakaocdn.net/dn/bE8AKO/btqqFHI6vDQ/mWZGNbLIOlTv3oVF1gzXKK/1x1.jpg",
                  "link": {
                    "web": "https://namu.wiki/w/%EC%96%B4%ED%94%BC%EC%B9%98"
                  }
                }
              ],
              "buttons": [
                {
                  "label": "자세히 알아보기",
                  "action": "webLink",
                  "webLinkUrl": "https://www.myhome.go.kr/hws/portal/cont/selectContHousingView.do#guide=HB003"
                }
              ]
            }
          }
        ]
      }
    }
    return jsonify(datasend)


# 자가진단 정보 확인용
@application.route("/AskInformation", methods=['POST', 'GET'])
def AskInfor():
    content = request.get_json()

    content = content['contexts']
    content = content[0]
    params = content['params']
    param1 = params['inf_district']
    param1 = param1['value']
    
    param2 = params['inf_familyNumber']
    param2 = param2['value']
    

    
    datasend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type" : "basicCard",
                            "items": [
                                {
                                    "title" : "",
                                    "description" : "해당사항 입니다 지역명 : %s 가구수 : %s 소득인정액 : %s" % (param1, param2, param3)
                                }
                            ]
                        }
                    }
                ]
            },

    }
    return jsonify(datasend)

# 임차가구용 자가 진단
@application.route("/jindan", methods=['POST', 'GET'])
def Message3():
    content = request.get_json()

    content = content['action']
    params = content['params']
    param1 = params['inf_district']
    param2 = params['inf_familyNumber']
    param3 = params['inf_revenu']
    param4 = literal_eval(param3)
    
    param2 = param2[0:1]
    param2 = int(param2)
    param3 = int(param4['amount'])

    confirm = Calaulator.isConfirm(param2, param3)
    if confirm == False:
        datasend = {
          "version": "2.0",
          "template": {
            "outputs": [
              {
                "basicCard": {
                  "title": "주거급여",
                  "description" : "주거급여 신청 자격에 해당하지 않아요!",
                  "thumbnail": {
                    "imageUrl": "https://img.etoday.co.kr/pto_db/2020/12/600/20201201113104_1548009_832_342.PNG"
                  },
                  "profile": {
                    "imageUrl": "https://www.myhome.go.kr/hws/portal/cont/selectContHousingView.do#guide=HB001",
                    "nickname": "보물상자"
                  },
                  "social": {
                    "like": 1238,
                    "comment": 8,
                    "share": 780
                  },
                  "buttons": [
                    {
                      "action":  "webLink",
                      "label": "자세한 사항 보러가기",
                      "webLinkUrl": "https://www.myhome.go.kr/hws/portal/cont/selectContHousingView.do#guide=HB001"
                    }
                  ]
                }
              }
            ]
          }
        }
        return jsonify(datasend)
    
    supportAmount = Calaulator.GetSupportAmount_Imcha(param2, param1)
    
    supportAmount = str(supportAmount)
    
    supportAmount1 = supportAmount[-4:]
    supportAmount2 = supportAmount[:-4]
    datasend = {
      "version": "2.0",
      "template": {
        "outputs": [
          {
            "basicCard": {
              "title": "주거급여",
              "description" : "최대 %s만%s원 지원받을 수 있습니다" % (supportAmount2, supportAmount1),
              "thumbnail": {
                "imageUrl": "https://img.etoday.co.kr/pto_db/2020/12/600/20201201113104_1548009_832_342.PNG"
              },
              "profile": {
                "imageUrl": "https://www.myhome.go.kr/hws/portal/cont/selectContHousingView.do#guide=HB001",
                "nickname": "보물상자"
              },
              "social": {
                "like": 1238,
                "comment": 8,
                "share": 780
              },
              "buttons": [
                {
                  "action":  "webLink",
                  "label": "지원 신청하러 가기",
                  "webLinkUrl": "https://www.myhome.go.kr/hws/portal/cont/selectContHousingView.do#guide=HB001"
                }
              ]
            }
          }
        ]
      }
    }
    return jsonify(datasend)

# 지가가구용 자가 진단
@application.route("/jagagaguJindan", methods=['POST', 'GET'])
def JindaanJagagagu():
    content = request.get_json()

    content = content['action']
    params = content['params']
    pFamilyNumber = params['inf_familyNumber']
    pRevenu = params['inf_revenu']
    param4 = literal_eval(pRevenu)
    pHasDisabled = params['inf_hasDisabled']
    pIsPermission = params['inf_isPermission']
    
    
    pFamilyNumber = pFamilyNumber[0:1]
    pFamilyNumber = int(pFamilyNumber)
    pRevenu = int(param4['amount'])
    
    confirm = Calaulator.isConfirm(pFamilyNumber, pRevenu)

    # 'familyNumber' 'revenu'-'amount' 'hasDisabled' 'isPermission'
    # 'amount' , 'familyNumber' 를 이용하여 생계급여 기준 확인
    # 어차피 대부분 현장 조사를 통해서 지급한다고 쓰면 된다
    # hasDisabled 가 true 인 경우에 추가 380만원(편의시설 설치) 지원 가능하다고 글로 표시
    # isPermission 이 false면 전부다 취소, true면 무시
    if pHasDisabled == "False":
        hasDisabled = False
    elif pHasDisabled == "True":
        hasDisabled = True;
    
    if pIsPermission == "False":
        permission = False;
    elif pIsPermission == "True":
        permission = True;
        
    if confirm == False or permission == False:
        datasend = {
          "version": "2.0",
          "template": {
            "outputs": [
              {
                "basicCard": {
                  "title": "신청 대상자가 아니에요!",
                  "description": "",
                  "thumbnail": {
                    "imageUrl": "https://1.bp.blogspot.com/-1hB1ehZcePM/Vw-VbmphMII/AAAAAAAAJOo/UnBUCm4fM3wTFlWLLRLqs1GASqj1UbmdgCLcB/s1600/Fail-emoticon.png"
                  },
                  "profile": {
                    "imageUrl": "https://1.bp.blogspot.com/-1hB1ehZcePM/Vw-VbmphMII/AAAAAAAAJOo/UnBUCm4fM3wTFlWLLRLqs1GASqj1UbmdgCLcB/s1600/Fail-emoticon.png",
                    "nickname": "보물상자"
                  },
                  "social": {
                    "like": 1238,
                    "comment": 8,
                    "share": 780
                  },
                }
              }
            ]
          }
        }
        return jsonify(datasend)
    
        
    datasend = {
      "version": "2.0",
      "template": {
        "outputs": [
          {
            "listCard": {
              "header": {
                "title": "다음중 한가지의 혜택을 받을 수 있어요!"
              },
              "items": [
                {
                  "title": "대보수",
                  "description": "7년 주기 1,241만원 한도",
                  "imageUrl": "http://k.kakaocdn.net/dn/APR96/btqqH7zLanY/kD5mIPX7TdD2NAxgP29cC0/1x1.jpg",
                  "link": {
                    "web": "https://namu.wiki/w/%EB%9D%BC%EC%9D%B4%EC%96%B8(%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%94%84%EB%A0%8C%EC%A6%88)"
                  }
                },
                {
                  "title": "중보수",
                  "description": "5년 주기 849만원 한도",
                  "imageUrl": "http://k.kakaocdn.net/dn/N4Epz/btqqHCfF5II/a3kMRckYml1NLPEo7nqTmK/1x1.jpg",
                  "link": {
                    "web": "https://namu.wiki/w/%EB%AC%B4%EC%A7%80(%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%94%84%EB%A0%8C%EC%A6%88)"
                  }
                },
                {
                  "title": "경보수",
                  "description": "3년 주기 457만원 한도",
                  "imageUrl": "http://k.kakaocdn.net/dn/bE8AKO/btqqFHI6vDQ/mWZGNbLIOlTv3oVF1gzXKK/1x1.jpg",
                  "link": {
                    "web": "https://namu.wiki/w/%EC%96%B4%ED%94%BC%EC%B9%98"
                  }
                }
              ],
              "buttons": [
                {
                  "label": "신청하기",
                  "action": "webLink",
                  "webLinkUrl": "https://www.myhome.go.kr/hws/portal/cont/selectContHousingView.do#guide=HB003"
                }
              ]
            }
          }
        ]
      }
    }
    return jsonify(datasend)


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=80)
