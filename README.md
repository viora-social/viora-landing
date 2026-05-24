# viora-landing

Viora ティザーランディングページ。静的 HTML/CSS（ビルド不要）。

## ローカル確認

```bash
bash serve.sh
# → http://localhost:8080 で確認
```

`serve.sh` は `.gitignore` 入り（ローカル専用）。Python 3 が必要（WSL 標準で利用可能）。

## 本番デプロイ

**デプロイ先**: Cloudflare Pages（`viora-social/viora-landing` リポジトリに連携済み）

**デプロイ方法**:

```
main ブランチへのマージ → Cloudflare Pages が自動デプロイ
```

1. `dev` ブランチで作業・確認
2. `main` へ PR を作成してマージ
3. Cloudflare Pages ダッシュボードでデプロイ完了を確認

**手動デプロイ**（緊急時）: Cloudflare Pages ダッシュボード → 該当プロジェクト → 「Retry deployment」

## ファイル構成

```
index.html     メインページ
style.css      スタイル
assets/        画像（ロゴ・アイコン・OGP）
_headers       Cloudflare Pages 用セキュリティヘッダー
```
