# 0005. クラウド側の job_config を土台に prompt だけ差し替えて同期する

- 日付: 2026-09-30
- 状態: Accepted

## 背景
routine の更新 API は `job_config` を部分更新できず、送ると丸ごと置き換わる。
既存の routine は Cowork 由来で、`job_config` に Cowork 固有のシステムプロンプト・環境 ID・
許可ツール・タグが入っている。これらをファイル側で完全に再現しようとすると、
Anthropic 側の内部設定をリポジトリに抱え込むことになる。

## 決定
更新時は `RemoteTrigger get` で現在の routine を取得して `routines/<name>/<name>.current.json` に保存し、
`scripts/render.py --current` でその `job_config` を土台に prompt とモデルだけを差し替えた body を作る。
`*.current.json` は gitignore し、コミットしない。

## 理由
- クラウド側の内部設定を壊さず、ファイルで管理したい部分（prompt・スケジュール・モデル・名前）だけを確実に上書きできる。
- システムプロンプト等は Anthropic の資産であり、公開リポジトリに含めるべきでない。

## 影響
- 更新のたびに get を挟む一手間が増える。
- 新規作成時は `--current` がないため、`routine.yaml` に `environment_id` と `allowed_tools` を書いて render する。
- クラウド側の内部設定が変わっても、ファイルには現れない。設定の乖離が疑われる場合は get の結果を目視で確認する。
