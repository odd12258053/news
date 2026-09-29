# 0007. 新規 routine は Claude Code から Default 環境・最小限のツールで作成する

- 日付: 2026-09-30
- 状態: Accepted

## 背景
既存の週刊 AI ダイジェストは claude.ai の Cowork から作成され、Cowork 専用の環境 ID・
長いシステムプロンプト・Documents 系ツールの許可・複数のコネクタ（Claude_Docs, Claude_Code_Remote）が
自動で付いている。新しい routine を追加するにあたり、同じ構成に揃えるか、別の構成にするかを決める必要があった。

## 決定
新規 routine は Claude Code の `RemoteTrigger create` で作成し、次を標準とする。
- 実行環境: Claude Code の Default 環境（`env_01JZgqWHmHCFqQkV1hS95esy`）
- 許可ツール: タスクに必要なものだけ。情報収集メール配信なら `WebSearch`, `WebFetch`, `mcp__Gmail__send_message`
- コネクタ: 必要なものだけ（Gmail のみ）。`send_message` は `always_allow` にして無人実行を止めない
- git リポジトリの clone はしない（このリポジトリの内容は prompt に含まれるため不要）
- モデル: 既存と同じ `claude-fable-5-1`

`routine.yaml` に `environment_id` と `allowed_tools`、コネクタの `connector_uuid` / `url` を書き、
`scripts/render.py` が create 用の body を組み立てる。

## 理由
- Cowork の環境 ID やシステムプロンプトは Anthropic 側の内部設定で、ファイルから再現できない。
  Claude Code から作るものは、ファイルだけで完全に再現できる構成にしておく方が、公開・再利用の目的に合う。
- 許可ツールを最小限にすると、無人実行で想定外の操作（ドキュメント作成、他 routine の操作）が起きない。

## 影響
- AI ダイジェスト（Cowork 由来）と新規 routine で `job_config` の形が異なる。AI ダイジェストの更新は
  引き続き ADR 0005 の `--current` 方式、新規 routine は create/update ともファイルから直接 render できる。
- 将来 AI ダイジェストもこの構成に揃える場合は、再作成になる（update で環境は変えられるが、Cowork 固有設定を消す判断が必要）。
- Default 環境で `WebSearch` / `WebFetch` が使えることは、初回実行の結果で確認する。
