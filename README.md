# news — Claude Code 定期実行タスク（routine）の定義集

Claude Code のスケジュール済みクラウドエージェント（routine）で情報収集を行うための定義を、
このリポジトリで管理しています。目的は次の 3 つです。

1. **変遷の記録** — prompt やスケジュールを状況に応じて更新していくので、その理由と経過を残す
2. **再現性** — 定義をファイルとして持ち、クラウド側と同期できるようにする
3. **公開・共有** — 情報収集用の prompt を他の人がそのまま、または改変して使えるようにする

## 構成

```
routines/<routine名>/
  routine.yaml   # 名前・スケジュール・モデル・コネクタ・変数
  prompt.md      # エージェントへの指示（本体）。{{KEY}} は routine.yaml の vars で置換
  CHANGELOG.md   # 「何を・なぜ変えたか」の記録。差分そのものは git log で追う
scripts/render.py   # yaml + prompt から API に渡す JSON を生成
docs/ADR/           # 決定事項の記録。方針を決めたら必ず追加する
```

## routine 一覧

| routine | 実行 | 概要 |
|---|---|---|
| [weekly-ai-digest](routines/weekly-ai-digest/) | 毎週金曜 17:00 JST | 直近 1 週間の AI 関連ニュースを英語一次情報から集め、日本語ダイジェストを Gmail で送る |

## 更新の流れ（Claude Code 上で行う）

1. `routines/<name>/prompt.md` や `routine.yaml` を編集する
2. `CHANGELOG.md` に日付・変更点・理由を書く
3. クラウド側の現在値を取得して `routines/<name>/<name>.current.json` に保存する（`RemoteTrigger get`。gitignore 済み）
4. `python3 scripts/render.py routines/<name> --current routines/<name>/<name>.current.json` で body を生成する
5. Claude Code の `RemoteTrigger update` に渡して反映する
6. コミットする

Claude Code 上では `/schedule` と伝えれば、この手順を対話的に実行できます。

## 他の人が使うには

- `prompt.md` はそのまま自分の routine の prompt として使えます。`{{RECIPIENT_EMAIL}}` など `vars` の値は自分のものに置き換えてください。
- `routine.yaml` の `id` と `mcp_connections` の connector は利用者ごとに異なります。自分の claude.ai で Gmail 等を接続した上で routine を作成してください。
- routine の作成・管理画面: https://claude.ai/code/routines

## ライセンス

MIT
