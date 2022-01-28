<br>

# 👻 Errovler : KT 에이블 스쿨만의 "에러 게시판"
> 2022.01.17 ~ 2022.01.28 KT AIVLE 전남/전북 1조 미니프로젝트<br>
>  *'에러블러'는 수업 중 생긴 에러를 질문해서 함께 해결하고, 자신이 해결한 에러들을 공유해 에이블러들과 함께 공부하는데 목적을 가진 에러 보관소(Archive)입니다*

<br>

[1. 개발 배경 및 목적](#1-개발-배경-및-목적)

[2. 기능](#2-기능)

[3. DB 설계](#3-DB-설계)

[4. 개발 환경](#4-개발-환경)

[5. 개발 일정](#5-개발-일정)

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
<details>
  <summary>메인 화면</summary>
   <div markdown="1">       
     <br>
     <img src="https://user-images.githubusercontent.com/68097036/151487284-f73137b0-cb68-4736-9f39-62debfca2c1c.gif" width="740" height="412">
     <br>
     <text>⇒ '오늘 강의' 및 '내일 강의', '오늘의 명언'을 슬라이드 형식으로 볼 수 있도록 구현</text>
   </div>
 </details>

 <details>
    <summary><strong>1) KT 에이블 스쿨을 위한 프라이빗 게시판 (회원가입/로그인)</strong></summary>
        <div markdown="1">  
            <h3>📝 회원가입</h3>
            <img src="https://user-images.githubusercontent.com/68097036/151476280-fa1be845-2609-4f46-8d2a-2bf76c716362.png" width="700" height="480">
            <img src="https://user-images.githubusercontent.com/68097036/151476799-b9fa00de-3360-4092-a47b-a75dcf2ed162.png" width="700" height="480">
            <h3>🔓 로그인</h3>
            <img src="https://user-images.githubusercontent.com/68097036/151479107-4c444093-9c6f-4b36-8eea-98dcedc7f239.png" width="550" height="380">
            <h3>🔒 로그아웃</h3>
            <img src="https://user-images.githubusercontent.com/68097036/151486411-5dbd0ecb-06c8-4b67-ad97-94658a553d86.png" width="700" height="60">
        </div>
</details>
 
 <details>
  <summary><strong>2) 지금 가장 인기 있는 게시물을 한 눈에 볼 수 있는 기능</strong></summary>
   <div markdown="1"> 
    <br>      
     <img src="https://images.velog.io/images/jiyeah3108/post/cd12159c-60fc-4b99-934e-632cd5fc65bb/image.png" width="700" height="430">
     <br>
     <text>⇒ 조회수를 기준으로 상위 3개의 게시물을 보여준다.</text>
   </div>
 </details>
 
 <details>
  <summary><strong>3) 질문을 할 수 있는 에러 게시판 + 해결한 에러를 공유하는 게시판</strong></summary>
   <div markdown="1">
     <h3>❓ 질문 게시판</h3> 
     <img src="https://images.velog.io/images/jiyeah3108/post/f7fbfd5c-cb17-4d02-bae9-e1532030c9a4/image.png" width="700" height="480">
     <h3>💡 해결 게시판</h3> 
     <img src="https://images.velog.io/images/jiyeah3108/post/7628d0a9-594d-4daf-983b-f3c965a886a0/image.png" width="700" height="480">
     <h3>👀 태그 기능</h3> 
     <img src="https://images.velog.io/images/jiyeah3108/post/931881a1-d99e-4833-94c7-946494ce6efb/%EC%97%90%EB%9F%AC%EB%B8%94%EB%9F%AC%20%E2%80%94%20Board.gif" width="700" height="350">
   </div>
 </details>
 
 <details>
  <summary><strong>4) 궁금한 에러에 대해서 검색할 수 있는 기능</strong></summary>
   <div markdown="1">  
   <br>     
     <img src="https://images.velog.io/images/jiyeah3108/post/9dcc7a1c-7999-4d10-b297-45cc6f27126f/image.png" width="700" height="70">
     <img src="https://images.velog.io/images/jiyeah3108/post/4b4da61e-72eb-4f34-b4d0-f2e91b63a2c5/image.png" width="700" height="440">
     <br>
     <text>⇒ 글 제목, 글 내용, 작성자를 검색하면 그에 대한 검색 결과 반환</text>
   </div>
 </details>
 
 <details>
  <summary><strong>5) 해결/미해결 에러들을 올릴 수 있는 코드에 특화된 글쓰기 (사진 첨부 가능)</strong></summary>
   <div markdown="1">
   <br>
     <img src="https://images.velog.io/images/jiyeah3108/post/44118709-617a-4ec7-998e-ee174e4b2453/image.png" width="700" height="480">
     <img src="https://images.velog.io/images/jiyeah3108/post/493a7888-0d92-4d8f-987b-42f391f6914d/image.png" width="650" height="480">
     <br>
     <text>⇒ 로그인 시 작성 가능 / 질문 & 해결 선택 / 파이썬 & 장고 & 기타 선택</text>
   </div>
 </details>
 
 <details>
  <summary><strong>6) 댓글 및 좋아요와 같은 소통 기능</strong></summary>
   <div markdown="1">  
     <br>
     <img src="https://images.velog.io/images/jiyeah3108/post/57329d5f-0276-4247-8966-cd59f3d3182a/image.png" width="700" height="440">
     <br>
     <text>⇒ 초기 : 빈 하트, 빈 스크랩 아이콘</text>
     <br>
     <br>
     <img src="https://images.velog.io/images/jiyeah3108/post/b42b3d01-0d69-4398-a61b-31f14a079d45/image.png" width="700" height="420">
     <br>
     <text>⇒ 클릭 시 아이콘 채워짐</text>
   </div>
 </details>
 
 <details>
  <summary><strong>7) 특히! 도움이 되는 에러글을 스크랩 할 수 있는 기능 (마이페이지)</strong></summary>
   <div markdown="1">    
     <br>
     <img src="https://images.velog.io/images/jiyeah3108/post/e39a79df-65d2-434a-95cb-dcf1e4bb0e8b/image.png" width="700" height="440">
     <br>
     <text>⇒앞서 스크랩한 게시물 마이페이지에서 확인 가능</text>
     <h3>✏ 프로필 수정</h3>
     <img src="https://images.velog.io/images/jiyeah3108/post/cdefdcd4-15a2-4a25-a88c-7b8c8e58e7c3/image.png" width="390" height="440">
     <img src="https://images.velog.io/images/jiyeah3108/post/6ca4b8cf-dd92-43f6-a86f-c978104707a6/image.png" width="390" height="440">
     <img src="https://images.velog.io/images/jiyeah3108/post/c145c4b5-6901-4683-9b5c-447efe8ce313/image.png" width="600" height="240">
     <br>
   </div>
 </details>
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

## 5. 개발 일정

![image](https://user-images.githubusercontent.com/68097036/151492506-e5197cbe-d619-42e4-be5b-0196cbff3abb.png)
