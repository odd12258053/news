# 0008. 情報源の指定は egress 制約を前提に GitHub 上のソースを優先する

- 日付: 2026-09-30
- 状態: Accepted

## 背景
週刊 Python/Rust ダイジェストの初回実行（2026-09-30）で、Default 環境の egress proxy が
公式ブログ・掲示板・ニュースサイト・個人ブログの多くをブロックすることが分かった。
blog.rust-lang.org、peps.python.org、discuss.python.org、news.ycombinator.com なども対象で、
github.com と pypi.org は通る。エージェントはブロックされたサイトへの WebFetch を十数回無駄に試行した。

## 決定
routine の prompt を書くときは、次を標準とする。
1. prompt 内に「実行環境の制約」節を置き、egress 制約の存在と、通るドメイン（github.com, pypi.org）を明示する。
2. 一次情報は GitHub 上のソース（ソースリポジトリ、Releases、Security Advisories、advisory-database 系）を最優先にする。
3. それ以外のサイトは WebSearch の結果要約で把握し、必要なものだけ WebFetch を試す。EGRESS_BLOCKED になったドメインには再試行しない。
4. 本文を確認できなかった記事は、要約に「（検索要約に基づく）」と付けさせる。

## 理由
- 環境側の制約は routine から変えられない。prompt で前提を伝えた方が、無駄な試行を減らし所要時間と精度が改善する。
- 「GitHub にミラーがある一次情報」は多い（PEP、Rust ブログ、This Week in Rust、各種 advisory DB）。これを明示すれば一次情報主義を保てる。
- 確認できなかった記事を明示させることで、読者が情報の確度を判断できる。

## 影響
- 週刊セキュリティダイジェスト（2026-09-30 作成）から適用。
- 既存の週刊 Python/Rust ダイジェストと週刊 AI ダイジェストの prompt は未適用。次回改訂時に同じ節を追加する。
  ただし AI ダイジェストは Cowork 環境で動いており、egress 制約が同じかは未確認。
- 環境側の制約が変わった場合（許可ドメインの追加など）は、この節を更新する。
- 2026-09-30 の週刊セキュリティダイジェスト初回実行で追加判明: GitHub REST API はセッションに設定されたリポジトリ以外は使えない。
  GitHub 上のソースは Web ページ経由（`/advisories/GHSA-...`, `/releases`, `/security/advisories`, `/pull/<n>`）で読む。
  `blob/main/...` のファイル表示ページは本文を取れないことがあるため、Releases や PR ページを優先する。
