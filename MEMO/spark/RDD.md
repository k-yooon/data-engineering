## RDD

### RDD 특징
1. 추상화
- 클러스터에 흩어져 있지만 하나의 파일인 것처럼 사용이 가능하다.
2. Resilient & Immutable(탄력적이고 불변)
- 데이터 장애 시, 복원이 가능
- Immutable 
    - RDD1이 변환을 거치면 RDD1이 바뀌는게 아니라 새로운 RDD2가 만들어짐
     - 변환을 거칠때마다 연산의 기록이 남음, 때문에 문제가 생길 경우 쉽게 전 RDD로 돌아갈 수 있음
3. Type-safe
- 컴파일시, Type을 판별할 수 있어 문제를 일찍 발견할 수 있다.
4. Structured / UnStructured Data
-  Structured / UnStructured Data 둘 다 담을 수 있다.
5. Lazy Evaluation
- 액션을 할때까지 변환은 실행되지 않는다.

### RDD 장점
1. 유연성
2. 짧은 코드로 할 수 있는게 많다.