# セットアップ
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

# 開発
## 実行
```bash
uvicorn app.main:app --reload
```

## test
```bash
curl http://127.0.0.1:8000/my_root/v1/

# OK
curl -X POST "http://127.0.0.1:8000/my_root/v1/sample/2" \
    -H "Content-Type: application/json" \
    -d '{
      "user": "Fast APIから送信しました",
      "mystatus": "本文です"
    }'

# error
curl -X POST "http://127.0.0.1:8000/my_root/v1/sample/2" \
    -H "Content-Type: application/json" \
    -d '{
      "user": "a",
      "mystatus": "本文です"
    }'

# error
curl -X POST "http://127.0.0.1:8000/my_root/v1/sample/2" \
    -H "Content-Type: application/json" \
    -d '{
      "user": "b",
      "mystatus": "本文です"
    }'

# error
curl -X POST "http://127.0.0.1:8000/my_root/v1/sample/2" \
    -H "Content-Type: application/json" \
    -d '{
      "user": "Fast APIから送信しました",
      "mystatus_1": "本文です"
    }'
```

# ディレクトリ構成
FastAPIのディレクトリ構成におけるベストプラクティスは、コードの可読性やメンテナンス性を向上させ、機能ごとに役割を分割することで大規模なプロジェクトでも管理しやすくすることです。一般的なディレクトリ構成は次のようになります：

```
my_fastapi_project/
├── app/
│   ├── api/                # エンドポイント（ルーター）のディレクトリ
│   │   ├── v1/
│   │   │   ├── endpoints/  # 個別のエンドポイントファイル
│   │   │   │   ├── user.py # 例: ユーザー関連のエンドポイント
│   │   │   │   ├── item.py # 例: アイテム関連のエンドポイント
│   │   │   └── __init__.py
│   ├── core/               # 設定や重要なロジック（例: 認証設定）
│   │   ├── config.py       # 設定ファイル
│   │   ├── security.py     # セキュリティ関連の設定や認証処理
│   │   └── __init__.py
│   ├── models/             # データベースモデル（SQLAlchemyなど）
│   │   ├── user.py         # 例: ユーザーモデル
│   │   ├── item.py         # 例: アイテムモデル
│   │   └── __init__.py
│   ├── schemas/            # データバリデーションやリクエスト/レスポンスのスキーマ
│   │   ├── user.py         # 例: ユーザー関連のスキーマ
│   │   ├── item.py         # 例: アイテム関連のスキーマ
│   │   └── __init__.py
│   ├── services/           # ビジネスロジック（アプリケーションのサービス層）
│   │   ├── user_service.py # 例: ユーザー関連のビジネスロジック
│   │   ├── item_service.py # 例: アイテム関連のビジネスロジック
│   │   └── __init__.py
│   ├── db/                 # データベース接続や設定
│   │   ├── base.py         # モデルのベース設定
│   │   ├── session.py      # DBセッションの設定
│   │   └── __init__.py
│   ├── tests/              # テストディレクトリ
│   │   ├── test_user.py    # 例: ユーザー関連のテスト
│   │   └── test_item.py    # 例: アイテム関連のテスト
│   ├── utils/              # ヘルパー関数やユーティリティ関数
│   │   ├── helpers.py
│   │   └── __init__.py
│   ├── main.py             # アプリケーションのエントリーポイント
│   └── __init__.py
├── .env                    # 環境変数ファイル
├── requirements.txt        # Pythonの依存パッケージ
└── Dockerfile              # Dockerの設定ファイル（必要に応じて）
```

### 各ディレクトリの役割

- **api**：エンドポイントに関するコードを格納し、APIのルート設定を管理します。バージョニング（例: v1）でバージョン管理することが多いです。
  
- **core**：アプリケーションの設定や主要な構成を行う場所です。ここにはアプリ全体で使用する設定や認証・認可ロジックなどが含まれます。

- **models**：データベースのテーブルやコレクションのスキーマを定義するデータベースモデルを格納します。

- **schemas**：Pydanticを使用して、リクエストおよびレスポンスのスキーマを定義します。これにより、データのバリデーションとシリアライズが行えます。

- **services**：ビジネスロジックを分離して管理するためのディレクトリです。例えば、ユーザー作成やアイテムの処理など、データベースアクセスや処理をここに実装します。

- **db**：データベース接続の設定や、セッションの生成に関連するコードを格納します。

- **tests**：テストコードを配置するディレクトリです。各機能ごとに単体テストや統合テストを実装します。

- **utils**：小規模の補助関数や、再利用可能なロジックを格納します。

### 補足
FastAPIのプロジェクト構成では、各ファイルに適切な役割を割り当ててコードを整理することで、開発者間での理解を促進し、コードの保守性やテストの容易さを向上させます。