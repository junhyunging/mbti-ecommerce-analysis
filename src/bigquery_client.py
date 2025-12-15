import os
from google.cloud import bigquery

def get_bq_client():
    print("GOOGLE_APPLICATION_CREDENTIALS =", os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))
    client = bigquery.Client()
    return client

if __name__ == "__main__":
    # 클라이언트 생성
    client = get_bq_client()

    # BigQuery 연결 테스트
    print("\nBigQuery 연결 테스트 중...\n")

    datasets = list(client.list_datasets())
    if datasets:
        print("연결 성공! 데이터셋 목록:")
        for ds in datasets:
            print(" -", ds.dataset_id)
