# CLAUDE.md

このリポジトリは、Claude Code のスケジュール済みクラウドエージェント（routine）による
情報収集タスクの定義を管理し、変遷を記録し、公開するためのものです。

## 構成

```
routines/<name>/routine.yaml   # 名前・スケジュール(UTC cron)・モデル・コネクタ・vars
routines/<name>/prompt.md      # エージェントへの指示本体。{{KEY}} は vars で置換
routines/<name>/CHANGELOG.md   # 何を・なぜ変えたかの記録
scripts/render.py              # yaml + prompt から RemoteTrigger 用 body JSON を生成
docs/ADR/                      # 決定事項の記録 (Architecture Decision Records)
```

## 作業ルール

- **決定事項は必ず `docs/ADR/` に記録する。** 運用方針・構成・ツールの選択など、
  「なぜそうしたか」を後から問われる判断はすべて対象。書式と採番は `docs/ADR/README.md` に従う。
- **routine を変更したら、同じコミットで `CHANGELOG.md` に日付・変更点・理由を書く。**
  差分そのものは git log で追えるので、CHANGELOG には判断の理由を残す。
- **個人の値（メールアドレス等）は prompt.md に直接書かず、`{{KEY}}` と `vars` で分離する。**
  公開リポジトリなので、他者がそのまま再利用できる形を保つ。
- **個人情報にあたる値をリポジトリに含める前に、必ず利用者に確認する（ADR 0006）。**
  例外は `vars.RECIPIENT_EMAIL` の odd@agraffe.info（公開済みと確認済み）。
  氏名・所属・他サービスの ID・URL など、迷ったら確認する側に倒す。確認結果は ADR か CHANGELOG に残す。
- **prompt を書くときは egress 制約を前提にする（ADR 0008）。** 「実行環境の制約」節を置き、GitHub 上のソースを最優先、
  ブロックされたドメインへの再試行禁止、本文未確認の記事への注記を指示する。
- **クラウドへの反映は `README.md` の「更新の流れ」に従う。**
  routine の `job_config` は部分更新できないため、`RemoteTrigger get` の結果を
  `--current` に渡して prompt だけ差し替える。`*.current.json` はコミットしない。
- routine の削除は API からはできない。https://claude.ai/code/routines で行う。
- 文書・コミットメッセージ本文・CHANGELOG・ADR は日本語で書く（コミットの件名は英語でもよい）。

## Claude Code での操作

- routine の一覧・作成・更新・実行は `/schedule` スキル（内部では `RemoteTrigger` ツール）で行う。
- cron は UTC。利用者のタイムゾーンは Asia/Tokyo なので、変換結果を必ず明示する。
- 最短間隔は 1 時間。

## 現在の routine

| name | 実行 | 状態 |
|---|---|---|
| weekly-ai-digest | 毎週金曜 17:00 JST (`0 8 * * 5` UTC) | 稼働中。Cowork 由来のため git clone なし |
| weekly-python-rust-digest | 毎週月曜 08:00 JST (`0 23 * * 0` UTC) | 稼働中。Claude Code から作成（ADR 0007） |
| weekly-security-digest | 毎週金曜 21:00 JST (`0 12 * * 5` UTC) | 稼働中。Claude Code から作成。egress 制約前提の情報源設計（ADR 0008） |
