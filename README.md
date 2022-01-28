<br>

# 👻 Errovler : KT 에이블 스쿨만의 "에러 게시판"
> 2022.01.17 ~ 2022.01.28 KT AIVLE 전남/전북 1조 미니프로젝트<br>
>  *'에러블러'는 수업 중 생긴 에러를 질문해서 함께 해결하고, 자신이 해결한 에러들을 공유해 에이블러들과 함께 공부하는데 목적을 가진 에러 보관소(Archive)입니다*

<br>

[1. 개발 배경 및 목적](#1.-개발-배경-및-목적)

[2. 기능](#2.-기능)

[3. DB 설계](#3.-DB-설계)

[4. 개발 환경](#4.-개발-환경)

[5. 일정](#5.-일정)

<br>

***

<br>

## 1. 개발 배경 및 목적
> 💡 KT 에이블 스쿨 교육을 들으면서 강사님께서 에러를 잘 정리 해놓는 습관에 대한 중요성을 강조하신 것에서 아이디어를 얻음. 수업 중 생기는 에러를 올려서 함께 해결하고, 해결된 에러들을 따로 정리하지 않아도 수집해서 서로 공유하고 공부하는데 목적을 가진 게시판을 만들기로 함.
즉, **에러의, 에러의 의한, 에러를 위한 게시판!**

<br>

- KT AIVLE 강의를 진행하면서 실습 하나하나에 여러가지 에러 발생

<br>

- `기존 AIVLE 강의장`
  - **채팅**
    - 모든 교육생들이 볼 수 있음
    - 한 눈에 보기 힘들고, 강사님이 자주 더 자세한 상황을 설명해줄 수 있냐고 물어보는 것을 볼 수 있음
    - 무엇보다 코드를 보기 쉽지 않음
  - **1:1 질문**
    - 다른 교육생들은 볼 수 없음
 
<br>

- 위와 같은 사항을 **보완**하기 위해 **에러 게시판**(에러블러)를 기획

<br>

- `에러블러`
  - 모든 교육생들이 볼 수 있음 (KT 에이블러만을 위한 공간)
  - 발생한 에러나 해결한 에러를 게시글로 올림으로써 교육생들이 기존보다 더 수월하게 에러를 해결할 수 있음
  - 한 눈에 보기 쉬움
  - 실습 진행이 조금 더 평이하게 흘러갈 수 있을 것으로 예상

<br>


<br>

## 2. 기능
- **KT 에이블 스쿨**을 위한 프라이빗 게시판 (회원가입/로그인)
- 지금 가장 **인기 있는 게시물**을 한 눈에 볼 수 있는 기능
- 질문을 할 수 있는 **에러 게시판 + 해결한 에러**를 공유하는 게시판
- 궁금한 에러에 대해서 **검색**할 수 있는 기능
- 해결/미해결 에러들을 올릴 수 있는 **코딩에 특화** 된 글쓰기 (사진 첨부 가능)
- 댓글 및 좋아요와 같은 **소통** 기능
- 특히! 도움이 되는 에러글을 **스크랩** 할 수 있는 기능(마이페이지)

<br>


<br>

## 3. DB 설계
  - `ERD`

![erd](https://user-images.githubusercontent.com/68097036/151470133-5dee929a-36bd-456c-95ec-5d5dc8c48559.png)


<br>


<br>

## 4. 개발 환경

- `Front-End`

  |HTML|CSS|JS|Bootstrap|
  |:---:|:---:|:---:|:---:|
  |![html](https://user-images.githubusercontent.com/68097036/151471705-99458ff8-186c-435b-ac5c-f348fd836e40.png)|![css](https://user-images.githubusercontent.com/68097036/151471805-14e89a94-59e8-468f-8192-c10746b93896.png)|![js](https://user-images.githubusercontent.com/68097036/151471854-e0134a79-b7ef-4a0f-99fd-53e8ee5baf50.png)|![bootstrap](https://user-images.githubusercontent.com/68097036/151480381-2b23a8af-c6b4-43a6-96a6-ea69e0b953e0.png)|


- `Back-End`

  |Python|Django|MySQL|HeidiSQL|
  |:---:|:---:|:---:|:---:|
  |![pngwing com](https://user-images.githubusercontent.com/68097036/151479684-a85d26d4-e79e-47c9-9023-bf6d92f57536.png)|![pngwing com (1)](https://user-images.githubusercontent.com/68097036/151466729-9cad0405-85ad-454e-815a-1a4fd065f8b7.png)|![pngwing com (2)](https://user-images.githubusercontent.com/68097036/151466853-2b56fd0f-3aa9-424e-b17b-1c7cd991ffbf.png)|<img src="https://user-images.githubusercontent.com/68097036/151467351-5a359330-8d81-47b9-a33f-f7a5e0d69319.png" width="120" height="120">|

- `Etc`

  |Summernote|VS Code|Microsoft Teams|GitHub|Notion|
  |:---:|:---:|:---:|:---:|:---:|
  |![brand_summernote_icon_157332](https://user-images.githubusercontent.com/68097036/151470431-2b196263-3c3f-425d-8fd0-0d6cf440e3d1.png)|<img src="https://user-images.githubusercontent.com/68097036/151479933-01785e34-1283-4fca-a407-9fe284b50fa8.png" width="220" height="100">|![pngwing com (4)](https://user-images.githubusercontent.com/68097036/151467837-2cd89acd-2a92-45dd-b06b-e08e316b7695.png)|<img src="https://user-images.githubusercontent.com/68097036/151467910-0fda00cd-c08b-4869-a21e-a66d1d133ff5.png" width="220" height="100">|<img src="https://user-images.githubusercontent.com/68097036/151468186-82e630d3-8c3c-4c75-8243-e1efcba34926.png" width="220" height="130">|

<br>

<br>

## 5. 일정

![일정표](https://user-images.githubusercontent.com/43737828/150968173-8d975fd9-92e6-4762-9fac-75f87e5ec995.png)
