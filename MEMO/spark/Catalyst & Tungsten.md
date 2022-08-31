## Catalyst & Tungsten

스파크 SQL는 쿼리를 돌리기 위해 두가지 엔진을 사용한다. Catalyst & Tungsten

### Catalyst
- 스파크 SQL의 질의 옵티마이저로 Logical Plan을 Physical Plan으로 바꾸는 일을 수행

    #### Logical Plan이란?
    - 수행해야하는 모든 transformation 단계에 대한 추상화
    - 데이터가 어떻게 변해야 하는지 정의하지만 실제 어디서 어떻게 동작 하는지는 정의하지 않음.

    #### Physical Plan이란?
    - Logical Plan이 어떻게 클러스터 위에서 실행될지 정의
    - 실행 전략을 만들고 Cost Model에 따라 최적화

    #### Catalyst의 실행 순서
    1. 분석 
    - DataFrame 객체의 relation을 계산, 컬럼의 타입과 이름을 확인
    1. Logical Plan 최적화
     - 상수로 표현된 표현식을 compile time에 계산 (runtime 시 계산하지 않고)
     - Predicate Pushdown : join & filter -> filter & join 
     - Project Pruning : 연산에 필요한 컬럼만 가져오기 
    2. Physical Plan 만들기
    - 스파크에서 실행 가능한 Plan으로 변환
    1. 코드 제너레이션
    - 최적화도니 Physical Plan을 Java Bytecode로 변환
    
    +++ catalyst pipeline  사진 추가 

### Explain
```python
    spark.sql(query).explain(True)
```

1. Parsed Logical Plan 
2. Analyzed Logical Plan 
3. Optimized Logical Plan 
4. Physical Plan
  
### Tungsten
- Physical Plan이 선택되고 나면 분산환경에서 실행된 Bytecode가 만들어짐(코드 제너레이션)
- 스파크 엔진의 성능 향상이 목적
- 메모리 최적화 / 캐시 활용 연산 / 코드 생성

