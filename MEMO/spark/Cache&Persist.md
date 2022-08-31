## Cache & Persist

처음 Spark를 사용했던 프로젝트는 방대한 양의 금융데이터를 중복 연산해야하는 프로젝트였다. 데이터가 방대하다보니 초기 데이터를 로드하는 데만 해도 시간이 꽤 소요돼었다. 그때 Cache & Persist를 이용해 총 수행시간을 절약할 수 있었다.

### Cache & Persist란?
- 데이터를 다루는 작업은 필연적으로 task가 반복되는 경우가 잦음.
- Spark의 지연되는 연산은 데이터를 메모리에 저장해둘 수 있어 유용. 이때 사용되는 것이 cache와 persist다.

1. cache
- 디폴트 Storage Level을 사용
- RDD : MEMORY_ONLY / DF : MEMORY_AND_DISK

2. Persist
- Storage Level을 사용자가 원하는대로 지정 가능

```Python
    # cache()를 통해 categoryReviews 연산은 1번만 수행
    categoryReviews = filtered_lines.map(parse).cache()

    result1 = categoryReviews.take(10)
    result2 = categoryReviews.mapValues(lambda x: (x,1))

    # persist()
    from pyspark import StorageLevel
    categoryReviews = filtered_lines.map(parse).persist(StorageLevel.MEMORY_AND_DISK)
```

### Storage Level
 1. MEMORY_ONLY
 2. MEMORY_AND_DISK
 3. MEMORY_ONLY_SER
 4. MEMORY_AND_DISK_SER
 5. DISK_ONLY
   
** serialized 형태로 변환해서 저장해 저장 용량을 아낄 수 있지만 데이터 read시 재변환 연산을 수행해야함.  

