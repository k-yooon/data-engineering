## SPARK란?

### 메모리 계층 구조
```
CPU
L1 캐시
L2 캐시
L3 캐시
RAM
HDD/SSD
```
 - 연산을 시작하면 하드디스크에서 CPU까지 데이터가 위로 이동
 - 연산에 자주 쓰이는 데이터는 위로, 자주 쓰이지 않는 데이터는 아래로
 - spark는 여러 노드에 분산 저장을 통해 in-memory 연산이 가능하도록 함.

### SPARK 특징
1. in-memory 연산이 가능
2. Hadoop MapReduce보다 메모리 상에선 100배, 디스크 상에선 10배가 빠름
3. Transform + Action 으로 구성
4. 태스크를 정의할 때는 연산을 하지 않다가 결과가 필요할 때 연산 수행

### SPARK 객체
1. SparkConf
- 사용자가 재정의해서 쓸 수 있는 설정 옵션들에 대한 키와 값을 갖고있는 객체
2. SparkContext
- Spark 클러스터와 연결시켜주는 객체
- Spark 모든 기능에 접근할 수 있는 시작점
- Spark는 분산환경에서 동작하기 때문에 Driver Program을 구동시키기 위해 SparkContext가 필요
- SparkContext는 프로그램당 하나만 만들 수 있고 사용 후에는 종료








