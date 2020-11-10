# Bammlier
## [명사] Barista와 Sommelier의 합성어로서 커피 취향을 분석하여 와인을 추천해주는 챗봇.

![A Trick For Choosing Wine _ A Cup of Jo](https://user-images.githubusercontent.com/68367134/98342226-77d8bf80-2053-11eb-8b25-58d33e9093a0.jpeg)

## 매일 아침 마시는 커피로 오늘 밤 당신의 와인을 찾아드려요 🍷
당신에게 와인은 여전히 어렵기만 한가요?
매일 아침 바디감이 풍부한 플랫화이트를 마시고 나른한 오후에는 산미있는 롱블랙을 즐기는 당신은 어쩌면 스페인의 '그랑 트레소랏'을 좋아할 수도 있겠네요.
커피 취향이 분명한 당신에게 Bammlier가 최고의 와인을 추천해드릴게요.

![Screen Shot 2020-11-09 at 20 21 37](https://user-images.githubusercontent.com/68367134/98535169-0144f780-22c9-11eb-8441-463871219c7a.png)

## 어떤 와인이 가장 마음에 들지 몰라서 다 가져왔어요.

    wine21.com에서 와인 입문자가 즐기기 쉬운 20만원 미만의 레드, 화이트, 로제, 스파클링, 기타(포트, 셰리) 와인을 활용했어요.

1. Filtered data : 와인명칭, 이미지 링크, 알코올도수, 당도, 산도, 바디감, 탄닌감, 푸드페어링, 가격이 없는 데이터는 continue로 데이터프레임으로 받아오지 않음

![스크린샷 2020-11-10 오전 5 26 44](https://user-images.githubusercontent.com/68261338/98592834-9d94eb80-2315-11eb-8766-4bd0fece69ff.png)

2. Maker’s note: 전문가의 와인 후기글. 동일한 와인이지만 빈티지별로 후기를 볼 수 있는 동적 웹페이지는 selenium으로 링크와 함께 크롤링 후 동일한 링크로 기존의 데이터프레임과 결합

![스크린샷 2020-11-10 오전 5 45 26](https://user-images.githubusercontent.com/68261338/98594393-f1a0cf80-2317-11eb-9330-dc3050c88d55.png)

## 당신이 좋아하는 와인만 찾고 싶어서 데이터를 분석했어요.
1. Grape type : 혼합된 포도를 사용한 와인은 가장 첫번째 포도 품종으로 분류 / '부사'로 만들어진 와인은 제거
2. Food pairing : 같이 먹기 좋은 음식에 언급된 명사를 기반으로 육류(meat), 치즈(cheese), 해산물(seafood), 채소 및 과일(vegetables), 디저트(dessert)로 카테고리화 

![Screen Shot 2020-11-09 at 19 38 09](https://user-images.githubusercontent.com/68367134/98534095-5122bf00-22c7-11eb-86a3-5424b1107f95.png)

3. Aroma : 와인 메이커 노트에 언급된 향을 꽃향(floral), 과일향(fruity), 시트러스향(citrus), 스파이스향(spice), 스모키향(oriental_leather), 숲향(earth)으로 카테고리화
    - 꽃향, 과일향, 시트러스향은 'fruity flavor'으로 스파이스향, 스모키향, 흙향은 'dark flavor'로 추가적으로 2차 분류
    - 향에 대해 언급이 없는 와인은 제거
    
![Screen Shot 2020-11-09 at 19 38 38](https://user-images.githubusercontent.com/68367134/98534101-53851900-22c7-11eb-9ad2-042afda6f794.png)

4. Continent : 기존의 유럽과 신대륙으로 나뉘던 대륙을 유럽 a(프랑스, 오스트리아..), 유럽 b(이탈리아, 스페인), 북미(미국, 캐나다), 남미(아르헨티나, 칠레), 신대륙(호주,뉴질랜드,남아프리카), 한국으로 재분류

![Screen Shot 2020-11-09 at 19 39 52](https://user-images.githubusercontent.com/68367134/98534104-54b64600-22c7-11eb-9b4e-ec1c865abe7f.png)
![Screen Shot 2020-11-09 at 19 40 43](https://user-images.githubusercontent.com/68367134/98534106-54b64600-22c7-11eb-9ccc-ce19e61811b0.png)

5. Wine type : 로제, 스파클링 와인은 화이트로, 포트 와인은 레드로 편입하였고 셰리 와인은 제거

![Screen Shot 2020-11-09 at 19 41 06](https://user-images.githubusercontent.com/68367134/98534109-554edc80-22c7-11eb-9f2a-fd35d77576a9.png)

6. Winery : 테스코 와인 제거
7. Size : 750ml 이외의 모든 사이즈는 제거

## Bammlier는 협업 필터링(Collaborative Filtering)을 활용한 와인 추천 챗봇입니다.
![Screen Shot 2020-11-06 at 18 21 50](https://user-images.githubusercontent.com/68367134/98349958-00f4f400-205e-11eb-897a-e5d1edd4523b.png)

### 고객 기반 필터링(User Based Filtering) & 아이템 기반 필터링(Item Based Filtering)
- 고객 기반 필터링 : 커피 성향이 비슷한 소비자들이 많이 선택한 와인을 1차적으로 선별
- 아이템 기반 필터링 : 선별된 와인 중 고객이 와인과 함께 먹을 음식, 선호하는 향과 가격대에서 가장 가까운(코사인 유사도 거리가 가장 가까운) 와인 추천

## 저희의 첫 고객들입니다 ☺️
- 커피 취향별 2,000명의 소비자들이 가장 좋아하는 와인 Best3를 구매한다고 가정하여 가상의 고객들을 만들었어요.
![Screen Shot 2020-11-09 at 19 42 42](https://user-images.githubusercontent.com/68367134/98534113-55e77300-22c7-11eb-9748-a0d16ee372a7.png)

## Bammlier는 당신을 알고 싶어요.
    1. 평소에 어떤 커피를 즐겨 마시나요?
        - 아메리카노
        - 달달한 라떼 
        - 차(tea)
    2. 원두는 어떤 스타일을 선호하시나요?
        - 산미가 강한 타입
        - 바디감이 있는 타입
    3. 오늘은 어떤 음식과 마실건가요?
        - 육류
        - 치즈
        - 해산물
        - 샐러드나 과일
        - 디저트
    4. 어떤 향을 좋아하세요?
        - 꽃향
        - 과일향
        - 시트러스향 
        - 스파이스향
        - 스모키향
        - 숲향
    5. 꼭 비싸지 않아도 괜찮아요 :) (가격대를 넣어주세요.)

## 이제 카카오톡에서 만나요.
@winecoffee 를 카카오톡 친구 추가하여 매일 아침 당신이 마시는 커피를 알려주세요. 오늘 밤 와인 한 잔 할까요?
![vllo (1)](https://user-images.githubusercontent.com/68367134/98549235-da44f080-22dd-11eb-8f47-b672bc455c00.gif)

## Bammlier는 아직 완벽하진 않아요.
- 협업 필터링 추천 시스템은 고객 데이터가 쌓여야만 추천할 수 있는 cold start 문제점이 존재합니다.
- 그러므로 아직은 고객 기반 필터링에서 선별된 와인 중 무작위로 선정된 와인을 우선적으로 추천하지만 여러분의 좋아요가 쌓일 수록 여러분에게 맞는 와인을 추천해드릴거에요.

## Bammlier의 성장 과정
- Bammlier는 욕심이 많은 챗봇이었습니다.😢
    - 데이터베이스에 데이터를 저장하고 AWS로 프로그래밍을 작업하며 카카오톡 오픈빌더를 여러분에게 와인을 직접 추천해드리고 리뷰를 받아 다시 데이터베이스의 업데이트를 하고 싶었죠.
    - 그러나 아직은 제가 태어난지 7일밖에 되지 않아 모든 것을 하기에는 부족한 점이 많았습니다. 
    - 조금만 기다려주세요! 최종적으로 데이터베이스와 연결되어 여러분의 리뷰 하나하나가 저를 더욱 강력한 추천 챗봇으로 만들어주실 수 있도록 열심히 성장하겠습니다!💪
    
    - vino-bot.com에서 이마트 코스트코 롯데 라고 치면 필터처리된 와인상품들을 받아올 수 있어서 실용적인 데이터베이스를 만들고 싶었습니다.
    - 하지만 아로마 그리고 잘 어울리는 음식에 대한 정보가 없어서 사용할 수 없었습니다.
    - 또한, 기존의 와인21 데이터와 와인 명칭이 조금씩 달라서 사용할 수 필터링하기가 까다로웠습니다.
        
        예)"루이 자도 마르사네 루즈" / "루이자도 마르사네 루즈"
        예)"앙드레 끌루에 상파뉴 브뤼 그랑 리저브" / "앙드레 끌루에, 그랑 리저브 브뤼" / "앙드레 끌루에 샹파뉴 브뤼 그랑 리저브"
        
    - HTML과 카카오톡 오픈빌더는 정말...
    - 우리의 마지막 불꽃... 하얗게 불태웠다.
![KakaoTalk_Photo_2020-11-10-11-59-44](https://user-images.githubusercontent.com/68261338/98622199-478f6a80-234c-11eb-84c8-662ff4d3febe.gif)
    


### 프로그래밍 언어
![python](https://user-images.githubusercontent.com/68367134/98533242-0e141c00-22c6-11eb-9d66-2bff894e1d10.png)
![html](https://user-images.githubusercontent.com/68367134/98533239-0ce2ef00-22c6-11eb-9377-77ca745d1546.png)

### 개발 환경
![jupyter notebook (1)](https://user-images.githubusercontent.com/68367134/98533658-9bf00700-22c6-11eb-9b23-7e1c8ed0ed0c.jpeg)
![flask](https://user-images.githubusercontent.com/68367134/98533377-3f8ce780-22c6-11eb-8736-98895c5173f3.png)

### 팀원 구성
이태헌, 강동윤
