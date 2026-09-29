# 変更履歴 — 週刊 Python/Rust ダイジェスト

新しいものを上に書く。各項目は「日付 / 何を変えたか / なぜ変えたか / 結果（分かれば）」。
細かい差分は git log で追えるので、ここには判断の理由を残す。

## 2026-09-30 — 初版

- 週刊 AI ダイジェストと同じ骨格（一次情報の収集 → 選別 → 日本語 HTML メール）で、対象を Python と Rust にした。
- Python と Rust は 1 本のメールにまとめた。routine を 1 つで管理でき、両言語にまたがる話題（uv, ruff, PyO3 など）を独立セクションで拾えるため。
- 各言語を「言語・ランタイム(コンパイラ) / ライブラリ・ツール / コミュニティ・記事」の 3 分野に分け、言語ごと 7〜10 件、全体トップ 3 を選ぶ構成。
- リリース情報は「何が変わったか・アップグレード時の注意点・バージョン番号」を優先させた。ニュース性より実務での判断材料を重視するため。
- 配信は月曜 08:00 JST（`0 23 * * 0` UTC）。週の初めに前週の動きを把握する用途。AI ダイジェスト（金曜 17:00）と曜日を分けた。
- Claude Code から作成したため、Cowork 由来の AI ダイジェストとは実行環境・許可ツールが異なる（ADR 0007）。
- クラウド側に作成済み（routine ID: trig_01DWMeQiTPUCFd9wU6VnnqkP）。定期実行の初回は 2026-10-05 月曜 08:06 JST。

### 結果: 2026-09-30 00:38 JST 手動実行（初回）

- 成功。所要 622 秒、161 ターン。Gmail 送信まで完了し、受信を確認した。
- 掲載件数: Python 13 件、Rust 12 件、両言語にまたがる話題 2 件。件数の目標（言語ごと 7〜10 件）はやや超過。
- トップ 3: Rust Leadership Council 9 月更新（LLM ポリシーチーム新設、Maintainers Fund 増額）、Cloudflare Python Workers GA、uv 0.12.18 / ty 0.0.84 のセキュリティ修正。
- **環境の制約**: Default 環境の egress proxy により、prompt で「優先する情報源」に挙げた多くのサイトへ直接アクセスできなかった。
  ブロックされた例: blog.rust-lang.org, blog.python.org, peps.python.org, discuss.python.org, realpython.com, lobste.rs, news.ycombinator.com, tokio.rs, rustsec.org, blog.pypi.org, 個人ブログ各種。
  エージェントは GitHub 上のソースリポジトリ（python/peps, rust-lang/blog.rust-lang.org, this-week-in-rust）と各プロジェクトの GitHub Releases、WebSearch の要約で代替し、メール冒頭にその旨を注記した。
- 課題: 直接読めないサイトへの WebFetch 試行が十数回無駄になっている。prompt の情報源リストを「GitHub 上のミラーを優先」に書き換えると、時間と精度の両面で改善が見込める（未対応）。
- 補足: allowed_tools に含めていない Bash が使用されていた（HTML の一時保存用）。環境側の既定で許可されている模様。
