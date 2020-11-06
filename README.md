# Bammlier
## [한국어 명사] Baristar와 Sommelier의 합성어로서 커피 취향을 분석하여 와인을 추천해주는 사람.

![A Trick For Choosing Wine _ A Cup of Jo](https://user-images.githubusercontent.com/68367134/98342226-77d8bf80-2053-11eb-8b25-58d33e9093a0.jpeg)

<문제 인식>
## 매일 아침 마시는 커피로 오늘 밤 당신의 와인을 찾아드려요 🍷
당신에게 와인은 여전히 어렵기만 한가요?
매일 아침 바디감이 풍부한 플랫화이트를 마시고 나른한 오후에는 산미있는 롱블랙을 즐기는 당신은 어쩌면 스페인의 '그랑 트레소랏'을 좋아할 수도 있겠네요.
커피 취향은 분명한 당신에게 Bammlier의 추천 시스템으로 최고의 와인을 추천해드릴게요.

## 데이터 크롤링
wine21.com에서 20만원 미만의 레드, 화이트, 로제, 스파클링, 기타(포트, 셰리) 와인

## 데이터 전처리 : 이미지 추가!!!
1. Grape type : 포도 혼합을 사용한 와인은 가장 첫번째 포도 품종으로 분류
2. Food pairing : 같이 먹기 좋은 음식에 언급된 명사를 기반으로 육류(meat), 치즈(cheese), 해산물(seafood), 채소 및 과일(vegetables), 디저트(dessert)로 카테고리화 
3. Aroma : 와인 메이커 노트에 언급된 향을 꽃향(floral), 과일향(fruity), 시트러스향(citrus) 가죽향(oriental_leather), 스파이스향(spice), 흙향(earth)으로 카테고리화
  - 꽃향, 과일향, 시트러스향은 'fruity flavor'으로 가죽향, 스파이스향, 흙향은 'dark flavor'로 추가적으로 2차 분류
  - 메이커 노트에 향에 대해 언급으 없는 와인은 제거
4. Continent : 기존의 유럽과 신대륙으로 나뉘던 대륙을 유럽 a(프랑스, 오스트리아..), 유럽 b(이탈리아, 스페인), 북미(미국, 캐나다), 남미(아르헨티나, 칠레), 신대륙(호주,뉴질랜드,남아프리카), 한국으로 재분류
5. Wine type : 로제, 스파클링 와인은 화이트로, 포트 와인은 레드로 편입하였고 셰리 와인은 제거
6. winery : 테스코 와인은 제거
7. size : 750ml 이외의 모든 사이즈는 제거


<추천 시스템>
## 추천 알고리즘 : Collaborative Filtering
![Screen Shot 2020-11-06 at 18 21 50](https://user-images.githubusercontent.com/68367134/98349196-0b62be00-205d-11eb-92ba-6de9bb622e45.png)

### user based filtering & item based filtering

- user based filtering : 커피 성향이 비슷한 소비자들이 많이 선택한 와인을 1차적으로 선별
- item based filtering : 선별된 와인 중 고객이 와인과 함께 먹을 음식, 선호하는 향과 가격대에서 코사인 유사도 거리가 가장 가까운 와인을 추천



## 평가

<카카오톡 친구>
## 서비스화

