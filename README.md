# viora-landing

Viora ティザーランディングページ。静的 HTML/CSS（ビルド不要）。

## ローカル確認

```bash
docker compose up -d
# → http://localhost:8081 で確認
```

ファイルを編集したらブラウザをリロードするだけで反映される（ボリュームマウント）。

停止:
```bash
docker compose down
```

## デプロイフロー

```
dev ブランチに push
  → GitHub Actions: nginx 起動 → curl でページ確認
  → 通過したら main に自動マージ
  → Cloudflare Pages が main を検知して自動デプロイ
```

**作業ブランチは常に `dev`。`main` への直接 push は禁止。**

## ファイル構成

```
index.html       メインページ
style.css        スタイル
assets/          画像（ロゴ・アイコン・OGP）
_headers         Cloudflare Pages 用セキュリティヘッダー
docker-compose.yml  ローカルプレビュー用 nginx
.github/workflows/deploy.yml  CI/CD
```
