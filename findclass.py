import webbrowser

Edulocate = ['서울특별시', '인천광역시', '울산광역시', '강원도', '전라북도', '전라남도', '경상북도', '경상남도', '제주특별자치도', '부산광역시', '대구광역시', '광주광역시', '대전광역시', '세종특별자치시', '경기도', '충청북도', '충청남도']
EduUrl = ["sen", "ice", "use", "kwe", "jbe", "jne", "gbe", "gne", "jje", "pen", "dge", "gen", "dje", "sje", "goe", "cbe", "cne"]


def whichEduSite():
    print("해당하는 교육청을 정확히 적으세요.")
    Edulocateinput = input()
    if Edulocateinput in Edulocate:
        for i in range(17):
            if Edulocateinput == Edulocate[i]:
                url = EduUrl[i]  
            print("학생이신가요, 학부모이신가요?")
            whour = input()
            if whour == '학생':link = "https://stu." + url + ".go.kr/"
            elif whour == "학부모":link = "https://par]." + url + ".go.kr/"
            webbrowser.open(link)
    else:
        print("일치하는 교육청이 없습니다..\n다시", end=" ")
        whichEduSite()

whichEduSite()

