1.처음 백조의 위치를 저장해둔다
2. 물인 공간에 번호를 매기고 백조정보에 현재 백조가 몇번 물에 있는지 저장하고 얼음 덩어리에 가장자리를 찾아 edges 큐에 저장한다.
for( 반복문 시작 )
  if 두 백조가 같은 번호에 있는지 체크
     같다면 시간 출력 후 종료
  else 얼음 녹이기
    if edges 길이만큼 반복문 시작
       if 4방향 탐색
         1) if  얼음이고 처음 방문한 얼음이라면 edges에 push
         2) else 물이라면 주변 물중 가장 큰 물의 번호 저장
       else 물 영역 합치기 시작
	        1) 해당 점을 기준으로 물 영역 번호를 수정한다
          2) 만약 백조가 있는 위치라면 해당 백조의 물 번호 수정