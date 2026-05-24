# viora-landing

Viora ティザーランディングページ。静的 HTML/CSS（ビルド不要）。

## 開発フロー

```
dev ブランチで変更 → git push
  → GitHub Actions (verify): nginx 起動 → curl で疎通確認 → ✅ / ❌

/start-local-landing  ← dev 部門が実行
  → Docker で nginx 起動（自動確認含む）
  → オーナーが http://localhost:8081 をブラウザで視認確認

オーナー「OK」
  ↓
/deploy-landing  ← dev 部門が実行
  → spec 同期チェック → セキュリティ検証 → PR 作成 → main にマージ
  → Cloudflare Pages が自動デプロイ（反映まで約 1 分）
```

**作業ブランチは常に `dev`。`main` への直接 push は禁止。**

## ローカル操作（手動が必要な場合）

```bash
# 起動
docker compose up -d    # http://localhost:8081

# 停止
docker compose down
```

## ファイル構成

```
index.html               メインページ
style.css                スタイル
assets/                  画像（ロゴ・アイコン・OGP）
_headers                 Cloudflare Pages セキュリティヘッダー
docker-compose.yml       ローカルプレビュー用 nginx
.github/workflows/
  verify.yml             dev push 時の疎通確認
```
