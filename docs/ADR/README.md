# Architecture Decision Records

このリポジトリで行った決定を記録する。1 決定 = 1 ファイル。

## 採番と命名

`NNNN-短い-スラッグ.md`。番号は 4 桁連番で欠番を作らない。
決定を覆す場合は新しい ADR を書き、古い方の状態を「Superseded by NNNN」に変える。ファイルは消さない。

## テンプレート

```markdown
# NNNN. タイトル

- 日付: YYYY-MM-DD
- 状態: Proposed | Accepted | Deprecated | Superseded by NNNN

## 背景
なぜこの判断が必要になったか。

## 決定
何をどうすると決めたか。

## 理由
他の選択肢と比べてなぜこれか。

## 影響
この決定で何が変わるか、注意点、やらなくなること。
```

## 一覧

| 番号 | タイトル | 状態 |
|---|---|---|
| [0001](0001-record-decisions-as-adr.md) | 決定事項を ADR として記録する | Accepted |
| [0002](0002-manage-routine-definitions-in-git.md) | routine の定義を git で管理し、クラウド側へ同期する | Accepted |
| [0003](0003-separate-personal-values-into-vars.md) | 個人の値を prompt から分離し vars で置換する | Accepted |
| [0004](0004-record-change-reasoning-in-changelog.md) | 変更の理由を routine ごとの CHANGELOG に残す | Accepted |
| [0005](0005-sync-by-swapping-prompt-into-cloud-job-config.md) | クラウド側の job_config を土台に prompt だけ差し替えて同期する | Accepted |
| [0006](0006-personal-information-policy.md) | 個人情報の取り扱い方針 | Accepted |
| [0007](0007-new-routines-from-claude-code-with-minimal-tools.md) | 新規 routine は Claude Code から Default 環境・最小限のツールで作成する | Accepted |
| [0008](0008-design-sources-around-egress-restrictions.md) | 情報源の指定は egress 制約を前提に GitHub 上のソースを優先する | Accepted |
